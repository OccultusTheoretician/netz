#!/usr/bin/env python3
"""arrive.py -- ANCHOR-2026-09-01: generation-time anchoring, the arrive step.

WHY THIS EXISTS

    The desk seals in the evening. When the evening is missed, every row whose
    window opened that day dies the next morning as retrodiction, because the
    gate cannot know the forecast existed before the window opened. Thirteen
    rows paid this on 2026-08-29; two more (MAG, Nepal) came within hours of
    it on 2026-08-31. The forecast files DID exist. Nothing proved it.

    This tool proves it. Every arm file is hashed the moment it lands and the
    digest is stamped through OpenTimestamps, so the file's existence at that
    hour is attested by calendars the operator does not control. The gate
    (ANCHOR-2026-09-01 lane A1 in kkr.py) reads anchor_log.json at ingest: a
    row whose window opened AFTER the file arrived seals under the disclosed
    class "late-seal, generation-anchored" instead of dying. A file that
    arrived after its window opened is no defence, and still dies.

WHAT IT DOES

    python arrive.py              sweep: hash + stamp every new arm file, append to anchor_log.json
    python arrive.py --no-stamp   sweep without calling the calendars (state 'unstamped'; hash still logged)
    python arrive.py --status     every anchor with its receipt state (unstamped / pending / anchored)
    python arrive.py --upgrade    try to upgrade pending receipts to Bitcoin attestations

    Arm files are *.json in the repo root whose name contains forecast,
    projection or refire, excluding control_packet_*. The log is append-only
    and keyed by sha256: an identical re-download changes nothing; an edited
    file is a new arrival with its own line. Receipts are written beside the
    file as <file>.ots and are committed like any other artifact.

    PENDING is honest and expected right after a stamp: the calendars hold the
    digest, Bitcoin does not yet. ANCHORED only after --upgrade succeeds.
    Claiming otherwise is the stated-versus-operational gap this desk audits.

FIRST RUN

    python arrive.py --no-stamp   baseline: files already on disk are logged
    unstamped, because they predate the tool and a stamp today would prove
    nothing about when they were written. Every later sweep stamps only new
    arrivals.

DRIVER

    Task Scheduler, hourly (see the delivery block), plus a manual run right
    after saving arm files. Both are idempotent.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
LOG = HERE / "anchor_log.json"
PATTERNS = ("forecast", "projection", "refire")

try:
    import ots_anchor as OA  # the desk's OTS client discovery, receipt reading, run()
except Exception:  # pragma: no cover
    OA = None


def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def arm_files():
    for p in sorted(HERE.glob("*.json")):
        n = p.name.lower()
        if n.startswith("control_packet_") or n == LOG.name:
            continue
        if any(k in n for k in PATTERNS):
            yield p


def load_log() -> list:
    if not LOG.exists():
        return []
    try:
        data = json.loads(LOG.read_text(encoding="utf-8"))
        return data if isinstance(data, list) else []
    except Exception:
        print(f"arrive: {LOG.name} unreadable - refusing to overwrite it; fix or move it first", file=sys.stderr)
        sys.exit(2)


def save_log(entries: list) -> None:
    LOG.write_text(json.dumps(entries, indent=1, ensure_ascii=True) + "\n", encoding="utf-8")


def receipt_for(p: Path) -> Path:
    return p.with_suffix(p.suffix + ".ots")


def receipt_state(rec: Path) -> str:
    if not rec.exists():
        return "unstamped"
    if OA is None:
        return "unknown (ots_anchor not importable)"
    try:
        st, _h, _ = OA.receipt_state(rec)
        return st
    except Exception as e:
        return f"unreadable ({type(e).__name__})"


def stamp(p: Path) -> tuple[str | None, str, str]:
    """Return (receipt name or None, state, client output tail)."""
    if OA is None or not OA.have_ots():
        return None, "unstamped", "opentimestamps-client not available"
    rec = receipt_for(p)
    if rec.exists():
        # a receipt from an earlier version of a same-named file: keep it, rename it aside
        try:
            old = OA.receipt_digest(rec)
        except Exception:
            old = None
        if old and old != sha256_file(p):
            rec.rename(rec.with_suffix(rec.suffix + "." + old[:8]))
        else:
            return rec.name, receipt_state(rec), "receipt already present for this digest"
    code, out = OA.run(["stamp", str(p)])
    if rec.exists():
        return rec.name, receipt_state(rec), out.strip()[-200:]
    return None, "unstamped", out.strip()[-400:] or f"ots exit {code}, no output"


def sweep(no_stamp: bool) -> int:
    log = load_log()
    known = {e.get("sha256") for e in log}
    added = 0
    for p in arm_files():
        digest = sha256_file(p)
        if digest in known:
            continue
        now = datetime.now(timezone.utc)
        entry = {
            "file": p.name,
            "sha256": digest,
            "bytes": p.stat().st_size,
            "mtime_utc": datetime.fromtimestamp(p.stat().st_mtime, tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "arrived_utc": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "receipt": None,
            "stamp_state": "unstamped",
        }
        if not no_stamp:
            rec, state, out = stamp(p)
            entry["receipt"], entry["stamp_state"] = rec, state
            if rec is None:
                entry["stamp_note"] = out
        log.append(entry)
        known.add(digest)
        added += 1
        print(f"arrive: {p.name} | sha {digest[:16]} | arrived {entry['arrived_utc']} | {entry['stamp_state']}"
              + ("" if entry.get("receipt") else " (no receipt)"))
    if added:
        save_log(log)
    print(f"arrive: {added} new arrival(s), {len(log)} anchored file(s) in {LOG.name}")
    return 0


def status() -> int:
    log = load_log()
    if not log:
        print("arrive: no anchors yet"); return 0
    for e in log:
        rec = HERE / e["receipt"] if e.get("receipt") else None
        st = receipt_state(rec) if rec else "unstamped"
        print(f"  {e['arrived_utc']}  {e['sha256'][:16]}  {st:9s}  {e['file']}")
    return 0


def upgrade() -> int:
    if OA is None or not OA.have_ots():
        print("arrive: opentimestamps-client not available"); return 2
    log = load_log(); changed = 0
    for e in log:
        rec = HERE / e["receipt"] if e.get("receipt") else None
        if not rec or not rec.exists():
            continue
        if receipt_state(rec) == "pending":
            OA.run(["upgrade", str(rec)])
            st = receipt_state(rec)
            if st != e.get("stamp_state"):
                e["stamp_state"], changed = st, changed + 1
            print(f"  {e['file']}: {st}")
    if changed:
        save_log(log)
    print(f"arrive: {changed} receipt(s) changed state")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--no-stamp", action="store_true", help="hash and log only; do not call the calendars")
    ap.add_argument("--status", action="store_true")
    ap.add_argument("--upgrade", action="store_true")
    a = ap.parse_args()
    if a.status:
        return status()
    if a.upgrade:
        return upgrade()
    return sweep(a.no_stamp)


if __name__ == "__main__":
    sys.exit(main())

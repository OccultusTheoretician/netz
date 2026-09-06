#!/usr/bin/env python3
"""
packet_commit.py — COMMIT THE ELICITATION INPUT WITHOUT PUBLISHING IT

WHY

    206 sealed entries name a `source_packet`. Every one of those files is
    excluded from the public repository by ignore rule. A stranger can
    recompute the seal, retrieve the report, read the entry and check the
    outcome — and cannot retrieve the text the forecaster was actually shown.

    RPAS-26 Amendment 2026-08-04, Part I·E states that limitation against the
    desk's own primary claim. This is the mechanism it names.

WHAT THIS CLOSES, AND WHAT IT DOES NOT

    CLOSES — retrofit. Once a packet's digest is committed and chained, the
    operator cannot quietly rewrite what an arm was shown after seeing how the
    row resolved. A stranger holding the packet later can verify it is the
    same bytes. That is a real property and nothing on the desk had it.

    DOES NOT CLOSE — readability. 1.04 asks whether a hit was DEDUCIBLE from
    the declared priors. A digest does not let anyone read the priors, so the
    keyed/keyless determination on those entries stays uncheckable by a third
    party. The commitment makes the input FIXED, not VISIBLE.

    The amendment's wording — that hash commitment "would close the
    limitation" — is therefore too strong, and this file is the correction.
    Half a remedy stated as a whole one is the exact failure class the
    amendment was written to report.

    Full closure requires publishing packet bodies, or publishing them under
    embargo until every row citing them has resolved. Both are operator
    rulings with real costs; neither is assumed here.

THE REGISTER

    docs/packet_register.json — one entry per packet, hash-chained in
    filename order so an insertion or deletion breaks the chain:

        {"packet": "kkr_packet_2026-08-03_1501.md",
         "sha256": "...", "bytes": 53769, "mtime_utc": "...",
         "rows": 16, "row_ids": [...],
         "prev": "...", "chain": "..."}

    `rows` counts sealed entries naming that packet, so the register carries
    its own denominator — the DECC-26 completeness control, applied to inputs.

USE
    python packet_commit.py                 report, write nothing
    python packet_commit.py --write         write the register
    python packet_commit.py --verify        recompute and compare
"""

import argparse
import hashlib
import json
import re
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
PACKETS = HERE / "forecasts"
REGISTER = HERE / "docs" / "packet_register.json"
TAG = b"netz/packet-register/1\x00"
GENESIS = "0" * 64


def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def chain(prev_hex: str, core: dict) -> str:
    blob = json.dumps(core, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(TAG + bytes.fromhex(prev_hex) + blob).hexdigest()


def _packet_stamp(name):
    """PACKETREG-2026-09-04: the YYYY-MM-DD[_HHMM] stamp inside a packet name, for
    chain order; a name without one sorts last."""
    m = re.search(r"(\d{4}-\d{2}-\d{2}(?:_\d{4})?)", name)
    return m.group(1) if m else "9999"


def build():
    led = HERE / "ledger.json"
    rows = json.loads(led.read_text(encoding="utf-8"))["projections"] \
        if led.exists() else []
    by_packet = {}
    for p in rows:
        k = (p.get("source_packet") or "").strip()
        if k:
            by_packet.setdefault(k, []).append(p.get("id"))

    # PACKETREG-2026-09-04: frame arms write kkr_packet_frame_<name>_<stamp>.md so
    # the frontier arms' packet is never touched; the register must see those too,
    # and order every packet by its stamp so the chain stays append-only.
    files = sorted([f for f in list(PACKETS.glob("kkr_packet_2*.md"))
                    + list(PACKETS.glob("kkr_packet_frame_*_2*.md"))
                    if f.name != "kkr_packet_latest.md"],
                   key=lambda f: (_packet_stamp(f.name), f.name))
    entries, prev = [], GENESIS
    for f in files:
        core = {
            "packet": f.name,
            "sha256": sha256_file(f),
            "bytes": f.stat().st_size,
            "mtime_utc": datetime.fromtimestamp(
                f.stat().st_mtime, timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "rows": len(by_packet.get(f.name, [])),
            "row_ids": sorted(x for x in by_packet.get(f.name, []) if x),
        }
        h = chain(prev, core)
        entries.append({**core, "prev": prev, "chain": h})
        prev = h

    named = set(by_packet)
    present = {f.name for f in files}
    return {
        "schema": "packet-register/1.0",
        "generated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "what_this_proves": (
            "Each digest fixes the bytes of an elicitation packet a sealed "
            "entry names. It proves the input was not rewritten after the "
            "outcome was known."),
        "what_this_does_not_prove": (
            "It does not make the input readable. RPAS-26 1.04 asks whether a "
            "hit was deducible from the declared priors; a digest does not "
            "disclose them, so the keyed/keyless determination on these "
            "entries remains uncheckable by a third party. The packet bodies "
            "are excluded from this repository by ignore rule. This register "
            "closes retrofit, not readability, and the distinction is stated "
            "because Amendment 2026-08-04 Part I-E overstated it."),
        "packets": len(entries),
        "rows_covered": sum(e["rows"] for e in entries),
        "named_but_absent": sorted(named - present),
        "present_but_unnamed": sorted(present - named),
        "head": prev,
        "entries": entries,
    }


def main():
    ap = argparse.ArgumentParser(description="commit elicitation packet digests")
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--verify", action="store_true")
    a = ap.parse_args()

    if not PACKETS.exists():
        sys.exit(f"no packet directory at {PACKETS}")
    reg = build()

    print(f"\nPACKET REGISTER — {reg['packets']} packet(s), "
          f"{reg['rows_covered']} sealed row(s) covered")
    print("-" * 66)
    for e in reg["entries"]:
        print(f"  {e['packet']:<34} {e['sha256'][:16]}…  "
              f"{e['bytes']:>7}B  {e['rows']:>3} row(s)")
    print(f"\n  chain head: {reg['head']}")
    if reg["named_but_absent"]:
        print(f"\n  NAMED BY A SEALED ROW BUT NOT ON DISK — "
              f"{len(reg['named_but_absent'])}:")
        for n in reg["named_but_absent"]:
            print(f"    {n}")
        print("    These rows name an input that no longer exists anywhere. "
              "That is a finding, not a gap to fill.")
    if reg["present_but_unnamed"]:
        print(f"\n  on disk, named by no sealed row: "
              f"{len(reg['present_but_unnamed'])}")

    if a.verify:
        if not REGISTER.exists():
            sys.exit("\nno register to verify against")
        old = json.loads(REGISTER.read_text(encoding="utf-8"))
        oldmap = {e["packet"]: e["sha256"] for e in old["entries"]}
        newmap = {e["packet"]: e["sha256"] for e in reg["entries"]}
        changed = [k for k in oldmap if k in newmap and oldmap[k] != newmap[k]]
        gone = [k for k in oldmap if k not in newmap]
        print()
        if changed:
            print(f"  DIGEST CHANGED on {len(changed)} committed packet(s) — "
                  f"an input a sealed row names has been rewritten:")
            for k in changed:
                print(f"    {k}")
        if gone:
            print(f"  COMMITTED PACKET NO LONGER ON DISK — {len(gone)}:")
            for k in gone:
                print(f"    {k}")
        if not changed and not gone:
            print("  VERIFY OK — every committed digest still matches its file.")
        return 2 if (changed or gone) else 0

    if a.write:
        REGISTER.parent.mkdir(exist_ok=True)
        REGISTER.write_text(json.dumps(reg, indent=1, ensure_ascii=False) + "\n",
                            encoding="utf-8")
        print(f"\n  register -> {REGISTER}")
    else:
        print("\n  Nothing written. Re-run with --write.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""
health.py — the desk's own uptime, on one face.

Every finding class KK24's audit surfaced was the same defect wearing four
coats: an instrument whose staleness was invisible on its own surface. The
KFK chain went seven days dark and nothing said so. The packet register fell
three packets behind and nothing said so. The freshness instrument was itself
the stalest tile on the site. WARDESK solved this locally with a banner; this
generalises the banner.

health_expect.json is the load-bearing half: it is the desk COMMITTING to a
cadence per surface, in a tracked file, so this page grades stated against
operational — the one method, pointed at the desk's own tempo.

Date extraction, in order of trust, provenance printed per row:
    1. an internal date field in the JSON (as_of / generated / generated_at /
       ts / updated / rendered / date) — the surface speaking for itself
    2. `git log -1` on the path — the repository speaking for it
    3. file mtime — untrusted, printed as such, only if git has no history

Special check, not a cadence: PACKET LAG. The register's `generated` is
compared against the newest kkr_packet_*.md on local disk (the packets are
gitignored; this check only runs where they exist and says so where they
don't). A register older than the newest packet means rows are sealing
against uncommitted inputs — the exact gap that grew for three days before
2026-08-06.

    python health.py            board to console + docs/health.json
    python health.py --check    board only, write nothing
Exit 0 clean · exit 2 if any STALE (printable, never blocking — a stale
manual chain is a finding to see, not a reason the site cannot publish).
"""

import argparse
import datetime as dt
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
EXPECT = HERE / "health_expect.json"
OUT = HERE / "docs" / "health.json"
DATE_KEYS = ("as_of", "generated", "generated_at", "ts", "updated",
             "rendered", "date")
ISO = re.compile(r"(\d{4}-\d{2}-\d{2})[T ](\d{2}:\d{2}(?::\d{2})?)")


def now() -> dt.datetime:
    return dt.datetime.now(dt.timezone.utc)


def parse_iso(s: str):
    m = ISO.search(str(s))
    if not m:
        return None
    t = f"{m.group(1)}T{m.group(2)}"
    if len(m.group(2)) == 5:
        t += ":00"
    try:
        d = dt.datetime.fromisoformat(t.replace("Z", ""))
        return d.replace(tzinfo=dt.timezone.utc)
    except ValueError:
        return None


def date_internal(p: Path):
    if p.suffix != ".json":
        return None
    try:
        d = json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return None
    if not isinstance(d, dict):
        return None
    for k in DATE_KEYS:
        if k in d and isinstance(d[k], str):
            got = parse_iso(d[k])
            if got:
                return got
    return None


def date_git(p: Path):
    try:
        r = subprocess.run(
            ["git", "log", "-1", "--format=%cI", "--", str(p)],
            cwd=HERE, capture_output=True, text=True, timeout=20)
        s = r.stdout.strip()
        if s:
            return dt.datetime.fromisoformat(s).astimezone(dt.timezone.utc)
    except Exception:
        pass
    return None


def fmt_age(hours: float) -> str:
    if hours < 48:
        return f"{hours:.1f}h"
    return f"{hours / 24:.1f}d"


def packet_lag(register_dt):
    """Register generated-time vs newest packet on local disk. Local-only by
    construction (packets are gitignored); absent packets is stated, not
    guessed at."""
    packs = sorted((HERE / "forecasts").glob("kkr_packet_2*.md"))
    if not packs:
        return {"checkable": False,
                "note": "no packets on this disk — lag not measurable here"}
    newest = packs[-1]
    newest_dt = dt.datetime.fromtimestamp(newest.stat().st_mtime,
                                          dt.timezone.utc)
    lag_h = (newest_dt - register_dt).total_seconds() / 3600 \
        if register_dt else None
    return {"checkable": True, "newest_packet": newest.name,
            "newest_packet_utc": newest_dt.strftime("%Y-%m-%dT%H:%MZ"),
            "lag_hours": round(lag_h, 1) if lag_h is not None else None,
            "behind": bool(lag_h and lag_h > 0.1),
            "note": ("register predates the newest packet — rows may be "
                     "sealing against uncommitted inputs"
                     if lag_h and lag_h > 0.1 else
                     "register covers the newest packet on disk")}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="board only, write nothing")
    a = ap.parse_args()

    exp = json.loads(EXPECT.read_text(encoding="utf-8"))
    t0 = now()
    rows, worst = [], "OK"
    order = {"OK": 0, "EVENT": 0, "LATE": 1, "NO-DATE": 2, "STALE": 3}

    for s in exp["surfaces"]:
        p = HERE / s["path"]
        provenance, moved = None, None
        if p.exists():
            moved = date_internal(p)
            provenance = "internal" if moved else None
            if not moved:
                moved = date_git(p)
                provenance = "git" if moved else None
            if not moved:
                moved = dt.datetime.fromtimestamp(p.stat().st_mtime,
                                                  dt.timezone.utc)
                provenance = "mtime (untrusted)"
        age_h = (t0 - moved).total_seconds() / 3600 if moved else None
        cad = s.get("cadence_hours")

        if not p.exists():
            state = "NO-DATE"
        elif moved is None:
            state = "NO-DATE"
        elif cad is None:
            state = "EVENT"
        elif age_h <= cad:
            state = "OK"
        elif age_h <= 2 * cad:
            state = "LATE"
        else:
            state = "STALE"
        if order[state] > order[worst]:
            worst = state

        rows.append({
            "name": s["name"], "path": s["path"], "lane": s["lane"],
            "cadence_hours": cad,
            "last_moved_utc": moved.strftime("%Y-%m-%dT%H:%MZ")
            if moved else None,
            "age_hours": round(age_h, 1) if age_h is not None else None,
            "provenance": provenance, "state": state,
            "note": s.get("note", "")})

    reg_row = next((r for r in rows
                    if r["path"] == "docs/packet_register.json"), None)
    reg_dt = None
    if reg_row and reg_row["last_moved_utc"]:
        reg_dt = parse_iso(reg_row["last_moved_utc"])
    lag = packet_lag(reg_dt)

    tile = {
        "schema": "health/1.0",
        "as_of": t0.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "charter": exp["charter"],
        "states": exp["states"],
        "summary": {k: sum(1 for r in rows if r["state"] == k)
                    for k in ("OK", "LATE", "STALE", "EVENT", "NO-DATE")},
        "worst": worst,
        "packet_lag": lag,
        "surfaces": rows,
    }

    print(f"\nINSTRUMENT HEALTH — {len(rows)} surface(s) · {t0:%d%H%MZ %b %y}"
          .upper())
    print("-" * 74)
    for r in sorted(rows, key=lambda r: -order[r["state"]]):
        cad = f"{r['cadence_hours']}h" if r["cadence_hours"] else "event"
        age = fmt_age(r["age_hours"]) if r["age_hours"] is not None else "—"
        print(f"  {r['state']:<7} {r['name']:<20} {cad:>6}  age {age:>6}  "
              f"[{r['provenance'] or 'missing'}] {r['lane']}")
    s = tile["summary"]
    print(f"\n  {s['OK']} OK · {s['LATE']} LATE · {s['STALE']} STALE · "
          f"{s['EVENT']} event · {s['NO-DATE']} no-date")
    if lag.get("checkable"):
        mark = "BEHIND" if lag["behind"] else "current"
        print(f"  packet register: {mark} — {lag['note']}")
    else:
        print(f"  packet register lag: {lag['note']}")

    if a.check:
        print("\n  --check: nothing written")
    else:
        OUT.write_text(json.dumps(tile, ensure_ascii=False, indent=2),
                       encoding="utf-8")
        print(f"\n  tile -> {OUT}")
    return 2 if worst == "STALE" else 0


if __name__ == "__main__":
    sys.exit(main())

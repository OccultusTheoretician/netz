#!/usr/bin/env python3
r"""
kfk_sightings.py - KriegForeKaster x WarDesk: the sighting join.

    tg_cluster grades EVENTS: did hostile sides agree something happened.
    KriegForeKaster holds CLAIMS about formations, each with a half-life.
    Neither answers what they jointly can: WHICH TRACKED FORMATIONS ARE
    BEING NAMED in the graded stream, by whom, at what grade, and when.

Every sighting is evidence fuel for the fast-decay blocks (location 14d,
posture 21d, commander 60d) and the recency layer the overlay face renders.
This tool READS the newest event artifact and WRITES one sighting register.
It never touches KriegForeKaster.json - promotion of a sighting into a
graded claim is the operator's judgment, exactly like kfk_promote.

MATCHING DOCTRINE (precision over recall, printed not implied):
    A formation matches on its full NAME or its DESIGNATION (designations
    under 4 characters are skipped - too collidable). Word-boundary,
    case-insensitive, ASCII-folded. No invented aliases, no fuzzy match:
    transliterated and colloquial forms will NOT match, and that recall
    floor is stated in the output rather than papered over.

INPUT:  newest forecasts\tg_events_*.json (the clustered, graded artifact -
        not the raw pull; the ohrwurm_link 07-30 lesson). The pull stamp and
        age print every run: newest-on-disk is not fresh (KK18).
OUTPUT: forecasts\kfk_sightings_<stamp>.json + kfk_sightings_latest.json
        (latest is a byte copy of the dated file).

    python kfk_sightings.py            newest event artifact
    python kfk_sightings.py --file forecasts\tg_events_2026-08-07_1745.json
"""

import argparse
import json
import re
import shutil
import sys
import unicodedata
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
FORECASTS = HERE / "forecasts"
DATA = HERE / "KriegForeKaster.json"

MIN_DESIGNATION = 4
EXCERPT = 160


def fold(s: str) -> str:
    return unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()


def load_formations():
    d = json.loads(DATA.read_text(encoding="utf-8"))
    recs = d.get("formations") or d.get("records") or []
    out = []
    for r in recs:
        pats = []
        for key in ("name", "designation"):
            v = (r.get(key) or "").strip()
            if not v or (key == "designation" and len(v) < MIN_DESIGNATION):
                continue
            pats.append(re.compile(r"\b" + re.escape(fold(v)) + r"\b"))
        if pats:
            out.append((r["id"], r.get("name", r["id"]), r.get("faction", "?"),
                        r.get("echelon", "?"), pats))
    return out, d.get("as_of", "?")


def newest_events():
    cands = sorted(FORECASTS.glob("tg_events_*.json"))
    return cands[-1] if cands else None


def event_text(e):
    parts = [e.get("statement", ""), " ".join(e.get("actors") or []),
             " ".join(e.get("anchor") or [])]
    for s in e.get("sources") or []:
        parts.append(s.get("text_en") or "")
    return parts


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", help="explicit tg_events_*.json (default: newest)")
    a = ap.parse_args()

    src = Path(a.file) if a.file else newest_events()
    if not src or not src.exists():
        print("no tg_events_*.json in forecasts\\ - run the daily first",
              file=sys.stderr)
        return 1
    stamp_m = re.search(r"(\d{4}-\d{2}-\d{2}_\d{4})", src.name)
    pull_stamp = stamp_m.group(1) if stamp_m else src.name
    age_h = (datetime.now(timezone.utc).timestamp() - src.stat().st_mtime) / 3600
    fresh_note = (f"pull {pull_stamp} - artifact age {age_h:.1f}h"
                  + ("" if age_h < 26 else " - STALE: newest-on-disk is not fresh (KK18); run the daily"))
    print(f"KFK-SIGHT - {fresh_note}", file=sys.stderr)

    raw = json.loads(src.read_text(encoding="utf-8"))
    events = raw.get("events") if isinstance(raw, dict) else raw
    if events is None:
        events = raw.get("kinetic", []) + raw.get("statements", []) if isinstance(raw, dict) else []
    formations, kfk_as_of = load_formations()

    sightings = {}
    n_hits = 0
    for e in events or []:
        folded = [fold(t) for t in event_text(e) if t]
        blob = " \n ".join(folded)
        for fid, name, faction, echelon, pats in formations:
            if not any(p.search(blob) for p in pats):
                continue
            # first matching source line for the excerpt; else the statement
            exc = ""
            for s in e.get("sources") or []:
                if any(p.search(fold(s.get("text_en") or "")) for p in pats):
                    exc = (s.get("text_en") or "")[:EXCERPT]
                    break
            if not exc:
                exc = (e.get("statement") or "")[:EXCERPT]
            rec = sightings.setdefault(fid, {
                "name": name, "faction": faction, "echelon": echelon,
                "n": 0, "first": None, "last": None, "top_grade": None,
                "hits": []})
            hit = {"date": e.get("last_seen") or e.get("first_seen"),
                   "zone": e.get("zone"), "grade": e.get("grade"),
                   "track": e.get("track"),
                   "sides": e.get("sides") or [],
                   "n_sides": e.get("n_sides"),
                   "excerpt": exc}
            rec["hits"].append(hit)
            rec["n"] += 1
            n_hits += 1
            for k, d0 in (("first", e.get("first_seen")), ("last", e.get("last_seen"))):
                if d0 and (rec[k] is None or (d0 < rec[k] if k == "first" else d0 > rec[k])):
                    rec[k] = d0
            g = e.get("grade")
            if g and (rec["top_grade"] is None or str(g) < str(rec["top_grade"])):
                rec["top_grade"] = g  # A < B < C lexically

    out = {"_meta": {
        "generated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "pull": src.name, "pull_note": fresh_note,
        "kfk_as_of": kfk_as_of,
        "formations_scanned": len(formations),
        "formations_sighted": len(sightings),
        "events_scanned": len(events or []),
        "total_hits": n_hits,
        "matching": ("strict name/designation, word-boundary, ascii-folded; "
                     "designations under 4 chars skipped. Recall floor: "
                     "transliterated and colloquial forms do not match - "
                     "precision is the design choice, and it is printed."),
    }, "sightings": sightings}

    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M")
    dated = FORECASTS / f"kfk_sightings_{stamp}.json"
    if dated.exists():
        dated = FORECASTS / f"kfk_sightings_{stamp}_2.json"
    dated.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    latest = FORECASTS / "kfk_sightings_latest.json"
    shutil.copyfile(dated, latest)  # byte copy - the KFK publish lesson

    print(f"KFK-SIGHT - {len(sightings)} formation(s) sighted in "
          f"{len(events or [])} event(s) ({n_hits} hit(s)) -> {dated.name} "
          f"(+ latest byte copy)", file=sys.stderr)
    for fid, r in sorted(sightings.items(), key=lambda kv: -kv[1]["n"])[:12]:
        print(f"    {fid:12s} {r['n']:3d} hit(s) - top grade {r['top_grade']}"
              f" - last {str(r['last'])[:16]} - {r['name'][:40]}", file=sys.stderr)
    if not sightings:
        print("    none - expected while the board is a national skeleton; "
              "the RU-UA order-of-battle walk is what feeds this instrument.",
              file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())

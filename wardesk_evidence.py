#!/usr/bin/env python3
"""
wardesk_evidence.py — Grade-A corpus evidence for open ledger rows.

THE CONTRACT (same family as mechanical_adjudicator.py)
Writes nothing to the ledger. `kkr --resolve` remains the only resolution
path. This tool is the adjudicator's corroboration sibling: the adjudicator
maps rows onto INSTRUMENT resolvers (prices, feeds); this maps rows onto
EVENT evidence the War Desk has already graded. It proposes; you resolve.

BLIND MATCHING. Rows are matched on statement text, deadline and issue date
only — the arm and the probability are never consulted during matching and
are revealed only in the output, so the evidence cannot be steered by who
forecast what at what odds.

INDEPENDENCE GUARD (the KK13 circularity flag, enforced). Rows whose
statement is about this desk's own corpus — origin claims, corpus-mention
forecasts — are skipped and listed: an instrument must not resolve a
forecast it is not independent of. Only Grade A (3+ hostile sides) proposes
by default; A rests on cross-bias corroboration and is the desk's most
independent product. --include-b widens to B and says so on every line.

WHAT A PROPOSAL IS AND IS NOT. Corpus evidence SUPPORTS early resolution of
an occurrence claim; it does not satisfy a resolution clause that names
Reuters or AP — check the row's own named sources before marking a hit. And
corpus ABSENCE is never proposed as a miss: this tool cannot see the world,
only the watched channels.

    python wardesk_evidence.py                 open rows vs newest pull
    python wardesk_evidence.py --include-b
    python wardesk_evidence.py --file forecasts\\tg_events_2026-07-30_0745.json
"""
import argparse
import glob
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from runguard import write_run_artifact   # KK21h

HERE = Path(__file__).resolve().parent

ZONE_WORDS = {
    "iran": {"iran", "iranian", "tehran"},
    "russia_ukraine": {"ukraine", "ukrainian", "russia", "russian"},
    "israel_gaza": {"israel", "gaza", "palestinian", "west bank"},
    "lebanon": {"lebanon", "lebanese", "beirut"},
    "yemen": {"yemen", "houthi", "red sea"},
}

SELF_REFERENTIAL = ("netz", "watched-channel", "watched channel", "corpus",
                    "ohrwurm", "this desk")


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8-sig"))


def newest_events(explicit=None):
    if explicit:
        p = Path(explicit)
        return p if p.exists() else None
    cands = []
    for base in (HERE / "forecasts", HERE, Path.cwd()):
        cands += glob.glob(str(base / "tg_events_*.json"))
    return Path(sorted(set(cands))[-1]) if cands else None


def norm(s):
    return re.sub(r"[^a-z0-9 ]+", " ", str(s).lower())


def anchors_of(e):
    out = []
    for k in ("anchor", "anchor_aliases", "anchor_variants"):
        out += [str(x).lower() for x in (e.get(k) or [])]
    return sorted(set(out))


def event_date(e):
    fs = e.get("first_seen") or ""
    return fs[:10]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", default=None)
    ap.add_argument("--include-b", action="store_true",
                    help="also propose from Grade B (two sides) — weaker, labelled")
    a = ap.parse_args()

    lp = HERE / "ledger.json"
    if not lp.exists():
        lp = Path.cwd() / "ledger.json"
        if not lp.exists():
            print("ledger.json not found beside the script or in cwd.",
                  file=sys.stderr)
            return 1
    src = newest_events(a.file)
    if src is None:
        print("no tg_events_*.json found and no --file given.", file=sys.stderr)
        return 1

    rows = [p for p in read_json(lp).get("projections", [])
            if p.get("status") == "open"]
    events = read_json(src).get("events", [])
    grades = ("A",) if not a.include_b else ("A", "B")
    pool = [e for e in events
            if str(e.get("grade", "")).startswith(grades)
            and e.get("track") == "kinetic"]

    skipped_selfref, proposals, no_support = [], [], 0

    for p in rows:
        stmt_raw = str(p.get("statement", ""))
        stmt = norm(stmt_raw)
        if any(t in stmt for t in SELF_REFERENTIAL):
            skipped_selfref.append(p.get("id"))
            continue

        # BLIND: only statement text + dates from here on
        issued = str(p.get("date_issued", "") or "")[:10]
        deadline = str(p.get("deadline", "") or "")[:10]
        lo, hi = issued or "0000-00-00", deadline or "9999-99-99"
        m = re.search(r"\bon (\d{4}-\d{2}-\d{2})\b", stmt_raw.lower())
        if m:  # single-date statements resolve on that date only
            lo = hi = m.group(1)

        matched = []
        for e in pool:
            d = event_date(e)
            if not (lo <= d <= hi):
                continue
            tier = None

            def word_in(w, text):
                return re.search(r"\b" + re.escape(w) + r"\b", text) is not None

            hit_anchor = [an for an in anchors_of(e) if an and word_in(an, stmt)]
            if hit_anchor:
                tier = "ANCHOR"
            else:
                zw = ZONE_WORDS.get(e.get("zone", ""), set())
                if any(word_in(w, stmt) for w in zw):
                    tier = "ZONE"
            if tier:
                matched.append((tier, hit_anchor, e))
        if matched:
            matched.sort(key=lambda t: (t[0] != "ANCHOR",
                                        -(t[2].get("n_sides") or 0)))
            proposals.append((p, matched))
        else:
            no_support += 1

    now = datetime.now(timezone.utc).strftime("%d%H%MZ %b %y").upper()
    out = []
    out.append("## WAR DESK EVIDENCE — corpus support for open rows\n")
    out.append(f"Pull: `{src.name}` · grades {'A only' if grades==('A',) else 'A+B'} "
               f"· rendered {now} · proposes only, resolves nothing\n")

    if not proposals:
        out.append("No open row finds Grade-A corpus support in this pull. "
                   "That is a statement about the watched channels, not the world.\n")
    for p, matched in proposals:
        out.append(f"**{p.get('id')}** · `{p.get('model','?')}` · "
                   f"{p.get('probability','?')}% · deadline {p.get('deadline','?')}")
        out.append(f"> {str(p.get('statement',''))[:220]}")
        for tier, hit_anchor, e in matched[:4]:
            g = str(e.get("grade", "?"))[:1]
            weak = " · ZONE-TIER (place not named in statement — weaker)" if tier == "ZONE" else ""
            bnote = " · Grade B: two sides only" if g == "B" else ""
            out.append(f"- [{g}] {', '.join(e.get('anchor') or ['?'])} · "
                       f"{e.get('zone','?')} · {e.get('n_sides','?')} sides "
                       f"({'/'.join(e.get('sides') or [])}) · "
                       f"{e.get('n_reports','?')} rpt · first seen "
                       f"{event_date(e)}"
                       f"{' · matched: ' + ', '.join(hit_anchor) if hit_anchor else ''}"
                       f"{weak}{bnote}")
        out.append("- CHECK the row's own resolution clause — corpus support "
                   "does not substitute for sources the clause names.")
        out.append("")

    if skipped_selfref:
        out.append(f"*Independence guard: skipped {len(skipped_selfref)} "
                   f"self-referential row(s) — an instrument must not resolve "
                   f"a forecast about itself: "
                   + ", ".join(skipped_selfref[:8])
                   + ("..." if len(skipped_selfref) > 8 else "") + "*")
    out.append(f"*{no_support} open row(s) with no corpus support in this "
               "pull — absence here proposes nothing.*\n")
    out.append("*Resolution path unchanged: `python kkr.py --resolve --all` "
               "(interactive) is the only writer.*")

    md = "\n".join(out)
    dest = HERE / "forecasts"
    dest.mkdir(exist_ok=True)
    stamp = src.stem.replace("tg_events_", "")
    dated = dest / f"EVIDENCE_{stamp}.md"
    latest = dest / "EVIDENCE_latest.md"
    # KK21h: dated artifacts go through the guard; the latest pointer does not.
    dated = write_run_artifact(dated, md, tag="evidence")
    latest.write_text(md, encoding="utf-8")

    print(f"EVIDENCE · {len(rows)} open rows vs {len(pool)} graded kinetic "
          f"event(s) [{'A' if grades==('A',) else 'A+B'}]")
    print(f"EVIDENCE · {len(proposals)} row(s) with corpus support · "
          f"{len(skipped_selfref)} skipped by independence guard · "
          f"{no_support} without support")
    for p, matched in proposals[:6]:
        tier0 = matched[0][0]
        print(f"    {p.get('id')}  <- {len(matched)} event(s), best tier {tier0}")
    print(f"EVIDENCE · brief -> {dated}")
    print(f"EVIDENCE · brief -> {latest}")
    print("EVIDENCE · resolve (interactive, the only writer): "
          "python kkr.py --resolve --all")
    return 0


if __name__ == "__main__":
    sys.exit(main())

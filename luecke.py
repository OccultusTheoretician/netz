#!/usr/bin/env python3
"""luecke.py - DIE LUECKE. The completeness audit.

Every forecasting ledger in existence tests ONE assertion: were the calls
that were made correct. That is an EXISTENCE test - it grades the recorded
population against outcomes. No forecasting record publishes the other
assertion, the one auditors have known for a century is the harder of the
two: COMPLETENESS. What happened that was never called at all.

A Brier score cannot see an uncalled event. A forecaster who calls only
safe ground scores well and forecasts nothing. The ledger's own silence is
invisible to every metric the ledger computes about itself.

This instrument measures it. The desk's own collection surfaces
cross-bias CONFIRMED events daily - Grade A (three or more hostile sides
agreeing on a specific anchor) and Grade B (two sides). Those are events
the desk SAW. Against them it sets every row on the book, open and
resolved, and asks a single question per event:

    Did any row on this book name this ground?

An event confirmed at Grade A that no row names is a LUECKE - a gap. Not
a miss: a miss is a call that failed. A gap is ground the instrument's own
eyes reported and its forecasting arm never spoke to. In CALM terms it is
the conditional abyssal zero-point sitting inside the scoped region - the
blind spot in the middle of the map, which is the dangerous kind.

WHAT THIS IS NOT. Coverage is not a score and is deliberately not
published as one. A desk cannot forecast every confirmed event and should
not try; some ground is unforecastable and some is not worth a row. The
number is a DENOMINATOR the ledger otherwise hides, and its movement over
time under a fixed collection is the measurement. A rising gap rate with a
steady channel set means the forecasting arm is narrowing while the eyes
stay open.

MATCHING IS DELIBERATELY GENEROUS, AND THE DIRECTION IS PRINTED. An anchor
counts as named if its token appears in any row's statement or resolution.
Generous matching UNDERSTATES the gap, so every figure here is a floor:
the true gap is at least this large and may be larger. An audit that
errs should err against its own headline.

Read-only. Writes forecasts/luecke_latest.json + LUECKE_latest.md and a
docs mirror. ASCII only.
"""
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "forecasts"
DOCS = HERE / "docs"

ANCHOR = re.compile(r"^\*\*(.+?)\s+[^A-Za-z0-9]\s+(.+?Theatre)\*\*\s*$")
GRADE = re.compile(r"^\*\*.*GRADE\s+([ABC]).*\*\*\s*$")
ALIAS = {
    "kyiv": ["kyiv", "kiev"], "odesa": ["odesa", "odessa"],
    "kharkiv": ["kharkiv", "kharkov"], "dnipro": ["dnipro", "dnepr",
                                                  "dnipropetrovsk"],
    "sloviansk": ["sloviansk", "slavyansk"],
    "konstantinovka": ["konstantinovka", "kostiantynivka"],
    "zaporizhzhia": ["zaporizhzhia", "zaporozhye"],
    "gaza city": ["gaza"], "khan younis": ["khan younis", "khan yunis"],
}


def parse_wardesk(path):
    """Grade A and B kinetic anchors from a WARDESK render. Statement-track
    entries are quoted and skipped - an utterance is not ground."""
    out, grade = [], None
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        g = GRADE.match(line.strip())
        if g:
            grade = g.group(1)
            continue
        if grade not in ("A", "B"):
            continue
        m = ANCHOR.match(line.strip())
        if not m:
            continue
        anchor = m.group(1).strip()
        if anchor.startswith(("\u201c", '"', "[")):
            continue
        out.append({"anchor": anchor, "zone": m.group(2).strip(),
                    "grade": grade})
    return out


def names(anchor):
    a = anchor.lower().strip()
    return ALIAS.get(a, [a])


def main():
    stamp = None
    for a in sys.argv[1:]:
        if re.fullmatch(r"\d{4}-\d{2}-\d{2}.*", a):
            stamp = a
    wd = (OUT / f"WARDESK_{stamp}.md") if stamp else (OUT / "WARDESK_latest.md")
    if not wd.exists():
        cands = sorted(OUT.glob("WARDESK_2026-*.md"))
        if not cands:
            print("LUECKE - no WARDESK render found", file=sys.stderr)
            return 1
        wd = cands[-1]
    events = parse_wardesk(wd)
    if not events:
        print(f"LUECKE - {wd.name} parsed to zero anchors - INDETERMINATE, "
              f"not zero gaps", file=sys.stderr)
        return 1

    led = json.loads((HERE / "ledger.json").read_text(encoding="utf-8"))
    rows = led["projections"]
    hay = []
    for p in rows:
        hay.append((p["id"], (str(p.get("statement", "")) + " "
                              + str(p.get("resolution", ""))).lower(),
                    str(p.get("status", "")), str(p.get("model", ""))))

    seen, results = set(), []
    for e in events:
        key = (e["anchor"].lower(), e["zone"], e["grade"])
        if key in seen:
            continue
        seen.add(key)
        toks = names(e["anchor"])
        hits = [(rid, st, arm) for rid, txt, st, arm in hay
                if any(t in txt for t in toks)]
        results.append({**e, "rows_naming": [h[0] for h in hits[:12]],
                        "n_rows": len(hits),
                        "open_rows": sum(1 for h in hits if h[1] == "open"),
                        "arms": sorted({h[2] for h in hits})[:8],
                        "covered": bool(hits)})

    a_all = [r for r in results if r["grade"] == "A"]
    b_all = [r for r in results if r["grade"] == "B"]
    gaps_a = [r for r in a_all if not r["covered"]]
    gaps_b = [r for r in b_all if not r["covered"]]
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    def rate(g, tot):
        return (round(100.0 * len(g) / len(tot), 1) if tot else None)

    out = {"_meta": {
        "generated": now, "instrument": "luecke/1.0",
        "source_render": wd.name, "ledger_rows": len(rows),
        "doctrine": ("a Brier cannot see an uncalled event; this is the "
                     "completeness assertion a forecasting ledger otherwise "
                     "hides. Coverage is a denominator, not a score."),
        "matching": ("generous - an anchor counts as named if its token or a "
                     "known alias appears in any row's statement or "
                     "resolution. Generous matching UNDERSTATES the gap, so "
                     "every figure here is a floor."),
        "grade_a_confirmed": len(a_all), "grade_a_gaps": len(gaps_a),
        "grade_a_gap_rate_pct": rate(gaps_a, a_all),
        "grade_b_confirmed": len(b_all), "grade_b_gaps": len(gaps_b),
        "grade_b_gap_rate_pct": rate(gaps_b, b_all)},
        "events": results}

    OUT.mkdir(exist_ok=True)
    blob = json.dumps(out, indent=1, ensure_ascii=False) + "\n"
    (OUT / "luecke_latest.json").write_text(blob, encoding="utf-8")
    if DOCS.exists():
        (DOCS / "luecke_latest.json").write_text(blob, encoding="utf-8")

    md = [f"# DIE LUECKE - the completeness audit - {now}", "",
          "Every forecasting ledger tests whether the calls it made were "
          "right. That is an existence test. This is the other assertion: "
          "what the desk's own eyes confirmed and its forecasting arm never "
          "called.", "",
          f"Source render: `{wd.name}` - ledger {len(rows)} rows, open and "
          f"resolved.", "",
          f"**Grade A confirmed: {len(a_all)} - never named by any row: "
          f"{len(gaps_a)}"
          + (f" ({rate(gaps_a, a_all)}%)**" if a_all else "**"), "",
          f"**Grade B corroborated: {len(b_all)} - never named: "
          f"{len(gaps_b)}"
          + (f" ({rate(gaps_b, b_all)}%)**" if b_all else "**"), "",
          "> Matching is generous by design, so these are FLOORS: the true "
          "gap is at least this large. Coverage is a denominator, not a "
          "score - a desk cannot forecast every confirmed event and should "
          "not try. What the number measures is movement under a fixed "
          "collection.", ""]
    if gaps_a or gaps_b:
        md.append("## The gaps - confirmed ground, no row")
        for r in gaps_a + gaps_b:
            md.append(f"- **{r['anchor']}** - {r['zone']} - Grade "
                      f"{r['grade']} - no row on the book names it")
        md.append("")
    md.append("## Covered")
    for r in results:
        if r["covered"]:
            md.append(f"- {r['anchor']} ({r['zone']}, {r['grade']}) - "
                      f"{r['n_rows']} row(s), {r['open_rows']} open - "
                      f"{', '.join(r['arms'][:4])}")
    md.append("")
    md.append("luecke/1.0 - read-only - the gap is the measurement")
    (OUT / "LUECKE_latest.md").write_text("\n".join(md) + "\n",
                                          encoding="utf-8")

    print(f"LUECKE - {wd.name}: Grade A {len(gaps_a)}/{len(a_all)} uncalled"
          + (f" ({rate(gaps_a, a_all)}%)" if a_all else "")
          + f" - Grade B {len(gaps_b)}/{len(b_all)} uncalled", file=sys.stderr)
    print(f"LUECKE - json -> {OUT / 'luecke_latest.json'}", file=sys.stderr)
    print(f"LUECKE - md   -> {OUT / 'LUECKE_latest.md'}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())

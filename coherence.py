#!/usr/bin/env python3
"""
coherence.py - the coherence bank. Does a forecaster contradict itself?

WHAT THIS MEASURES, AND WHAT IT REFUSES TO

A Brier says whether a forecaster was right. It says nothing about whether
the forecaster was COHERENT - whether the set of probabilities it asserted
could all be true of one world at once. Coherence is checkable the moment
the rows are sealed, years before any of them resolve, and it needs no
outcome at all.

The rule used here is the weakest defensible one, monotonicity:

    if claim A's success set is a SUBSET of claim B's success set,
    then P(A) must be <= P(B).

Brent settling above 100 is a subset of Brent settling above 90, so a
forecaster asserting 30% on the first and 22% on the second has asserted
something no world satisfies. That is a defect in the forecaster, printed
without waiting for the market.

WHAT IT DOES NOT DO, BY RULE

  - It does not score. Nothing here enters a Brier, and incoherence is
    reported as its own class, never folded into accuracy.
  - It does not compare arms against each other as a fault. A Brier
    belongs to one forecaster (the desk's arm-identity law), and two
    forecasters disagreeing is not an error by either. Cross-arm spread
    is printed as MEASUREMENT, in its own section, with no verdict.
  - It excludes control/baserate by default. That arm's probabilities are
    assigned mechanically from domain rates, so testing it for reasoning
    coherence measures the assignment table, not a forecaster.

THE GUARDS, AND WHY EACH EXISTS

Every one was added because the unguarded version produced a false
positive on the live ledger, measured 2026-08-18:

  DIRECTION   "settle below 85" vs "settle below 80": the higher bar is
              EASIER for a below-claim, so P must be >=, not <=. The
              unguarded check called a coherent pair a violation.
  INSTRUMENT  Brent is not WTI, and a 10-year yield is not a 30-year.
              Word overlap alone matched across instruments.
  WINDOW      A threshold over a four-day window and the same threshold
              over three months are different claims. Only same-window
              pairs are checked STRICT; nested windows with the SAME
              threshold are checked WEAK, where the longer window must
              carry the higher probability.

Usage:
    python coherence.py                 within-arm check + cross-arm spread
    python coherence.py --strict-only   suppress the nested-window class
    python coherence.py --include-control
    python coherence.py --out FILE      write the report as well as print

Standard library only. Reads the ledger. Writes nothing to it.
Exit code 1 if any violation is found, so it is CI-wireable.
"""

import argparse
import itertools
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
LEDGER = HERE / "ledger.json"

ERAS = {"lmstudio/auto": [("pre-verbot", None, "2026-07-28"),
                          ("post-verbot", "2026-07-28", "2026-08-03"),
                          ("post-window", "2026-08-03", None)]}

# instrument keys. Order matters: the first match wins, so more specific
# patterns are listed first. A row matching none is not comparable and is
# dropped rather than guessed at.
INSTRUMENTS = [
    ("brent",      r"\bbrent\b"),
    ("wti",        r"\bwti\b|west texas"),
    ("ust30",      r"30[- ]year.{0,24}(?:treasury|yield)|dgs30"),
    ("ust10",      r"10[- ]year.{0,24}(?:treasury|yield)|dgs10|10-year treasury"),
    ("ust2",       r"\b2[- ]year.{0,24}(?:treasury|yield)|dgs2\b"),
    ("gold",       r"\bgold\b"),
    ("natgas",     r"natural gas|henry hub"),
    ("sp500",      r"s&p 500|sp500"),
    ("btc",        r"\bbitcoin\b|\bbtc\b"),
    ("eurusd",     r"euro.{0,12}dollar|eur/usd"),
    ("fedfunds",   r"federal funds"),
    ("kev_count",  r"known exploited vulnerabilities.{0,40}(?:entries|catalog)"),
    ("quake_mag",  r"magnitude\s*\d"),
]

ABOVE = r"(?:at or above|above|at least|exceed(?:s|ing)?|greater than|no lower than|or higher)"
BELOW = r"(?:at or below|below|at most|no more than|less than|or lower)"
DATE = re.compile(r"(20\d{2}-\d{2}-\d{2})")


def arm_of(r):
    m = r.get("model", "?")
    d0 = str(r.get("date_issued", ""))
    es = ERAS.get(m)
    if not es:
        return m
    tag = m
    for eid, frm, until in es:
        if until and d0 < until:
            return f"{m}[{eid}]"
        if frm and d0 >= frm:
            tag = f"{m}[{eid}]"
    return tag


def instrument(text):
    low = text.lower()
    for key, pat in INSTRUMENTS:
        if re.search(pat, low):
            return key
    return None


def bound(text):
    """(direction, threshold) or None. Direction is the side the claim
    asserts the value lands on."""
    m = re.search(ABOVE + r"\s+\$?([\d,]+\.?\d*)", text, re.I)
    if m:
        return "above", float(m.group(1).replace(",", ""))
    m = re.search(BELOW + r"\s+\$?([\d,]+\.?\d*)", text, re.I)
    if m:
        return "below", float(m.group(1).replace(",", ""))
    return None


def window(r):
    ds = sorted(set(DATE.findall(r.get("statement", "") or "")))
    if len(ds) >= 2:
        return ds[0], ds[-1]
    d0 = str(r.get("date_issued", ""))[:10]
    dl = str(r.get("deadline", ""))[:10]
    return (d0, dl) if d0 and dl else None


def nested(a, b):
    """True if window a is contained in window b."""
    return a[0] >= b[0] and a[1] <= b[1]


def main():
    ap = argparse.ArgumentParser(description="coherence bank over the sealed ledger")
    ap.add_argument("--strict-only", action="store_true")
    ap.add_argument("--include-control", action="store_true")
    ap.add_argument("--out")
    a = ap.parse_args()

    rows = json.loads(LEDGER.read_text(encoding="utf-8"))["projections"]
    out, W = [], None
    W = out.append
    W("COHERENCE BANK - does a forecaster contradict itself?")
    W("=" * 72)

    parsed = []
    for r in rows:
        p = r.get("probability")
        st = r.get("statement", "") or ""
        if p is None:
            continue
        arm = arm_of(r)
        if not a.include_control and arm.startswith("control/"):
            continue
        ins, bd, win = instrument(st), bound(st), window(r)
        if ins and bd and win:
            parsed.append(dict(id=r.get("id"), arm=arm, ins=ins, dirn=bd[0],
                               thr=bd[1], win=win, p=float(p), st=st))
    W(f"  {len(rows)} sealed rows | {len(parsed)} carry a comparable "
      f"instrument, direction, threshold and window")
    W(f"  control/baserate {'INCLUDED' if a.include_control else 'excluded'} "
      f"- its probabilities are assigned, not reasoned")

    strict, weak = [], []
    for x, y in itertools.combinations(parsed, 2):
        if x["arm"] != y["arm"] or x["ins"] != y["ins"] or x["dirn"] != y["dirn"]:
            continue
        # STRICT: identical window, different threshold. The harder bar
        # must not carry the higher probability.
        if x["win"] == y["win"] and x["thr"] != y["thr"]:
            hard, easy = ((x, y) if
                          ((x["thr"] > y["thr"]) == (x["dirn"] == "above"))
                          else (y, x))
            if hard["p"] > easy["p"]:
                strict.append((hard, easy))
        # WEAK: same threshold and direction, one window nested in the
        # other. More time cannot make a threshold less likely to be hit.
        elif x["thr"] == y["thr"] and x["win"] != y["win"]:
            if nested(x["win"], y["win"]):
                inner, outer = x, y
            elif nested(y["win"], x["win"]):
                inner, outer = y, x
            else:
                continue
            if inner["p"] > outer["p"]:
                weak.append((inner, outer))

    def show(pair, lab_a, lab_b):
        h, e = pair
        W(f"  [{h['arm']}] {h['ins']} {h['dirn']}")
        W(f"    {lab_a:<22} p={h['p']:>5}  {h['id']}  {h['win'][0]}..{h['win'][1]}")
        W(f"      {h['st'][:96]}")
        W(f"    {lab_b:<22} p={e['p']:>5}  {e['id']}  {e['win'][0]}..{e['win'][1]}")
        W(f"      {e['st'][:96]}")
        W("")

    W("")
    W("STRICT - same arm, same instrument, same window, nested thresholds")
    W("-" * 72)
    if strict:
        for pr in strict:
            show(pr, "harder bar", "easier bar")
        W(f"  {len(strict)} violation(s): the harder claim carries the higher")
        W("  probability. No world satisfies both assertions.")
    else:
        W("  none. Every same-window threshold pair is ordered correctly.")

    if not a.strict_only:
        W("")
        W("WEAK - same threshold, one window inside the other")
        W("-" * 72)
        if weak:
            for pr in weak:
                show(pr, "shorter window", "longer window")
            W(f"  {len(weak)} violation(s): more time cannot make a threshold")
            W("  less likely to be reached at least once.")
        else:
            W("  none.")

    # cross-arm: measurement, never a verdict
    W("")
    W("CROSS-ARM SPREAD - measurement, not a finding")
    W("-" * 72)
    W("  Two forecasters disagreeing is not an error by either. A Brier")
    W("  belongs to one forecaster; nothing below is scored or attributed.")
    groups = {}
    for r in parsed:
        groups.setdefault((r["ins"], r["dirn"], r["thr"], r["win"]), []).append(r)
    shown = 0
    for k, g in sorted(groups.items(), key=lambda kv: -(
            max(x["p"] for x in kv[1]) - min(x["p"] for x in kv[1]))):
        arms = {x["arm"] for x in g}
        if len(arms) < 2:
            continue
        spread = max(x["p"] for x in g) - min(x["p"] for x in g)
        if spread <= 0:
            continue
        W(f"  {k[0]} {k[1]} {k[2]:g}  {k[3][0]}..{k[3][1]}   spread {spread:g} pts")
        for x in sorted(g, key=lambda z: -z["p"]):
            W(f"      p={x['p']:>5}  {x['arm']:<34} {x['id']}")
        shown += 1
        if shown >= 8:
            break
    if not shown:
        W("  no two arms priced an identical claim over an identical window.")

    W("")
    W("Coherence is checkable at seal. None of it waits on an outcome, and")
    W("none of it is scored.")
    text = "\n".join(out)
    print(text)
    if a.out:
        Path(a.out).write_text(text + "\n", encoding="ascii", errors="replace")
        print(f"\n[written] {a.out}")
    return 1 if (strict or (weak and not a.strict_only)) else 0


if __name__ == "__main__":
    sys.exit(main())

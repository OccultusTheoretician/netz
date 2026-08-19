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
                               thr=bd[1], win=win, p=float(p), st=st,
                               day=str(r.get("date_issued", ""))[:10]))
    W(f"  {len(rows)} sealed rows | {len(parsed)} carry a comparable "
      f"instrument, direction, threshold and window")
    W(f"  control/baserate {'INCLUDED' if a.include_control else 'excluded'} "
      f"- its probabilities are assigned, not reasoned")

    strict, weak, revision = [], [], []
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
                (strict if hard["day"] == easy["day"] else revision).append(
                    (hard, easy, "threshold"))
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
                (weak if inner["day"] == outer["day"] else revision).append(
                    (inner, outer, "window"))

    def show(pair, lab_a, lab_b):
        h, e = pair[0], pair[1]
        W(f"  [{h['arm']}] {h['ins']} {h['dirn']}")
        W(f"    {lab_a:<22} p={h['p']:>5}  {h['id']}  {h['win'][0]}..{h['win'][1]}")
        W(f"      {h['st'][:96]}")
        W(f"    {lab_b:<22} p={e['p']:>5}  {e['id']}  {e['win'][0]}..{e['win'][1]}")
        W(f"      {e['st'][:96]}")
        W("")

    W("")
    W("STRICT - SAME ELICITATION, same arm, same instrument, same window")
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
        W("WEAK - SAME ELICITATION, same threshold, one window inside the other")
        W("-" * 72)
        if weak:
            for pr in weak:
                show(pr, "shorter window", "longer window")
            W(f"  {len(weak)} violation(s): more time cannot make a threshold")
            W("  less likely to be reached at least once.")
        else:
            W("  none.")

    W("")
    W("REVISION - the same arm, different elicitations, nested claims")
    W("-" * 72)
    W("  NOT a violation, and the distinction is the whole point. Monotonicity")
    W("  binds one belief state at one moment. These pairs were sealed on")
    W("  different days from different packets, so the later row reflects")
    W("  information the earlier one did not have. Revising a subset event")
    W("  upward on new evidence is correct forecasting, not contradiction.")
    W("  The arms are also elicited cold and never see their own sealed rows,")
    W("  so cross-day consistency is not something they can maintain.")
    W("  What is measured here is belief volatility, and nothing is scored.")
    if not revision:
        W("  none.")
    else:
        for pair in revision:
            h, e, kind = pair
            later, earlier = (h, e) if h["day"] >= e["day"] else (e, h)
            W(f"  [{h['arm']}] {h['ins']} {h['dirn']} - {kind}, "
              f"{abs(h['p'] - e['p']):g} pt move")
            W(f"    {earlier['day']}  p={earlier['p']:>5}  {earlier['id']}  "
              f"{earlier['win'][0]}..{earlier['win'][1]}")
            W(f"    {later['day']}  p={later['p']:>5}  {later['id']}  "
              f"{later['win'][0]}..{later['win'][1]}")
            W("")
        W(f"  {len(revision)} revision(s) recorded.")

    # cross-arm DISPERSION: same elicitation day, same subject, every arm
    # that priced it. This is the banked surface - not contradiction
    # detection but agreement measurement, and it needs no threshold parsing,
    # which is why it sees claims the sections above cannot.
    W("")
    W("CROSS-ARM DISPERSION - same day, same subject, measurement only")
    W("-" * 72)
    W("  Two forecasters disagreeing is not an error by either. A Brier belongs")
    W("  to one forecaster; nothing below is scored or attributed as a fault.")
    W("  control/baserate is printed as a reference line, never in the spread.")
    STOP = set("""between and the a an of at least on or for with will
        that which within from before after during any one two three
        least most more than 2026 2027 utc""".split())

    def cwords(s):
        return {w for w in re.findall(r"[a-z]{4,}", (s or "").lower())
                if w not in STOP}

    byday = {}
    for r in rows:
        if r.get("probability") is None:
            continue
        byday.setdefault(str(r.get("date_issued"))[:10], []).append(r)
    clusters = []
    for d0, g in byday.items():
        used = set()
        for i, x in enumerate(g):
            if i in used:
                continue
            wx = cwords(x.get("statement"))
            if len(wx) < 4:
                continue
            grp = [x]
            used.add(i)
            for j in range(i + 1, len(g)):
                if j in used:
                    continue
                wy = cwords(g[j].get("statement"))
                if len(wy) < 4:
                    continue
                if len(wx & wy) / max(1, len(wx | wy)) >= 0.50:
                    grp.append(g[j])
                    used.add(j)
            real = [r for r in grp if not str(r.get("model", "")).startswith("control/")]
            byarm = {}
            for r in real:
                byarm.setdefault(arm_of(r), []).append(float(r["probability"]))
            # A cluster can hold two rows from ONE arm. Folding those into the
            # cross-arm spread reports a forecaster's disagreement with itself
            # as disagreement between forecasters. Spread is computed across
            # arm medians; a within-arm split is flagged in its own right.
            split = {a: sorted(set(v)) for a, v in byarm.items() if len(set(v)) > 1}
            if len(byarm) >= 2:
                meds = []
                for v in byarm.values():
                    v = sorted(v)
                    meds.append(v[len(v) // 2] if len(v) % 2 else
                                (v[len(v) // 2 - 1] + v[len(v) // 2]) / 2)
                clusters.append((max(meds) - min(meds), d0, grp, real, split))
    clusters.sort(reverse=True, key=lambda c: (c[0], c[1]))
    if not clusters:
        W("  no subject was priced by two or more arms on one day.")
    else:
        W(f"  {len(clusters)} subject(s) priced by two or more arms on one day.")
        W("")
        nsplit = sum(1 for c in clusters if c[4])
        if nsplit:
            W(f"  {nsplit} of them also carry a WITHIN-ARM split - one arm pricing")
            W("  the same subject two ways on one day. Marked below; not scored.")
        W("")
        for spread, d0, grp, real, split in clusters[:10]:
            narms = len({arm_of(r) for r in real})
            ps = sorted(float(r["probability"]) for r in real)
            mid = (ps[len(ps) // 2] if len(ps) % 2 else
                   (ps[len(ps) // 2 - 1] + ps[len(ps) // 2]) / 2)
            W(f"  {d0}  spread {spread:g} pts across {narms} arm(s)  median {mid:g}"
              + ("   [WITHIN-ARM SPLIT]" if split else ""))
            W(f"    {real[0]['statement'][:100]}")
            for r in sorted(grp, key=lambda z: -float(z["probability"])):
                tag = arm_of(r)
                ref = "   <- reference, assigned not reasoned" if tag.startswith("control/") else ""
                W(f"      p={float(r['probability']):>5}  {tag:<34} {r.get('id')}{ref}")
            for _sa, vals in sorted(split.items()):
                W(f"      within-arm split: {_sa} priced this "
                  f"{' and '.join('%g' % v for v in vals)} on one day")
            W("")
        W("  A wide spread is not a defect. It is the measurement this desk")
        W("  exists to take: identical packet, identical gate, different")
        W("  forecasters, and the disagreement priced and sealed before any")
        W("  outcome exists. Nobody else is positioned to publish it.")

    # cross-arm: measurement, never a verdict
    W("")
    W("IDENTICAL-CLAIM SPREAD - same threshold, same window")
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

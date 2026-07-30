#!/usr/bin/env python3
"""
ohrwurm_candidates.py — NETZ War Desk · the bridge from signal to sealed call.

    ohrwurm_call.py has existed for some time and has issued exactly zero rows:
    the ledger arm ohrwurm/propagation is empty. The forward channel was built
    and never fired, because firing it requires naming a specific phrase that
    has NOT yet crossed the side boundary and committing to whether it will.
    Nothing produced that shortlist. This does.

WHAT IT DOES

    Reads the velocity tile, takes the phrases still CONFINED to their origin
    side, and ranks them as crossing candidates by what is observable about them
    right now: how many channels inside the origin side carry them, how fast
    they spread within that side, and how much of the pull window is left. Then
    it prints, for each, the exact ohrwurm_call.py invocation — with the
    probability left blank.

WHY IT ASSIGNS NO PROBABILITY

    A ranking is not a calibrated forecast. This tool has never been validated
    against a single resolved crossing, because the arm has no resolved rows —
    so any number it printed would be invention wearing arithmetic. What it can
    honestly supply is the REFERENCE CLASS: in this pull, N of M phrases above
    the floor crossed a side boundary, so the base rate for "a phrase like this
    crosses" is N/M. That is the anchor a forecaster is entitled to start from
    and then adjust. The adjustment is the operator's, and it is the operator's
    Brier score that pays for it.

    The ranking's own validity is the open question the ledger will answer. If
    high-ranked candidates cross no more often than low-ranked ones over thirty
    resolved rows, the heuristic is dead and the record will say so. That is the
    point of issuing the calls rather than admiring the signal.

THE LIMIT THAT RIDES EVERY ROW

    FIRST IN THIS CORPUS IS NOT FIRST IN THE WORLD, and a crossing is a
    crossing of the watched channel set, not of reality. A phrase may already
    be on both sides of a boundary in channels nobody here reads. Base rates
    computed inside one pull describe that pull.

USE
    python ohrwurm_candidates.py                     top candidates, base rate
    python ohrwurm_candidates.py --top 5 --window-days 14
    python ohrwurm_candidates.py --min-channels 2    tighten the floor
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DOCS = HERE / "docs"
FORECASTS = HERE / "forecasts"


def load_tile(explicit=None):
    for p in ([Path(explicit)] if explicit else
              [DOCS / "ohrwurm_velocity.json",
               FORECASTS / "ohrwurm_velocity_latest.json"]):
        if p.exists():
            return json.loads(p.read_text(encoding="utf-8")), p
    return None, None


KNOWN_GAP = """  KNOWN GAP, MEASURED THIS SESSION AND NOT SOLVED: ohrwurm's per-language
  stoplists are partial. They carry 44 Cyrillic entries but miss "при", "этом",
  "том", "числе" — so on a Russian-heavy pull, function-word n-grams outrank
  content. A document-frequency guard now flags the worst of them
  (function_shaped), and on the 07-30 pull it correctly catches "при этом" at
  3.1% of messages but MISSES "том числе" and "поле боя" at 1.5%, because at
  478 messages the frequency signal is too thin to separate a function phrase
  from a genuinely uncommon one. The threshold was left at 2% rather than tuned
  downward until the output looked right. The real fix is completing the
  stoplists from a verified word-frequency list per language, which is not done.
  Until it is: flagged rows are listed separately, and a Cyrillic or Arabic
  phrase near the top deserves your eye before it deserves a call."""


def rank(rows, min_channels):
    """Order confined phrases by observable spread strength inside their side.

    No weighting is tuned, because tuning implies validation data that does not
    exist. The three inputs are summed after a plain 0-1 normalisation and the
    composite is reported alongside its parts, so a reader can see exactly what
    drove a rank and disagree with it.
    """
    cands = [r for r in rows
             if r.get("confined") and r.get("channels", 0) >= min_channels
             and not r.get("function_shaped")]
    if not cands:
        return []
    def norm(vals):
        lo, hi = min(vals), max(vals)
        span = hi - lo
        return [(v - lo) / span if span else 0.5 for v in vals]

    chans = norm([r["channels"] for r in cands])
    vels = norm([r.get("velocity_chan_per_hr") or 0 for r in cands])
    reps = norm([r["reports"] for r in cands])
    for r, c, v, p in zip(cands, chans, vels, reps):
        r["_rank_parts"] = {"channels": round(c, 3),
                            "velocity": round(v, 3),
                            "reports": round(p, 3)}
        r["_score"] = round(c + v + p, 3)
    cands.sort(key=lambda r: -r["_score"])
    return cands


def main():
    ap = argparse.ArgumentParser(description="Ohrwurm crossing-call candidates")
    ap.add_argument("--tile")
    ap.add_argument("--top", type=int, default=8)
    ap.add_argument("--window-days", type=int, default=21)
    ap.add_argument("--min-channels", type=int, default=2)
    a = ap.parse_args()

    tile, path = load_tile(a.tile)
    if not tile:
        print("No velocity tile. Run: python ohrwurm_velocity.py --latest",
              file=sys.stderr)
        return 1
    rows = tile.get("phrases", [])
    summ = tile.get("summary", {})
    print(f"tile: {path.name} · pull {tile.get('source_pull')}", file=sys.stderr)

    total = summ.get("phrases_total") or len(rows)
    crossed = summ.get("crossed_side") or 0
    base = crossed / total if total else 0

    print("")
    print("REFERENCE CLASS — the anchor, not a forecast")
    print("-" * 62)
    print(f"  In this pull, {crossed} of {total} phrases above the floor "
          f"crossed a side boundary.")
    print(f"  Base rate for 'a phrase like this crosses': "
          f"{base*100:.1f}%")
    print(f"  Median cross latency among those that did: "
          f"{summ.get('median_cross_latency_hrs')}h")
    print("  This describes THIS pull and this watched channel set. It is the")
    print("  number a forecaster starts from and then adjusts on the specifics.")

    flagged = [r for r in rows
               if r.get("confined") and r.get("function_shaped")
               and r.get("channels", 0) >= a.min_channels]
    cands = rank(rows, a.min_channels)
    if not cands:
        print("\nNo confined phrase meets the channel floor — nothing to call.")
        return 0

    print("")
    print(f"CANDIDATES — confined phrases, ranked by observable spread "
          f"({len(cands)} eligible)")
    print("-" * 62)
    print(KNOWN_GAP)
    print("")
    print("  Rank is a heuristic with ZERO validation: the propagation arm has")
    print("  no resolved rows, so nothing here has ever been scored. Whether")
    print("  this ordering predicts anything is the question the ledger will")
    print("  settle, which is why the calls get issued instead of admired.")
    print("")
    for i, r in enumerate(cands[:a.top], 1):
        side = r["origin"]["side"]
        parts = r["_rank_parts"]
        print(f"  {i}. [{r['phrase']}]")
        print(f"     {r['zone']} · origin {side} via {r['origin']['channel']} "
              f"· {r['channels']} channels · {r['reports']} reports "
              f"· {r['span_hours']}h span")
        print(f"     velocity {r.get('velocity_chan_per_hr')} ch/hr · "
              f"composite {r['_score']} "
              f"(ch {parts['channels']} + vel {parts['velocity']} + "
              f"rep {parts['reports']})")
        share = r.get("rarest_token_msg_share")
        print(f"     sides carrying it: "
              + ", ".join(f"{k} {v}" for k, v in r["side_balance"].items()
                          if k != "?")
              + (f" · rarest token in {share*100:.1f}% of messages"
                 if share is not None else ""))
        print("")

    if flagged:
        print(f"WITHHELD — {len(flagged)} confined phrase(s) flagged "
              f"function-shaped")
        print("-" * 62)
        print("  Common-token phrases the stoplist should have caught. Not")
        print("  ranked, not suggested; printed so the filter's work is "
              "visible.")
        for r in flagged[:8]:
            sh = r.get("rarest_token_msg_share")
            print(f"    [{r['phrase']}] — rarest token in "
                  f"{sh*100:.1f}% of messages" if sh is not None
                  else f"    [{r['phrase']}]")
        print("")

    print("")
    print("TO ISSUE — fill in your own probability and rationale")
    print("-" * 62)
    print("  Every side this phrase has NOT reached is a separate callable")
    print("  proposition. Pick the boundary you actually have a view on.")
    print("")
    seen_sides = set()
    for r in rows:
        for s in (r.get("side_balance") or {}):
            if s and s != "?":
                seen_sides.add(s)
    for r in cands[:a.top]:
        origin = r["origin"]["side"]
        held = {s for s in (r.get("side_balance") or {}) if s and s != "?"}
        targets = sorted(seen_sides - held)
        if not targets:
            continue
        tgt = targets[0]
        print(f'  python ohrwurm_call.py --phrase "{r["phrase"]}" \\')
        print(f'      --from-side {origin} --to-side {tgt} '
              f'--window-days {a.window_days} \\')
        print(f'      --probability <YOUR NUMBER> --keyless \\')
        print(f'      --rationale "<why this crosses, or why it does not>"')
        if len(targets) > 1:
            print(f'      # other unreached sides: {", ".join(targets[1:])}')
        print("")

    print("  --keyless is the honest default for a language call: the corpus")
    print("  register is its grounding, not a deduction from prior reporting.")
    print("  Under thirty resolved rows the arm's Brier is noise, and the")
    print("  conformance page will say so next to the number.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

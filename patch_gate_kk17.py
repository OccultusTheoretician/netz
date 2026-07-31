#!/usr/bin/env python3
"""patch_gate_kk17.py — F1, the specificity gate. Report-only; --apply writes.

Four rejection classes the voids and misses wrote, now mechanical:
  1. VENUE MULTIPLICITY — "the Guardian or BBC" resolutions leave the
     adjudicator choosing the venue after the fact. One source of record,
     or a defined venue class, named at issuance.
  2. SOURCELESS RESOLUTION — a stranger must know where to look. The
     criterion must name a source: a proper noun, a domain, or a
     source-of-record phrase.
  3. NUMBERLESS MEASUREMENT — a row about a price, yield, rate, count or
     magnitude with no digit anywhere is an opinion wearing a row's clothes.
  4. NAKED CONDITIONAL — "if X, then Y" with no void clause pre-registers
     nothing about the antecedent failing; the 95% Yes/No void was this
     class in disguise.
Forward-only: the gate runs at issuance; sealed history is untouched.
"""
import argparse
from pathlib import Path

OLD = b'''    if not (5 <= p["probability"] <= 95):'''
NEW = b'''    res = p.get("resolution", "")
    if re.search(r"\\b[A-Z][\\w.&-]{1,}\\s+or\\s+(?:the\\s+)?[A-Z]", res):
        reasons.append("resolution names alternative venues joined by 'or' \\u2014 "
                       "name ONE source of record or define the venue class; "
                       "an adjudicator must not choose the venue after the fact")
    _src_hint = re.search(r"\\b(?:per|according to|as (?:published|posted|listed|"
                          r"reported|recorded)|official|website|page|feed|register|"
                          r"filing|bulletin|dataset|catalog|api)\\b", res, re.I)
    _src_noun = re.search(r"\\S\\s+[A-Z][A-Za-z]{2,}", res)
    _src_dom = re.search(r"\\b[\\w-]+\\.(?:gov|org|com|net|int|mil|eu)\\b", res, re.I)
    if not (_src_hint or _src_noun or _src_dom):
        reasons.append("resolution names no source of record \\u2014 a stranger "
                       "must know exactly where to look on the deadline date")
    if re.search(r"\\b(?:price|yield|rate|index|level|magnitude|count|total|"
                 r"threshold|close[sd]?|above|below|exceed)\\b", both, re.I) \\
            and not re.search(r"(?:above|below|exceed\\w*|at least|at or|over|"
                              r"under|reach\\w*|close[sd]?|threshold|magnitude|"
                              r"least)\\D{0,12}[\\$\\u20ac]?\\d", both, re.I):
        reasons.append("measurable claim without a numeric threshold \\u2014 "
                       "a row about a quantity must state the number next to its comparator; identifier digits (H.15, S&P 500) do not count")
    if re.search(r"^\\s*if\\b|\\bonly if\\b|\\bprovided that\\b|\\bin the event\\b",
                 p["statement"], re.I) and "void" not in res.lower():
        reasons.append("conditional trigger without a void clause \\u2014 "
                       "pre-register what happens when the antecedent fails")
    if not (5 <= p["probability"] <= 95):'''
MARK = b"an adjudicator must not choose the venue"


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()
    p = Path("kkr.py"); b = p.read_bytes()
    if MARK in b:
        print("OK    kkr.py \u2014 gate already hardened"); return
    if OLD not in b:
        print("MISS  kkr.py \u2014 anchor not found"); return
    if a.apply:
        p.write_bytes(b.replace(OLD, NEW, 1))
        print("FIX   kkr.py \u2014 four specificity rejections live: venue multiplicity, "
              "sourceless resolution, numberless measurement, naked conditional")
    else:
        print("WOULD kkr.py \u2014 rerun with --apply")


if __name__ == "__main__":
    main()

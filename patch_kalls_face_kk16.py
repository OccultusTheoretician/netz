#!/usr/bin/env python3
"""patch_kalls_face_kk16.py — report-only by default, --apply writes.

One sentence on the Kalls page claims the first-clutch hashes bind probability
and deadline. All ten live Kalls are knp-1; the hashlog's own disclosure block
prints that those two fields are NOT bound and are carried by the anchored
history alone. The page face contradicted the record it fronts — the exact
defect class the desk's own Revision 3 finding names. The lede now states the
knp-1 construction, prints the defect and the revision that repaired it going
forward, and keeps the reveal mechanics unchanged. The markdown twin was
always honest and is untouched.
"""
import argparse
from pathlib import Path

OLD = (b'  <p class="lede">Nine eggs, laid in one session. Every hash below was computed over the full\n'
       b'    call \xe2\x80\x94 statement, resolution basis, probability, deadline, and a secret salt \xe2\x80\x94 <strong>before any\n'
       b'    outcome existed</strong>. The hash reveals nothing about the content.')
NEW = (b'  <p class="lede">Nine eggs, laid in one session, each hash computed <strong>before any outcome\n'
       b'    existed</strong> over the statement, its resolution basis, and a secret salt (construction\n'
       b'    <span translate="no">knp-1</span>). The probability and deadline shown are <em>not</em> bound by these\n'
       b'    hashes \xe2\x80\x94 they are carried by the append-only anchored history, a defect this desk found in its\n'
       b'    own construction and printed as Revision 3; Kalls sealed after that revision bind them\n'
       b'    (<span translate="no">knp-2</span>). The hash reveals nothing about the content.')
MARK = b'a defect this desk found in its'


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()
    p = Path("docs/kraehes_kalls.html")
    b = p.read_bytes()
    if MARK in b:
        print("OK    kraehes_kalls.html \u2014 already applied"); return
    if OLD not in b:
        print("MISS  kraehes_kalls.html \u2014 target not found"); return
    if a.apply:
        p.write_bytes(b.replace(OLD, NEW, 1))
        print("FIX   kraehes_kalls.html \u2014 lede now states knp-1, prints the defect and Revision 3")
    else:
        print("WOULD kraehes_kalls.html \u2014 rerun with --apply")


if __name__ == "__main__":
    main()

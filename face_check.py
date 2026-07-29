#!/usr/bin/env python3
"""
face_check.py - do two published faces ever state different numbers?

THE QUESTION THIS ANSWERS

site_audit.py checks that the site is well-formed: links resolve, references
match disk case, nothing phones home, every page previews. All of that passed.

None of it checks whether the site is CONSISTENT. A page can be perfectly
well-formed and state that the ledger holds 77 projections while the ledger
holds 161. That is the failure a reader arriving from an argument about
verifiability will find first, because it is the exact failure that argument
says a standard should prevent.

There is precedent on this desk. For several days the forecasts face printed
`lmstudio/auto` at 13 resolved, Brier 0.221, skill -0.038 while the ledger face
printed 15, 0.231, -0.179 - both served, both current-looking, differing
because one was a per-run issue page frozen at generation and nothing on it
said so. The mirror invariant in desk.py could not see it: mirrors prove the
served copy matches the canonical copy, never that either agrees with the data.

HOW IT WORKS

ledger.json is canonical. Everything else is a rendering of it. This script
recomputes the figures from the ledger, then scans every served page for
numbers that claim to be those figures, and reports any that disagree.

WHAT IT CANNOT DO

It matches patterns, so it finds figures stated in the phrasings it knows. A
figure phrased a way this script does not recognise is not checked, and the
script prints how many it recognised so that the coverage is visible rather
than assumed. It is a floor, not a proof.

It also flags markdown that reached HTML unconverted - a literal ### or a raw
table pipe in rendered output - because on a page arguing nothing is hand-typed,
visible template leakage is the wrong impression to make.

    python face_check.py
    python face_check.py --verbose

Run from C:\\netz. Standard library only. Writes nothing. ASCII-only output.
"""

import argparse
import json
import re
import sys
from pathlib import Path

DOCS = Path("docs")
LEDGER = Path("ledger.json")


def load_canonical():
    """Recompute every published figure from the ledger itself."""
    d = json.loads(LEDGER.read_text(encoding="utf-8"))
    rows = d.get("projections") or d.get("entries") or []
    arms = {}
    for r in rows:
        a = r.get("model") or r.get("arm") or "unattributed"
        s = arms.setdefault(a, {"issued": 0, "open": 0, "void": 0,
                                "hit": 0, "miss": 0})
        s["issued"] += 1
        st = (r.get("status") or "").lower()
        if st in ("open", "sealed"):
            s["open"] += 1
        elif st == "void":
            s["void"] += 1
        elif st == "hit":
            s["hit"] += 1
        elif st == "miss":
            s["miss"] += 1
    for a, s in arms.items():
        s["resolved"] = s["hit"] + s["miss"]
        if s["resolved"]:
            tot = 0.0
            for r in rows:
                if (r.get("model") or r.get("arm")) != a:
                    continue
                st = (r.get("status") or "").lower()
                if st in ("hit", "miss"):
                    p = float(r.get("probability", 0)) / 100.0
                    tot += (p - (1.0 if st == "hit" else 0.0)) ** 2
            s["brier"] = round(tot / s["resolved"], 4)
        else:
            s["brier"] = None
    return {
        "as_of": d.get("as_of", "?"),
        "schema": d.get("schema", "?"),
        "total": len(rows),
        "arms": arms,
        "n_arms": len(arms),
        "open": sum(s["open"] for s in arms.values()),
        "void": sum(s["void"] for s in arms.values()),
        "resolved": sum(s["resolved"] for s in arms.values()),
    }


# Each check: label, regex over page text, and a function giving the expected
# value. Group 1 of the regex is the stated figure.
def build_checks(c):
    return [
        ("total issued",
         re.compile(r"(\d[\d,]*)\s+issued\b", re.I),
         c["total"]),
        ("forecaster arms",
         re.compile(r"(?:across\s+)?(\d+)\s+forecaster\s+arms?\b", re.I),
         c["n_arms"]),
        ("open count",
         re.compile(r"(\d[\d,]*)\s+open\b(?!\s*sources)", re.I),
         c["open"]),
        # ANCHORED. The previous form matched the day component of dates
        # inside per-row text like "(70%, due 2026-07-25, voided 2026-07-20)"
        # and produced ten false findings from one bad pattern. The count is
        # only ever stated as "N of M issued ... voided" or "N projection(s)
        # voided", so require that shape.
        ("voided count",
         # [^.] cannot cross the period in "(6.2%)", which made an earlier
         # version of this pattern match nothing at all - a silent no-op,
         # worse than the false positives it replaced. Bound by distance,
         # not by character class.
         re.compile(r"(\d[\d,]*)\s+(?:of\s+\d[\d,]*\s+issued|projections?)"
                    r".{0,30}?voided", re.I),
         c["void"]),
        ("resolved against the thirty floor",
         re.compile(r"\b(\d+)\s*/\s*30\b"),
         c["resolved"]),
        ("fifty-entry gate figure",
         re.compile(r"MET\s*\((\d[\d,]*)\)", re.I),
         c["total"]),
    ]


MD_LEAKS = [
    ("literal markdown heading", re.compile(r">\s*#{2,6}\s+\w")),
    ("literal bold markers", re.compile(r">[^<]*\*\*[^<]*\*\*")),
    ("raw table separator", re.compile(r">\s*\|[\s\-:|]{5,}\|")),
]


def tracked_docs():
    """Filenames git actually serves from docs/, top level only."""
    import subprocess
    try:
        r = subprocess.run(["git", "ls-files", "docs/"], capture_output=True,
                           text=True, check=False, errors="replace")
        out = r.stdout if r.returncode == 0 else ""
    except Exception:
        out = ""
    return {l.split("/")[-1] for l in out.splitlines()
            if l.count("/") == 1 and l.lower().endswith((".html", ".md"))}


def text_of(html):
    t = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", html)
    t = re.sub(r"(?s)<[^>]+>", " ", t)
    return re.sub(r"\s+", " ", t)


def main():
    ap = argparse.ArgumentParser(description="cross-face consistency audit")
    ap.add_argument("--verbose", action="store_true")
    a = ap.parse_args()

    if not LEDGER.exists():
        print("FAIL - ledger.json not found. Run from C:\\netz.", file=sys.stderr)
        return 1
    if not DOCS.is_dir():
        print("FAIL - docs/ not found. Run from C:\\netz.", file=sys.stderr)
        return 1

    c = load_canonical()
    checks = build_checks(c)

    print("")
    print("FACE CONSISTENCY AUDIT")
    print("=" * 72)
    print("  ledger.json is canonical. Everything else renders it.")
    print("")
    print("  CANONICAL FIGURES, recomputed from the ledger")
    print("  " + "-" * 68)
    print("    schema %s . as_of %s" % (c["schema"], c["as_of"]))
    print("    %d issued . %d arms . %d open . %d void . %d resolved"
          % (c["total"], c["n_arms"], c["open"], c["void"], c["resolved"]))
    print("")
    for name in sorted(c["arms"]):
        s = c["arms"][name]
        b = "%.4f" % s["brier"] if s["brier"] is not None else "not computed"
        print("    %-16s iss %3d  open %3d  void %2d  res %2d  H/M %d/%d  Brier %s"
              % (name, s["issued"], s["open"], s["void"], s["resolved"],
                 s["hit"], s["miss"], b))

    served = tracked_docs()
    # docs/ on disk holds untracked scratch files. Pages serves the repo, so an
    # untracked page is not published and is not a finding. warroom.html is the
    # live example - gitignored, on disk, and reported by an earlier version.
    pages = sorted(p for p in list(DOCS.glob("*.html")) + list(DOCS.glob("*.md"))
                   if p.name in served)
    findings = []
    snapshots = []
    n_figs = 0

    print("")
    print("  STATED FIGURES vs CANONICAL")
    print("  " + "-" * 68)
    for p in pages:
        raw = p.read_text(encoding="utf-8", errors="replace")
        txt = text_of(raw) if p.suffix == ".html" else raw
        # A document carrying its own generated-on line is a snapshot. Its
        # figures were true when written and are not a live claim.
        dated = re.search(r"[*_]?Generated\s+(\d{4}-\d{2}-\d{2})", raw)
        if dated:
            snapshots.append((p.name, dated.group(1)))
            continue
        for label, pat, expect in checks:
            for m in pat.finditer(txt):
                # A sentence scoped to one arm states THAT arm's figures.
                # "This arm - manual/opus-5: 30 issued . 30 open" is correct
                # and is not a claim about the ledger total.
                lead = txt[max(0, m.start() - 120):m.start()]
                if re.search(r"(?:this arm|arm\s*[-\u2014:]|`[a-z]+/[a-z0-9\-]+`)",
                             lead, re.I):
                    continue
                n_figs += 1
                try:
                    got = int(m.group(1).replace(",", ""))
                except ValueError:
                    continue
                if got != expect:
                    ctx = txt[max(0, m.start() - 50):m.end() + 30]
                    findings.append((p.name, label, got, expect, ctx.strip()))
                elif a.verbose:
                    print("    ok      %-26s %-24s %d" % (p.name, label, got))

    if findings:
        for name, label, got, expect, ctx in findings:
            print("    STALE   %s" % name)
            print("            %s: page says %d, ledger says %d"
                  % (label, got, expect))
            print("            ...%s..." % ctx[:96])
    else:
        print("    ok      every recognised figure matches the ledger")
    print("")
    print("    %d figure(s) recognised and checked across %d served page(s)"
          % (n_figs, len(pages)))
    for name, when in snapshots:
        print("    snapshot %s carries 'Generated %s' - figures not checked"
              % (name, when))
    if snapshots:
        print("    A dated snapshot states what was true when written. Whether")
        print("    it should still be served is a cadence question, not an error.")
    print("    Figures phrased in a way this script does not recognise are")
    print("    NOT checked. This is a floor, not a proof.")

    print("")
    print("  TEMPLATE LEAKAGE")
    print("  " + "-" * 68)
    leaks = []
    for p in sorted(DOCS.glob("*.html")):
        raw = p.read_text(encoding="utf-8", errors="replace")
        for label, pat in MD_LEAKS:
            for m in pat.finditer(raw):
                frag = re.sub(r"\s+", " ", m.group(0))[:70]
                leaks.append((p.name, label, frag))
    if leaks:
        seen = set()
        for name, label, frag in leaks:
            k = (name, label)
            if k in seen:
                continue
            seen.add(k)
            n = sum(1 for x in leaks if (x[0], x[1]) == k)
            print("    LEAK    %-24s %s (x%d)" % (name, label, n))
            print("            %s" % frag)
        print("")
        print("    Unconverted markdown in rendered output is a small defect")
        print("    with an outsized cost on a page whose dek says nothing here")
        print("    is hand-typed.")
    else:
        print("    ok      no unconverted markdown in any served page")

    print("")
    print("=" * 72)
    print("  %d stale figure(s), %d page(s) with template leakage"
          % (len(findings), len({l[0] for l in leaks})))
    print("")
    return 0


if __name__ == "__main__":
    sys.exit(main())

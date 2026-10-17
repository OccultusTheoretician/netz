#!/usr/bin/env python3
"""ident_rows.py - IDROWS-1017: identifiers a forecaster arm put in a sealed row.

ident_audit.py tests identifiers in a report's synthesis prose and only then
looks for them in the ledger, so an identifier an arm mints in its own row and
that never appears in any prose is invisible to it. Found 2026-10-16:
KKR-20261016-64 names CVE-2026-99999; the packet the arm read carries no such
token (0 lines), and the row is a near-certain NO at 7 percent - a free Brier.

This reads the ledger directly. For every row it takes the identifiers in the
statement, resolution and failure condition, and tests each against what the
arm read: the row's source_packet when --packets is given (the box), else the
row's source_report (any clone; a weaker test, printed as such). Report-only:
it never touches the ledger. A sealed row is never edited; findings print.
"""
import argparse, json, re, sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
FAMILIES = [
    ("CVE", re.compile(r"\bCVE-\d{4}-\d+\b", re.I)),
    ("GHSA", re.compile(r"\bGHSA-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}\b", re.I)),
    ("USGS", re.compile(r"\b(?:us|ci|nc|nn|hv|ak|uw|mb|se|pr|uu|ok|tx|at)(?=[0-9a-z]*\d)[0-9a-z]{6,12}\b")),
]

def tokens(text):
    out = []
    for fam, rx in FAMILIES:
        for t in dict.fromkeys(rx.findall(text or "")):
            out.append((fam, t))
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ledger", default=str(HERE / "ledger.json"))
    ap.add_argument("--reports", default=str(HERE / "reports"))
    ap.add_argument("--packets", default=None, help="dir holding kkr_packet_*.md (the box)")
    ap.add_argument("--since", default="2026-07-01")
    ap.add_argument("--report", default=None, help="write markdown here")
    a = ap.parse_args()
    rows = json.loads(Path(a.ledger).read_text(encoding="utf-8"))["projections"]
    cache, findings, checked, missing_src = {}, [], 0, Counter()
    def text_of(path):
        if path not in cache:
            cache[path] = path.read_text(encoding="utf-8", errors="replace").lower() if path.exists() else None
        return cache[path]
    for r in rows:
        if str(r.get("date_issued", "")) < a.since:
            continue
        toks = tokens(" ".join(str(r.get(k, "")) for k in ("statement", "resolution", "failure_condition")))
        if not toks:
            continue
        src, basis = None, None
        if a.packets and r.get("source_packet"):
            src, basis = text_of(Path(a.packets) / r["source_packet"]), "packet"
        if src is None and r.get("source_report"):
            src, basis = text_of(Path(a.reports) / r["source_report"]), "report"
        if src is None:
            missing_src[r.get("model")] += 1
            continue
        for fam, t in toks:
            checked += 1
            if t.lower() not in src:
                findings.append({"id": r.get("id"), "arm": r.get("model"), "family": fam, "token": t,
                                 "basis": basis, "p": r.get("probability"), "status": r.get("status"),
                                 "control": bool(r.get("is_control"))})
    L = ["# ROW IDENTIFIERS - what the arm wrote vs what it read (IDROWS-1017)", ""]
    L.append(f"Rows since {a.since}; identifier tokens checked: {checked}; not found in the source: {len(findings)}; rows with no readable source: {sum(missing_src.values())}.")
    L.append("")
    if not a.packets:
        L.append("Basis is the published report, not the packet the arm read (packets are gitignored). A finding here means 'not in the report'; rerun with --packets on the box for the real test.")
        L.append("")
    L.append("| row | arm | token | basis | p | status |")
    L.append("|---|---|---|---|---|---|")
    for f in sorted(findings, key=lambda x: x["id"] or ""):
        if f["control"]:
            continue
        L.append(f"| {f['id']} | {f['arm']} | {f['token']} | {f['basis']} | {f['p']} | {f['status']} |")
    ctl = sum(1 for f in findings if f["control"])
    L.append("")
    L.append(f"Control rows carrying the same tokens (copied from their arm, not minted): {ctl}.")
    by_arm = Counter(f["arm"] for f in findings if not f["control"])
    if by_arm:
        L.append("")
        L.append("By arm: " + ", ".join(f"{k} {v}" for k, v in by_arm.most_common()))
    txt = "\n".join(L) + "\n"
    print(txt)
    if a.report:
        Path(a.report).write_text(txt, encoding="ascii", errors="replace")
        print("written:", a.report)

if __name__ == "__main__":
    main()

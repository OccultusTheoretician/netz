#!/usr/bin/env python3
"""
ident_audit.py — IDENTIFIER GROUNDEDNESS AUDIT

WHY

    Resolving KKR-20260721-07 on 2026-08-04 turned up a defect one level
    upstream of the citation problem. The row's resolution basis turned on
    "CVE-2026-6". That identifier is malformed — a CVE sequence field is four
    digits minimum — and it does not appear in the item the row cited, whose
    headline carries no CVE at all. It appears only in the battle report's
    machine-drafted synthesis paragraph, beside three well-formed identifiers.

    So the desk's own report generator produced an identifier that refers to
    nothing, printed it in the record its forecaster arms read as priors, and
    an arm lifted it into a sealed row as that row's operative term. The real
    vulnerability was CVE-2026-6875.

    This is the citation defect's harder sibling. A bad citation points at a
    real item that fails to support the claim — checkable, and now gated. A
    fabricated identifier points at nothing at all, and reads as MORE precise
    than the prose around it, which is exactly why nobody checks it.

WHAT IT CHECKS

    For every report, identifier-shaped tokens are extracted from SYNTHESIS
    prose (the machine-drafted paragraphs) and tested twice:

      MALFORMED   the token cannot be a valid identifier of its kind.
                  CVE requires CVE-YYYY-NNNN with four or more digits.
      UNSOURCED   the token is well-formed but appears nowhere in the
                  numbered record the synthesis is summarising. This is NOT a
                  claim that the token is invented. The report's record lines
                  carry title, sources, time and link; the PACKET the arm
                  reads carries `rep['summary'][:250]` as well. An identifier
                  living in a summary is visible to the forecaster and absent
                  from the published record.

                  Which means UNSOURCED cannot be adjudicated from the
                  repository, because `forecasts/kkr_packet_*.md` is in
                  .gitignore. Pass --packets on a machine that has them.

    Then every finding is cross-checked against the ledger: did this token
    reach a SEALED ROW? That is the difference between a cosmetic defect and
    one carried on the permanent record.

USE
    python ident_audit.py                      audit all reports
    python ident_audit.py --report OUT.md      write the report
    python ident_audit.py --json OUT.json      machine verdicts
    python ident_audit.py --file NAME.md       one report only
"""

import argparse
import json
import re
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent

# Identifier families the desk's sources actually carry. Each entry is
# (name, finder, validator). The finder is deliberately loose so malformed
# tokens are CAUGHT rather than skipped — a strict pattern would silently
# ignore exactly the defect this exists to find.
FAMILIES = [
    ("CVE", re.compile(r"\bCVE-\d{4}-\d+\b"),
     re.compile(r"^CVE-\d{4}-\d{4,}$")),
    ("CWE", re.compile(r"\bCWE-\d+\b"), re.compile(r"^CWE-\d{1,4}$")),
    ("GHSA", re.compile(r"\bGHSA-[0-9a-z-]+\b", re.I),
     re.compile(r"^GHSA-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}$", re.I)),
]

ITEM_RE = re.compile(r"\s*(\d+)\.\s+(.*)")


def split_report(path: Path):
    """Numbered record lines vs everything else. The 'everything else' is the
    synthesis prose plus headers; identifiers in the record are sourced by
    definition, identifiers only in the prose are not."""
    record, prose = [], []
    try:
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    except Exception as _e:
        # KK31-INDETERMINATE: empty record + empty prose means no identifier
        # can be flagged, so the report scored clean by construction.
        print(f"  INDETERMINATE - ident_audit could not read {path}: {_e}. "
              f"This report is UNSCANNED, not clean.", file=sys.stderr)
        return "", ""
    for line in lines:
        (record if ITEM_RE.match(line) else prose).append(line)
    return "\n".join(record), "\n".join(prose)


def audit_report(path: Path, pkt_dir=None):
    record, prose = split_report(path)
    if not prose:
        return []
    # The packet is the artifact the arm actually read. It is gitignored, so
    # this is empty on any clone and populated only where the desk runs.
    pkt_text = ""
    if pkt_dir:
        stem = path.name.replace("battle_report_", "kkr_packet_")
        pk = Path(pkt_dir) / stem
        if pk.exists():
            pkt_text = pk.read_text(encoding="utf-8", errors="replace")
    out = []
    for name, finder, valid in FAMILIES:
        in_record = set(finder.findall(record))
        pkt_toks = set(finder.findall(pkt_text)) if pkt_text else set()
        for tok in dict.fromkeys(finder.findall(prose)):
            if not valid.match(tok):
                kind = "MALFORMED"
            elif tok not in in_record and tok not in pkt_toks:
                kind = "UNSOURCED"
            else:
                continue
            out.append({"report": path.name, "family": name,
                        "token": tok, "finding": kind})
    return out


def main():
    ap = argparse.ArgumentParser(description="identifier groundedness audit")
    ap.add_argument("--reports", default=str(HERE / "reports"))
    ap.add_argument("--ledger", default=str(HERE / "ledger.json"))
    ap.add_argument("--file", help="audit one report")
    ap.add_argument("--packets", default=None,
                    help="directory holding kkr_packet_*.md. These are "
                         "gitignored, so UNSOURCED is unadjudicable without "
                         "them and the report says so.")
    ap.add_argument("--report", help="write markdown here")
    ap.add_argument("--json", dest="jsonout")
    a = ap.parse_args()

    rdir = Path(a.reports)
    files = ([rdir / a.file] if a.file
             else sorted(rdir.glob("battle_report_*.md")))
    files = [f for f in files if f.exists()]
    if not files:
        sys.exit(f"no reports under {rdir}")

    findings = []
    for f in files:
        findings.extend(audit_report(f, a.packets))

    # Which findings reached a sealed row?
    rows = []
    lp = Path(a.ledger)
    if lp.exists():
        rows = json.loads(lp.read_text(encoding="utf-8"))["projections"]
    by_tok = defaultdict(list)
    for fd in findings:
        by_tok[fd["token"]].append(fd)
    sealed = []
    for tok, fds in by_tok.items():
        pat = re.compile(r"\b" + re.escape(tok) + r"\b")
        for p in rows:
            blob = f"{p.get('statement','')} {p.get('resolution','')} " \
                   f"{p.get('failure_condition','')}"
            if pat.search(blob):
                sealed.append({"token": tok, "finding": fds[0]["finding"],
                               "id": p.get("id"), "arm": p.get("model"),
                               "status": p.get("status"),
                               "keyed_keyless": p.get("keyed_keyless"),
                               "reports": sorted({x["report"] for x in fds})})

    L = []
    w = L.append
    w("# IDENTIFIER GROUNDEDNESS AUDIT")
    w("")
    w(f"Generated {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')} · "
      f"{len(files)} report(s)")
    w("")
    w("Identifiers appearing in machine-drafted synthesis prose are tested for "
      "format validity and for presence in the numbered record the synthesis "
      "summarises. An identifier the synthesis introduces on its own is "
      "unsourced by construction, and reads as more precise than the prose "
      "around it — which is why it goes unchecked.")
    w("")
    w("## Result")
    w("")
    w(f"- reports audited: **{len(files)}**")
    w(f"- findings: **{len(findings)}**")
    if not a.packets:
        w("> **Scope limitation.** `--packets` was not supplied, so UNSOURCED "
          "findings were tested against the published report only. The packet "
          "the forecaster arm actually read is excluded from the repository by "
          "`.gitignore` (`forecasts/kkr_packet_*.md`), and it carries article "
          "summaries the report's record lines omit. An UNSOURCED finding here "
          "means *not present in the published record* — it is not a claim "
          "that the identifier is invented. MALFORMED findings stand "
          "regardless of provenance.")
        w("")
    for k in ("MALFORMED", "UNSOURCED"):
        n = sum(1 for f in findings if f["finding"] == k)
        w(f"  - {k}: {n}")
    w(f"- distinct tokens: **{len(by_tok)}**")
    w("")
    w("## Reached a sealed row")
    w("")
    if sealed:
        w(f"**{len(sealed)}** sealed row(s) carry an identifier this audit "
          f"flags. A sealed row is never edited; these are printed as findings.")
        w("")
        w("| row | token | finding | arm | status | k/kl |")
        w("|---|---|---|---|---|---|")
        for s in sealed:
            w(f"| `{s['id']}` | `{s['token']}` | {s['finding']} | {s['arm']} | "
              f"{s['status']} | {s['keyed_keyless'] or '—'} |")
    else:
        w("None.")
    w("")
    if findings:
        w("## Every finding")
        w("")
        w("| report | token | finding |")
        w("|---|---|---|")
        for f in findings:
            w(f"| {f['report']} | `{f['token']}` | {f['finding']} |")
        w("")
    md = "\n".join(L)
    print(md)
    if a.report:
        Path(a.report).write_text(md + "\n", encoding="utf-8")
        print(f"\nreport -> {a.report}", file=sys.stderr)
    if a.jsonout:
        Path(a.jsonout).write_text(json.dumps(
            {"schema": "ident-audit/1.0",
             "generated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
             "reports": len(files), "findings": findings,
             "sealed": sealed}, indent=1) + "\n", encoding="utf-8")
        print(f"verdicts -> {a.jsonout}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())

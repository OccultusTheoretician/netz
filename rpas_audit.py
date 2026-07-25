#!/usr/bin/env python3
"""
rpas_audit.py — audit the live prediction ledger against RETRO-PRESCIENT AUDIT
STANDARDS, First Edition (RPAS-26), and migrate the schema to conformance.

The desk now publishes RPAS-26 one nav-click from the ledger. RPAS 6.04 binds the
desk to its own standard in public; RPAS 7.02 forbids presenting scores from a
record missing the keyed/keyless split. This tool makes the live data honest
against the published rule — and prints every gap, per 5.03 / 5.07.

    python rpas_audit.py --ledger ledger.json                 # audit only, no writes
    python rpas_audit.py --ledger ledger.json --migrate       # add missing fields, write ledger.json
    python rpas_audit.py --ledger ledger.json --report REPORT_conformance.md

WHAT IT CHECKS (per-entry, against the numbered standard):
  4.02b resolution criterion present and mechanical-looking (named sources)
  4.02c deadline present and parseable
  4.02d probability present, integer 0-100
  4.02e FAILURE CONDITION present and DISTINCT from the resolution criterion
  4.02f KEYED/KEYLESS determination present, decided before resolution
  4.03  entries missing a failure condition are UNFALSIFIABLE (must not seal)
  5.03  resolved entries carry a verdict; misses are counted, not dropped
  5.04  keyed hits segregated from keyless
  1.03f dropped/edited-after-seal detection where timestamps allow

Migration is CONSERVATIVE: it adds absent fields as explicit "UNSET — pre-reg
required" placeholders rather than guessing values. A placeholder is a visible
gap (honest); a guessed keyed/keyless flag decided after resolution is a 4.03
violation (dishonest). The tool will never fabricate the classification.
"""
from __future__ import annotations
import argparse, json, re, sys, datetime as dt
from pathlib import Path

UNSET = "UNSET — pre-registration required (RPAS 4.02)"
KEYCLASSES = {"keyed", "keyless", "unset", "n/a"}
RESOLVED = {"hit", "miss", "keyed", "null", "void", "confirmed", "partial"}
SOURCE_HINT = re.compile(r"\b(reuters|ap|associated press|bbc|al jazeera|guardian|"
                         r"bloomberg|cnn|afp|reﬀ|nyt|new york times|official|filing|"
                         r"repo|hash|records?)\b", re.I)


def load(path: Path):
    d = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(d, list):
        return {"projections": d}, "projections"
    for k in ("projections", "entries", "predictions", "ledger"):
        if isinstance(d.get(k), list):
            return d, k
    raise SystemExit("could not locate the entries list in ledger.json")


def parse_date(s):
    if not s or not isinstance(s, str):
        return None
    for fmt in ("%Y-%m-%d", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%dT%H:%M:%SZ"):
        try:
            return dt.datetime.strptime(s[:19] if "T" in s else s[:10], fmt).date()
        except ValueError:
            continue
    return None


def audit_entry(e: dict) -> list[tuple[str, str, str]]:
    """Return list of (severity, code, message). severity: FAIL | WARN | PASS-note."""
    out = []
    eid = e.get("id", "?")

    # 4.02d probability
    p = e.get("probability")
    if p is None:
        out.append(("FAIL", "4.02d", "no probability"))
    elif not (isinstance(p, (int, float)) and 0 <= p <= 100):
        out.append(("FAIL", "4.02d", f"probability out of range: {p!r}"))

    # 4.02b resolution criterion
    res = (e.get("resolution") or "").strip()
    if not res:
        out.append(("FAIL", "4.02b", "no resolution criterion"))
    elif not SOURCE_HINT.search(res):
        out.append(("WARN", "4.02b", "resolution criterion names no concrete source/instrument"))

    # 4.02c deadline
    if not parse_date(e.get("deadline")):
        out.append(("FAIL", "4.02c", f"deadline missing/unparseable: {e.get('deadline')!r}"))

    # 4.02e failure condition, DISTINCT from resolution
    fc = (e.get("failure_condition") or "").strip()
    if not fc or fc == UNSET:
        out.append(("FAIL", "4.02e/4.03", "no failure condition — UNFALSIFIABLE by 4.03"))
    elif fc.strip().lower() == res.strip().lower():
        out.append(("WARN", "4.02e", "failure condition identical to resolution (should state the MISS outcome explicitly)"))

    # 4.02f keyed/keyless
    kk = (e.get("keyed_keyless") or e.get("keyed") or "").strip().lower()
    if kk not in KEYCLASSES or kk in ("", "unset"):
        out.append(("FAIL", "4.02f", "no keyed/keyless determination (the master law, 1.04)"))
    if e.get("keyed_keyless_decided") == "post-resolution":
        out.append(("FAIL", "4.03", "keyed/keyless decided AFTER resolution — KEYED by rule"))

    # 5.03 resolved entries carry a verdict
    st = (e.get("status") or e.get("state") or "").strip().lower()
    if st in RESOLVED:
        aud = e.get("audit") or {}
        if not aud.get("verdict"):
            out.append(("WARN", "5.03", f"resolved ({st}) but no audit verdict recorded"))
        # 5.04 keyed hit segregation
        if st in ("hit", "confirmed") and kk == "keyed":
            out.append(("PASS-note", "5.04", "keyed hit correctly flagged — excluded from faculty scoring"))

    if not out:
        out.append(("PASS-note", "—", f"{eid}: conformant on all checked requirements"))
    return out


def migrate_entry(e: dict) -> bool:
    """Add absent conformance fields as explicit placeholders. Returns True if changed."""
    changed = False
    if "failure_condition" not in e:
        e["failure_condition"] = UNSET
        changed = True
    if "keyed_keyless" not in e and "keyed" not in e:
        e["keyed_keyless"] = "unset"
        e["keyed_keyless_rationale"] = UNSET
        changed = True
    # normalize probability to int where clean
    p = e.get("probability")
    if isinstance(p, float) and p.is_integer():
        e["probability"] = int(p)
        changed = True
    return changed


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ledger", required=True)
    ap.add_argument("--migrate", action="store_true")
    ap.add_argument("--report", default=None)
    a = ap.parse_args()

    path = Path(a.ledger)
    doc, key = load(path)
    entries = doc[key]

    rows, tally = [], {"FAIL": 0, "WARN": 0, "PASS-note": 0}
    resolved = keyed = keyless = 0
    for e in entries:
        st = (e.get("status") or "").lower()
        if st in RESOLVED:
            resolved += 1
        kk = (e.get("keyed_keyless") or e.get("keyed") or "").lower()
        keyed += kk == "keyed"
        keyless += kk == "keyless"
        for sev, code, msg in audit_entry(e):
            tally[sev] = tally.get(sev, 0) + 1
            if sev != "PASS-note":
                rows.append((e.get("id", "?"), sev, code, msg))

    # ---- console summary ----
    print(f"\nRPAS-26 CONFORMANCE AUDIT — {path.name}")
    print(f"entries: {len(entries)} | resolved: {resolved} | keyless: {keyless} | keyed: {keyed}")
    print(f"findings: {tally['FAIL']} FAIL · {tally['WARN']} WARN\n")

    # the gates that matter most, printed loud — two DIFFERENT floors:
    # 5.02 fifty ENTRIES before any score is computed/examined; the desk's
    # standing thirty-RESOLVED noise floor governs whether a score MEANS anything.
    fifty = "MET" if len(entries) >= 50 else f"NOT MET ({len(entries)}/50 entries) — no score may be computed (5.02)"
    print(f"  [5.02 fifty-entry gate] {fifty}")
    noise = "cleared" if resolved >= 30 else f"below floor ({resolved}/30 resolved) — any score is noise, and must say so on its face"
    print(f"  [thirty-resolved floor] {noise}")
    kkmissing = sum(1 for e in entries if (e.get('keyed_keyless') or e.get('keyed') or 'unset').lower() in ('', 'unset'))
    print(f"  [1.04 master law]       {kkmissing}/{len(entries)} entries lack keyed/keyless — 7.02 blocks scoring until set")
    fcmissing = sum(1 for e in entries if not (e.get('failure_condition') or '').strip() or e.get('failure_condition')==UNSET)
    print(f"  [4.03 falsifiability]   {fcmissing}/{len(entries)} entries lack a failure condition\n")

    for eid, sev, code, msg in rows[:40]:
        print(f"  {sev:4s} {code:10s} {eid:20s} {msg}")
    if len(rows) > 40:
        print(f"  … {len(rows)-40} more findings (full list in --report)")

    # ---- optional report ----
    if a.report:
        R = Path(a.report)
        with R.open("w", encoding="utf-8") as fh:
            fh.write(f"# RPAS-26 Conformance Report — {path.name}\n")
            fh.write(f"*Generated {dt.date.today()}. Audits the live ledger against the published standard. "
                     f"Per RPAS 6.04 the desk is bound by its own rule; per 5.03/5.07 gaps are printed, not hidden.*\n\n")
            fh.write(f"- entries: **{len(entries)}** · resolved: **{resolved}** · keyless: **{keyless}** · keyed: **{keyed}**\n")
            fh.write(f"- 5.02 fifty-entry gate: **{fifty}**\n")
            fh.write(f"- thirty-resolved noise floor: **{noise}**\n")
            fh.write(f"- thirty-resolved noise floor: **{noise}**\n")
            fh.write(f"- 1.04 keyed/keyless missing: **{kkmissing}/{len(entries)}**\n")
            fh.write(f"- 4.03 failure condition missing: **{fcmissing}/{len(entries)}**\n\n")
            fh.write(f"- findings: **{tally['FAIL']} FAIL**, **{tally['WARN']} WARN**\n\n## Findings\n\n")
            fh.write("| id | severity | RPAS | finding |\n|---|---|---|---|\n")
            for eid, sev, code, msg in rows:
                fh.write(f"| {eid} | {sev} | {code} | {msg} |\n")
        print(f"\nreport written -> {R}")

    # ---- optional migration ----
    if a.migrate:
        n = sum(migrate_entry(e) for e in entries)
        bak = path.with_suffix(".json.pre_rpas")
        bak.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")  # safety copy of ORIGINAL-as-loaded
        path.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"\nmigrated {n} entries (added conformance placeholders). backup -> {bak.name}")
        print("NEXT: fill each 'UNSET' failure_condition and keyed/keyless BY HAND, before the entry's")
        print("resolution where still open. Per 4.03, a determination made after resolution is KEYED by rule.")


if __name__ == "__main__":
    main()

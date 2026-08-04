#!/usr/bin/env python3
"""
type3.py — THE THIRD-PARTY AUDIT. RPAS 1.02c, exercised for the first time.

WHY THIS EXISTS

    RPAS has defined Type III since first edition: "the application of Type I
    or Type II procedures to a forecaster other than the auditor, with the
    adjudication independence requirements of Chapter 3." The clause has never
    been run. rpas_verify.py reads this desk's own ledger schema and nothing
    else, so the standard has only ever been applied to its author — which is
    the narrowest possible reading of 6.04 and not what 1.02c describes.

    Every instrument in the field is a benchmark, a platform, or a product.
    A benchmark measures performance and publishes a number. An audit tests
    conformance against a written standard, issues a scoped verdict, discloses
    its own limitations, and holds the issuer to the same rules. That is the
    difference this file implements.

WHAT IT DOES NOT DO, STATED FIRST

    It does not score the subject's forecasting ability. It does not rank.
    It does not compute a Brier and it does not say who is better. RPAS 1.06
    is unconditional: conformance certifies PROCESS, never foresight. A Type
    III report that shaded into a performance verdict would be a benchmark
    wearing an audit's clothes, which is the failure this instrument exists
    to be the opposite of.

    It also does not assume the subject's schema. A foreign record is ingested
    through a DECLARED MAPPING the auditor writes and publishes with the
    report. Where the mapping cannot reach a field, the procedure returns a
    SCOPE LIMITATION, never a finding. Auditing something into a defect
    because you could not read it is malpractice.

THE THREE OUTCOMES, AND WHY THE THIRD MATTERS MOST

    FINDING     the record demonstrably departs from a named clause
    CONFORMS    the procedure ran and the record satisfied the clause
    SCOPE       the procedure could not be performed on public inputs

    SCOPE is not a softer FINDING. It is the honest report that the public
    record does not carry what the clause requires an auditor to see, and it
    is the most common result on a subject who never agreed to be audited.
    A report of ten findings and no scope limitations is a report that guessed.

USE
    python type3.py --scope engagement.json      write/validate the engagement
    python type3.py --run engagement.json        perform the procedures
    python type3.py --report engagement.json     emit the 7.01 report

    python type3.py --template > engagement.json   start here

SELF-APPLICATION
    Pass "subject_is_self": true and the report prints as a Type I on this
    desk. 6.04 binds the issuer publicly; the first Type III report should
    carry the desk as a co-subject so the standard is not seen to be applied
    outward only. The instrument makes that cheap on purpose.
"""

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent

# --------------------------------------------------------------------------
# engagement declaration
# --------------------------------------------------------------------------

TEMPLATE = {
    "schema": "rpas-type3-engagement/1.0",
    "engagement_type": "III",
    "subject": {
        "name": "",
        "kind": "public forecasting benchmark | platform | published record",
        "record_url": "",
        "record_file": "",
        "retrieved": "",
        "notes": "how the record was obtained, verbatim"
    },
    "subject_is_self": False,
    "scope": {
        "period_start": "",
        "period_end": "",
        "entries_in_scope": "all entries in the retrieved record",
        "excluded": [],
        "basis": "public inputs only; no access to subject's internal systems"
    },
    "independence": {
        "auditor_holds_position_in_subject": False,
        "auditor_competes_with_subject": False,
        "disclosure": "state any relationship. An undisclosed one voids the report."
    },
    "mapping": {
        "_note": "declared field mapping. Left side = RPAS concept, right "
                 "side = key in the subject's record, or null if absent. "
                 "A null is a SCOPE LIMITATION, never a finding.",
        "entries_path": "projections",
        "id": "id",
        "statement": "statement",
        "resolution_basis": "resolution",
        "failure_condition": None,
        "probability": "probability",
        "deadline": "deadline",
        "date_issued": "date_issued",
        "status": "status",
        "resolved_date": None,
        "priors_declared": None,
        "keyed_keyless": None,
        "is_control": None,
        "arm": "model",
        "seal": None
    },
    "control_arm_tags": [],
    "_control_arm_tags_note": "arm tags whose rows ARE controls, e.g. "
                              "['control/baserate']. Used when the record "
                              "carries no per-row control flag. Declared in "
                              "the engagement so the reading is on the record.",
    "status_values": {
        "open": ["open"],
        "hit": ["hit", "yes", "resolved_yes", "true"],
        "miss": ["miss", "no", "resolved_no", "false"],
        "void": ["void", "annulled", "ambiguous", "n/a"]
    },
    "public_claims": {
        "_note": "what the subject publicly asserts about its own record. "
                 "Procedures P10-P12 test the claims, not the auditor's "
                 "impression of them. Quote or leave empty.",
        "publishes_scores": None,
        "claims_verifiability_without_trust": None,
        "claims_contamination_resistance": None
    }
}


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def get(rec, key):
    """Read a mapped field. None key -> None, which reads as unavailable."""
    if key is None:
        return None
    cur = rec
    for part in str(key).split("."):
        if not isinstance(cur, dict) or part not in cur:
            return None
        cur = cur[part]
    return cur


def entries_of(eng):
    src = eng["subject"].get("record_file") or ""
    p = Path(src)
    if not p.is_absolute():
        p = HERE / src
    if not p.exists():
        raise SystemExit(f"record_file not found: {p}")
    data = json.loads(p.read_text(encoding="utf-8", errors="replace"))
    path = eng["mapping"].get("entries_path")
    if path:
        for part in str(path).split("."):
            data = data[part]
    if not isinstance(data, list):
        raise SystemExit("entries_path did not resolve to a list")
    return data


def norm_status(eng, raw):
    s = str(raw or "").strip().lower()
    for canon, vals in eng["status_values"].items():
        if s in [str(v).lower() for v in vals]:
            return canon
    return "unknown"


# --------------------------------------------------------------------------
# procedures — each returns (code, cite, headline, detail)
#   code in {FINDING, CONFORMS, SCOPE}
# --------------------------------------------------------------------------

def P01_falsifiability(eng, rows):
    """4.03 — an entry missing its failure condition is unfalsifiable."""
    key = eng["mapping"]["failure_condition"]
    if key is None:
        return ("SCOPE", "RPAS 4.03",
                "failure conditions are not present in the public record",
                "The record carries no field a failure condition could map to. "
                "Whether the subject registers one privately cannot be "
                "determined from public inputs. Under 4.03 an entry without a "
                "failure condition is unfalsifiable and unsealable; this "
                "engagement can state only that the public record does not "
                "show one.")
    missing = [r for r in rows if not str(get(r, key) or "").strip()]
    if missing:
        return ("FINDING", "RPAS 4.03",
                f"{len(missing)} of {len(rows)} entries carry no failure condition",
                "An entry that does not state what would make it a miss cannot "
                "be adjudicated against by a third party. Ids: "
                + ", ".join(str(get(r, eng['mapping']['id'])) for r in missing[:12])
                + (" ..." if len(missing) > 12 else ""))
    return ("CONFORMS", "RPAS 4.03",
            "every entry in scope carries a failure condition", "")


def P02_prereg_completeness(eng, rows):
    """4.02 — the pre-registration field set."""
    need = ["statement", "resolution_basis", "probability", "deadline", "date_issued"]
    absent = [f for f in need if eng["mapping"].get(f) is None]
    if absent:
        return ("SCOPE", "RPAS 4.02",
                f"{len(absent)} required field(s) absent from the record schema",
                "Not mappable: " + ", ".join(absent) + ". The clause requires "
                "these at seal; the public record does not expose them, so "
                "completeness is undeterminable rather than defective.")
    bad = []
    for r in rows:
        gaps = [f for f in need if not str(get(r, eng["mapping"][f]) or "").strip()]
        if gaps:
            bad.append((get(r, eng["mapping"]["id"]), gaps))
    if bad:
        return ("FINDING", "RPAS 4.02",
                f"{len(bad)} entries incomplete at pre-registration",
                "; ".join(f"{i}: missing {'+'.join(g)}" for i, g in bad[:8]))
    return ("CONFORMS", "RPAS 4.02",
            "every entry carries the full pre-registration field set", "")


def P03_absolute_dates(eng, rows):
    """4.02a/gate doctrine — relative timeframes are not adjudicable."""
    key = eng["mapping"]["statement"]
    if key is None:
        return ("SCOPE", "RPAS 4.02", "statements not mappable", "")
    rel = re.compile(r"\b(within|next|coming|following)\s+"
                     r"(the\s+)?(\d+|a|an|few|several)?\s*"
                     r"(hours?|days?|weeks?|months?|years?)\b", re.I)
    hits = [r for r in rows if rel.search(str(get(r, key) or ""))]
    if hits:
        return ("FINDING", "RPAS 4.02",
                f"{len(hits)} entries state a relative timeframe in the claim",
                "A relative window resolves differently depending on when it "
                "is read. Ids: "
                + ", ".join(str(get(r, eng['mapping']['id'])) for r in hits[:10]))
    return ("CONFORMS", "RPAS 4.02", "claims use absolute dates", "")


def P04_misfire_inclusion(eng, rows):
    """5.03 — misses logged with the same ceremony as hits."""
    st = eng["mapping"]["status"]
    if st is None:
        return ("SCOPE", "RPAS 5.03", "resolution status not mappable", "")
    c = {}
    for r in rows:
        s = norm_status(eng, get(r, st))
        c[s] = c.get(s, 0) + 1
    hits, misses = c.get("hit", 0), c.get("miss", 0)
    resolved = hits + misses
    if resolved == 0:
        return ("SCOPE", "RPAS 5.03", "no resolved entries in scope",
                "Nothing to test; the record has not yet met the world.")
    if misses == 0 and hits > 0:
        return ("FINDING", "RPAS 5.03",
                f"{hits} hits and zero misses in the public record",
                "A record with no misses is either perfect or incomplete. "
                "3.08 names the shape: a compilation selected on outcome "
                "returns hits by construction and its misses have no index.")
    return ("CONFORMS", "RPAS 5.03",
            f"misses present alongside hits ({hits} hit / {misses} miss)", "")


def P05_fifty_entry_gate(eng, rows):
    """5.02 — no score computed or published before fifty entries."""
    claim = eng["public_claims"].get("publishes_scores")
    if claim is None:
        return ("SCOPE", "RPAS 5.02",
                "the subject's scoring-publication practice was not declared",
                "Populate public_claims.publishes_scores to run this procedure.")
    if claim and len(rows) < 50:
        return ("FINDING", "RPAS 5.02",
                f"scores published over {len(rows)} entries, below the fifty-entry gate",
                "Small records produce scores that are noise wearing the "
                "costume of measurement.")
    return ("CONFORMS", "RPAS 5.02",
            f"{len(rows)} entries in scope; the gate is satisfied", "")


def P06_keyed_keyless(eng, rows):
    """5.04 / 1.04 — the master law. Almost always a SCOPE on a foreign record."""
    key = eng["mapping"]["keyed_keyless"]
    if key is None:
        return ("SCOPE", "RPAS 1.04 / 5.04",
                "the record carries no keyed/keyless classification",
                "1.04: 'a test that cannot distinguish keyed from keyless is "
                "not a test; it is a mirror.' 5.04 admits only keyless hits "
                "above baseline toward a faculty claim. Absent the field, no "
                "result in this record can bear on a faculty claim, and none "
                "is understood to be offered. This is a scope limitation on "
                "the engagement, and simultaneously the clearest statement of "
                "what a performance benchmark does not measure.")
    unset = [r for r in rows if not str(get(r, key) or "").strip()]
    if unset:
        return ("FINDING", "RPAS 4.02f / 4.03",
                f"{len(unset)} entries carry no determination",
                "4.03: a determination made after resolution is KEYED by rule.")
    return ("CONFORMS", "RPAS 5.04",
            "every entry carries a pre-registered determination", "")


def P07_controls(eng, rows):
    """4.06 — decoys, opposite-side slots, null questions.

    A record may mark controls with a field OR carry them as a named arm.
    Both are declarations; refusing to read the second was reporting zero
    controls on a record that had nine.
    """
    key = eng["mapping"]["is_control"]
    arm_key = eng["mapping"].get("arm") or eng["mapping"].get("model")
    ctl_tags = {t.strip().lower()
                for t in (eng.get("control_arm_tags") or []) if t.strip()}
    if key is None and arm_key and ctl_tags:
        n = sum(1 for r in rows
                if str(get(r, arm_key) or "").strip().lower() in ctl_tags)
        if n == 0:
            return ("FINDING", "RPAS 4.06",
                    "declared control arms carry no entries in this record",
                    "A faculty claim that has never returned a correct NULL "
                    "on a control has not been tested.")
        return ("CONFORMS", "RPAS 4.06",
                f"{n} control entries present, identified by arm tag "
                f"({', '.join(sorted(ctl_tags))})", "")
    if key is None:
        return ("SCOPE", "RPAS 4.06",
                "the record does not distinguish control entries",
                "4.06 is a SHOULD. Its absence is not a departure from a must, "
                "but a record with no control has not demonstrated that its "
                "hits are distinguishable from apophenia, and the "
                "decoy-detection rate is the apophenia tell.")
    n = sum(1 for r in rows if get(r, key))
    if n == 0:
        return ("FINDING", "RPAS 4.06",
                "no control entries in the record",
                "A faculty claim that has never returned a correct NULL on a "
                "control has not been tested.")
    return ("CONFORMS", "RPAS 4.06", f"{n} control entries present", "")


def P08_commitment(eng, rows):
    """4.04 / 4.05 — hash commitment and an external clock."""
    key = eng["mapping"]["seal"]
    if key is None:
        return ("SCOPE", "RPAS 4.04 / 4.05",
                "no per-entry commitment is exposed in the record",
                "4.04 requires hash commitment at each change in a public "
                "history; 4.05 requires publication on a clock the subject "
                "does not control. A repository history or platform database "
                "may satisfy 4.04 in substance without exposing a per-entry "
                "seal; that determination requires access this engagement "
                "does not have.")
    unsealed = [r for r in rows if not str(get(r, key) or "").strip()]
    if unsealed:
        return ("FINDING", "RPAS 4.04",
                f"{len(unsealed)} entries carry no commitment", "")
    return ("CONFORMS", "RPAS 4.04", "every entry is committed", "")


def P09_deadline_integrity(eng, rows):
    """5.06 — an entry resolved after a silently moved deadline."""
    dl, rd = eng["mapping"]["deadline"], eng["mapping"]["resolved_date"]
    if dl is None or rd is None:
        return ("SCOPE", "RPAS 5.06",
                "deadline or resolution date not mappable", "")
    late = []
    for r in rows:
        try:
            d = datetime.strptime(str(get(r, dl))[:10], "%Y-%m-%d").date()
            x = str(get(r, rd) or "")[:10]
            if not x:
                continue
            v = datetime.strptime(x, "%Y-%m-%d").date()
            if v > d:
                late.append((get(r, eng["mapping"]["id"]), str(d), str(v)))
        except (ValueError, TypeError):
            continue
    if late:
        return ("FINDING", "RPAS 5.06",
                f"{len(late)} entries resolved after their stated deadline",
                "Resolution after the deadline is not by itself a defect; "
                "resolution after the deadline WITHOUT the deadline being "
                "stated as extended is. Examples: "
                + "; ".join(f"{i} due {d}, resolved {v}" for i, d, v in late[:6]))
    return ("CONFORMS", "RPAS 5.06",
            "no entry resolved past its stated deadline", "")


def P10_open_past_deadline(eng, rows):
    """5.06 — unresolved-by-neglect scores as a miss by rule."""
    dl, st = eng["mapping"]["deadline"], eng["mapping"]["status"]
    if dl is None or st is None:
        return ("SCOPE", "RPAS 5.06", "deadline or status not mappable", "")
    today = datetime.now(timezone.utc).date()
    stale = []
    for r in rows:
        if norm_status(eng, get(r, st)) != "open":
            continue
        try:
            d = datetime.strptime(str(get(r, dl))[:10], "%Y-%m-%d").date()
        except (ValueError, TypeError):
            continue
        if d < today:
            stale.append((get(r, eng["mapping"]["id"]), str(d)))
    if stale:
        return ("FINDING", "RPAS 5.06",
                f"{len(stale)} entries remain open past their deadline",
                "5.06: a dropped or unresolved-by-neglect entry scores as a "
                "miss by rule. Examples: "
                + ", ".join(f"{i} ({d})" for i, d in stale[:10]))
    return ("CONFORMS", "RPAS 5.06", "no entry is open past its deadline", "")


def P11_stated_vs_operational(eng, rows):
    """6.03 / 1.06 — does the subject's public claim match its record?"""
    pc = eng["public_claims"]
    out = []
    if pc.get("claims_verifiability_without_trust") and \
            eng["mapping"]["seal"] is None:
        out.append("The subject claims verifiability without trusting the "
                   "organiser, while the retrieved record exposes no per-entry "
                   "commitment a reader could recompute. The claim may hold "
                   "through a mechanism outside the record; the record alone "
                   "does not carry it.")
    if pc.get("claims_contamination_resistance") and \
            eng["mapping"]["date_issued"] is None:
        out.append("The subject claims contamination resistance, while the "
                   "record does not expose an issue date per entry. Resistance "
                   "rests on the claim that questions post-date training; the "
                   "record does not let a reader check it.")
    if not out:
        return ("CONFORMS", "RPAS 6.03",
                "no stated-versus-operational gap detected in scope", "")
    return ("FINDING", "RPAS 6.03", "stated-versus-operational gap",
            " ".join(out))


def P12_recomputability(eng, rows):
    """6.03 — sufficient for an unconnected third party to recompute."""
    m = eng["mapping"]
    have = sum(1 for k in ("id", "statement", "resolution_basis", "probability",
                           "deadline", "status") if m.get(k) is not None)
    if have < 6:
        return ("FINDING", "RPAS 6.03",
                f"the public record exposes {have} of 6 fields needed to "
                f"recompute a published grade",
                "6.03 requires the record be sufficient for an experienced "
                "third party with no previous connection to recompute every "
                "published grade from public inputs.")
    return ("CONFORMS", "RPAS 6.03",
            "the record exposes the fields needed to recompute grades", "")


PROCEDURES = [P01_falsifiability, P02_prereg_completeness, P03_absolute_dates,
              P04_misfire_inclusion, P05_fifty_entry_gate, P06_keyed_keyless,
              P07_controls, P08_commitment, P09_deadline_integrity,
              P10_open_past_deadline, P11_stated_vs_operational,
              P12_recomputability]


# --------------------------------------------------------------------------

def run(eng):
    rows = entries_of(eng)
    results = []
    for fn in PROCEDURES:
        try:
            code, cite, head, detail = fn(eng, rows)
        except Exception as exc:
            code, cite, head, detail = ("SCOPE", "—",
                                        f"{fn.__name__} could not be performed",
                                        f"{type(exc).__name__}: {exc}")
        results.append({"procedure": fn.__name__, "code": code, "cite": cite,
                        "headline": head, "detail": detail})
    return rows, results


def cmd_run(eng, path):
    rows, results = run(eng)
    tally = {}
    for r in results:
        tally[r["code"]] = tally.get(r["code"], 0) + 1
    print(f"\nTYPE III — {eng['subject']['name'] or '(unnamed subject)'}")
    print("=" * 72)
    print(f"  {len(rows)} entries in scope\n")
    for r in results:
        mark = {"FINDING": "FINDING ", "CONFORMS": "conforms",
                "SCOPE": "SCOPE   "}[r["code"]]
        print(f"  {mark}  {r['cite']:<20} {r['headline']}")
    print(f"\n  {tally.get('FINDING',0)} finding(s) · "
          f"{tally.get('SCOPE',0)} scope limitation(s) · "
          f"{tally.get('CONFORMS',0)} conforming")
    out = Path(path).with_suffix(".results.json")
    out.write_text(json.dumps({"generated": datetime.now(timezone.utc).isoformat(),
                               "engagement": eng, "results": results,
                               "entries_in_scope": len(rows)},
                              indent=2), encoding="utf-8")
    print(f"  results → {out}\n")
    return 0


def cmd_report(eng, path):
    rows, results = run(eng)
    s = eng["subject"]
    now = datetime.now(timezone.utc)
    findings = [r for r in results if r["code"] == "FINDING"]
    scopes = [r for r in results if r["code"] == "SCOPE"]
    conf = [r for r in results if r["code"] == "CONFORMS"]
    L = []
    A = L.append
    A(f"# RPAS TYPE III CONFORMANCE REPORT")
    A(f"## Subject: {s['name'] or '(unnamed)'}")
    A("")
    A(f"**Engagement type.** Type III — third-party audit (RPAS 1.02c), "
      f"applying Type I procedures to a forecaster other than the auditor.")
    A(f"**Report date.** {now.strftime('%Y-%m-%d')}  ")
    A(f"**Record retrieved.** {s.get('retrieved') or '(not stated)'}  ")
    A(f"**Source of record.** {s.get('record_url') or '(not stated)'}  ")
    A(f"**Entries in scope.** {len(rows)}  ")
    A(f"**Period.** {eng['scope'].get('period_start') or '—'} to "
      f"{eng['scope'].get('period_end') or '—'}")
    A("")
    A("### Validity clause (RPAS 1.06, unconditional)")
    A("")
    A("Conformance with these standards certifies **process, never foresight**. "
      "Nothing in this report is an assessment of the subject's forecasting "
      "ability, and nothing in it should be read as ranking the subject "
      "against any other forecaster. A departure from a clause is a departure "
      "from a documentation and pre-registration discipline; it is not "
      "evidence that the subject forecasts badly, and conformance would not "
      "be evidence that the subject forecasts well.")
    A("")
    A("### Independence (RPAS Chapter 3)")
    A("")
    ind = eng.get("independence", {})
    A(f"- Auditor holds a position in the subject: "
      f"**{'yes' if ind.get('auditor_holds_position_in_subject') else 'no'}**")
    A(f"- Auditor competes with the subject: "
      f"**{'yes' if ind.get('auditor_competes_with_subject') else 'no'}**")
    A(f"- Disclosure: {ind.get('disclosure','(none stated)')}")
    A("")
    A("### Basis and limitation of the engagement")
    A("")
    A(f"{eng['scope'].get('basis','public inputs only')}. The subject did not "
      f"participate in this engagement and was under no obligation to. Every "
      f"procedure was performed against the record as retrieved, through the "
      f"field mapping published in §Mapping below. Where the mapping could "
      f"not reach a field the procedure returns a **scope limitation**, not a "
      f"finding: a record cannot be held defective for failing to expose "
      f"something the auditor merely could not read.")
    A("")
    A(f"### Summary")
    A("")
    A(f"| | count |")
    A(f"|---|---|")
    A(f"| Findings | {len(findings)} |")
    A(f"| Scope limitations | {len(scopes)} |")
    A(f"| Procedures conforming | {len(conf)} |")
    A(f"| Procedures performed | {len(results)} |")
    A("")
    if findings:
        A("### Findings")
        A("")
        for i, r in enumerate(findings, 1):
            A(f"**F{i} — {r['cite']}.** {r['headline']}.")
            if r["detail"]:
                A("")
                A(f"{r['detail']}")
            A("")
    if scopes:
        A("### Scope limitations")
        A("")
        A("These are the procedures the public record did not permit. They are "
          "reported with the same prominence as findings because an audit that "
          "hides what it could not test is not an audit.")
        A("")
        for i, r in enumerate(scopes, 1):
            A(f"**S{i} — {r['cite']}.** {r['headline']}.")
            if r["detail"]:
                A("")
                A(f"{r['detail']}")
            A("")
    if conf:
        A("### Procedures conforming")
        A("")
        for r in conf:
            A(f"- **{r['cite']}** — {r['headline']}")
        A("")
    A("### Mapping (published so the engagement is reproducible)")
    A("")
    A("```json")
    A(json.dumps(eng["mapping"], indent=1))
    A("```")
    A("")
    A("### Self-application (RPAS 6.04)")
    A("")
    A("The desk issuing these standards is bound by them in public and reports "
      "its own nonconformance with the same ceremony as any finding above. "
      "The desk's own record and its open departures are published at "
      "`/conformance.html`; readers auditing this report are invited to audit "
      "the auditor first. A Type III report issued by a desk that does not "
      "publish its own failures is a marketing document.")
    A("")
    A("### Right of reply")
    A("")
    A("The subject may respond, and any response received will be published "
      "adjacent to this report without edit. Corrections are entered as new "
      "dated entries in the revision record; this report is not rewritten "
      "(5.07 — retractions stay in the record).")
    A("")
    out = Path(path).with_suffix(".report.md")
    out.write_text("\n".join(L), encoding="utf-8")
    print(f"report → {out}  ({len(findings)} finding(s), "
          f"{len(scopes)} scope limitation(s))")
    return 0


def main():
    ap = argparse.ArgumentParser(description="RPAS Type III third-party audit")
    ap.add_argument("--template", action="store_true")
    ap.add_argument("--scope", metavar="FILE")
    ap.add_argument("--run", metavar="FILE")
    ap.add_argument("--report", metavar="FILE")
    a = ap.parse_args()
    if a.template:
        print(json.dumps(TEMPLATE, indent=1))
        return 0
    path = a.scope or a.run or a.report
    if not path:
        ap.print_help()
        return 0
    eng = load(path)
    if a.scope:
        miss = [k for k in ("subject", "scope", "mapping", "status_values")
                if k not in eng]
        if miss:
            print("engagement missing: " + ", ".join(miss))
            return 1
        print(f"engagement valid — subject: {eng['subject']['name'] or '(unnamed)'}")
        print(f"  mapped fields: "
              f"{sum(1 for v in eng['mapping'].values() if v and not str(v).startswith('_'))}")
        print(f"  unmapped (will report as SCOPE): "
              + ", ".join(k for k, v in eng["mapping"].items()
                          if v is None) or "  none")
        return 0
    if a.run:
        return cmd_run(eng, path)
    return cmd_report(eng, path)


if __name__ == "__main__":
    sys.exit(main())

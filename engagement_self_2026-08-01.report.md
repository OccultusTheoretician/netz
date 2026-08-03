# RPAS TYPE III CONFORMANCE REPORT
## Subject: The Prescient Desk (self)

**Engagement type.** Type III — third-party audit (RPAS 1.02c), applying Type I procedures to a forecaster other than the auditor.
**Report date.** 2026-08-01  
**Record retrieved.** 2026-08-01  
**Source of record.** https://retroprescientaudit.com/ledger.json  
**Entries in scope.** 246  
**Period.** 2026-07-20 to 2026-08-01

### Validity clause (RPAS 1.06, unconditional)

Conformance with these standards certifies **process, never foresight**. Nothing in this report is an assessment of the subject's forecasting ability, and nothing in it should be read as ranking the subject against any other forecaster. A departure from a clause is a departure from a documentation and pre-registration discipline; it is not evidence that the subject forecasts badly, and conformance would not be evidence that the subject forecasts well.

### Independence (RPAS Chapter 3)

- Auditor holds a position in the subject: **no**
- Auditor competes with the subject: **no**
- Disclosure: Self-application under 6.04. The auditor IS the subject; this is a Type I in form and is published to demonstrate the standard is applied inward before outward.

### Basis and limitation of the engagement

public inputs only; no access to subject's internal systems. The subject did not participate in this engagement and was under no obligation to. Every procedure was performed against the record as retrieved, through the field mapping published in §Mapping below. Where the mapping could not reach a field the procedure returns a **scope limitation**, not a finding: a record cannot be held defective for failing to expose something the auditor merely could not read.

### Summary

| | count |
|---|---|
| Findings | 4 |
| Scope limitations | 1 |
| Procedures conforming | 7 |
| Procedures performed | 12 |

### Findings

**F1 — RPAS 4.02.** 18 entries state a relative timeframe in the claim.

A relative window resolves differently depending on when it is read. Ids: KKR-20260720-01, KKR-20260720-03, KKR-20260720-05, KKR-20260720-07, KKR-20260720-08, KKR-20260720-09, KKR-20260720-11, KKR-20260720-12, KKR-20260720-14, KKR-20260720-21

**F2 — RPAS 4.02f / 4.03.** 95 entries carry no determination.

4.03: a determination made after resolution is KEYED by rule.

**F3 — RPAS 4.04.** 161 entries carry no commitment.

**F4 — RPAS 5.06.** 13 entries resolved after their stated deadline.

Resolution after the deadline is not by itself a defect; resolution after the deadline WITHOUT the deadline being stated as extended is. Examples: KKR-20260720-04 due 2026-07-29, resolved 2026-07-31; KKR-20260720-08 due 2026-07-23, resolved 2026-07-24; KKR-20260720-21 due 2026-07-23, resolved 2026-07-24; KKR-20260720-25 due 2026-07-23, resolved 2026-07-24; KKR-20260720-26 due 2026-07-23, resolved 2026-07-24; KKR-20260721-01 due 2026-07-31, resolved 2026-08-01

### Scope limitations

These are the procedures the public record did not permit. They are reported with the same prominence as findings because an audit that hides what it could not test is not an audit.

**S1 — RPAS 4.06.** the record does not distinguish control entries.

4.06 is a SHOULD. Its absence is not a departure from a must, but a record with no control has not demonstrated that its hits are distinguishable from apophenia, and the decoy-detection rate is the apophenia tell.

### Procedures conforming

- **RPAS 4.03** — every entry in scope carries a failure condition
- **RPAS 4.02** — every entry carries the full pre-registration field set
- **RPAS 5.03** — misses present alongside hits (6 hit / 17 miss)
- **RPAS 5.02** — 246 entries in scope; the gate is satisfied
- **RPAS 5.06** — no entry is open past its deadline
- **RPAS 6.03** — no stated-versus-operational gap detected in scope
- **RPAS 6.03** — the record exposes the fields needed to recompute grades

### Mapping (published so the engagement is reproducible)

```json
{
 "_note": "declared field mapping. Left side = RPAS concept, right side = key in the subject's record, or null if absent. A null is a SCOPE LIMITATION, never a finding.",
 "entries_path": "projections",
 "id": "id",
 "statement": "statement",
 "resolution_basis": "resolution",
 "failure_condition": "failure_condition",
 "probability": "probability",
 "deadline": "deadline",
 "date_issued": "date_issued",
 "status": "status",
 "resolved_date": "resolved_date",
 "priors_declared": null,
 "keyed_keyless": "keyed_keyless",
 "is_control": null,
 "seal": "seal_sha256"
}
```

### Self-application (RPAS 6.04)

The desk issuing these standards is bound by them in public and reports its own nonconformance with the same ceremony as any finding above. The desk's own record and its open departures are published at `/conformance.html`; readers auditing this report are invited to audit the auditor first. A Type III report issued by a desk that does not publish its own failures is a marketing document.

### Right of reply

The subject may respond, and any response received will be published adjacent to this report without edit. Corrections are entered as new dated entries in the revision record; this report is not rewritten (5.07 — retractions stay in the record).

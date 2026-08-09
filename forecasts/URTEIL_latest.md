# URTEIL - verdict-grounding audit - 2026-08-09T20:49:48Z

Every non-ABSTAIN jury verdict audited against the held evidence for its row, by the same mechanics that audit forecast citations. Grounding is checkable even when the verdict is right; the CORRECT-BUT-UNGROUNDED class is the one the blind protocol cannot see on its own.

| class | n |
|---|---|
| GROUNDED | 0 |
| THIN | 0 |
| UNGROUNDED-SPECIFIC | 0 |
| UNHELD-VERDICT | 0 |
| UNHELD-SEARCHED | 3 |
| OUT-OF-HELD | 0 |
| ABSTAIN | 2 |

## CUSTODY
- held_evidence_2026-08-08.json holds 0 rows - held-evidence gathering returned nothing for a jury day; every verdict that day is unauditable at the custody layer
- held_evidence_2026-08-09.json holds 0 rows - held-evidence gathering returned nothing for a jury day; every verdict that day is unauditable at the custody layer

## All non-GROUNDED verdicts
- KKR-20260724-09 - juror A (searched) - MISS (final MISS) - **UNHELD-SEARCHED** - no held evidence for this row - a searched juror may rule from its own access (8.07 coercion is cold-seat only), but grounding cannot be audited; disclosed, unauditable
- KKR-20260725-07 - juror A (searched) - MISS (final MISS) - **UNHELD-SEARCHED** - no held evidence for this row - a searched juror may rule from its own access (8.07 coercion is cold-seat only), but grounding cannot be audited; disclosed, unauditable
- KKR-20260731-15 - juror A (searched) - HIT (final HIT) - **UNHELD-SEARCHED** - no held evidence for this row - a searched juror may rule from its own access (8.07 coercion is cold-seat only), but grounding cannot be audited; disclosed, unauditable

urteil/1.0 - read-only - the desk's method pointed at the desk's own bench

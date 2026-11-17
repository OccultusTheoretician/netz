# RPAS-26 - AMENDMENT 2026-11-17

**AUTHORSHIP.** Drafted by the desk's assistant on 2026-11-17 under the operator's delegation of 2026-11-13, and adopted by the operator applying it. PROVENANCE: draft - assistant-drafted 2026-11-17, operator rework pending.

**Amends the Retro-Prescient Audit Standards, First Edition 2026 v1, at 5.06 and 5.07 (correcting a resolved verdict). Records one nonconformance under 6.04.**

Issued as a dated amendment, not an edit; 7.05 governs. Entries remain scored under the edition in force at their sealing.

---

## 5.07a - Correcting a resolved verdict

A resolved verdict (HIT or MISS) changes only when a later examination, run under a rule printed no later than the change, finds the ruling contradicted by named sources. The change is conformant only when all four of the following hold in the publish that carries it:

1. **The row keeps what it replaces.** The superseded verdict in `status_superseded`; the superseded notes in `notes_superseded`.
2. **The row states the change.** The date in `resolution_corrected`, the reason in `resolution_correction`, who ruled it in `resolution_authority`.
3. **The ledger discloses it by id.** A `disclosed_entries` record with the id, clause `5.06`, the verdicts before and after (`status_from`, `status_to`), the correction date (`corrected`), its own date (`dated`) and a `finding`.
4. **The findings register prints it.**

A correction never touches a sealed field. The score moves with the corrected verdict, whichever way that moves it. A reversal that lacks any of the four remains a 5.06 failure.

## 6.04 - Nonconformance recorded

KKR-20260915-13 (lmstudio/realist, 40%, keyed) was reversed from MISS to HIT in the publish of 2026-10-13 (`d4e3a50`), after a blind validation run under the operator's rule of 2026-10-12. Conditions 1 and 2 held that day. The rule and the validation were printed on 2026-10-15 (`c4e0e91`), two days after the change; conditions 3 and 4 were met on 2026-11-17, 35 days late (Finding 20). The correction stands.

## The verifier and the publish gate

`rpas_verify.py` 1.3 reads a reversal that meets conditions 1 to 3 as conformant-as-disclosed under 5.07 and prints it; condition 4 sits outside the ledger and is checked by reading the register. Any other reversal remains a MUST failure under 5.06. A comparison between two snapshots that both predate a correction's disclosure still fails, because neither carries it. `desk.py verify` runs the same comparison against the last committed ledger at every publish.

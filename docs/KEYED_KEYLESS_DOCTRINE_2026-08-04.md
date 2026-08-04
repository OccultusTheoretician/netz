# KEYED / KEYLESS — DETERMINATION DOCTRINE

**Revision 2, 2026-08-04. Revision 1 was issued and applied the same day; §Correction below states what it got wrong and why.**

**Issued 2026-08-04 under RPAS-26 §1.04 and §4.02f. Companion to Amendments 2026-08-04 and 2026-08-04b.**

---

## Why this exists, and why its existence is itself a finding

§1.04 is the master law: *every test, entry, and scored claim must specify, before resolution, what would make a hit keyed versus keyless.* §7.04 scopes the desk's entire novelty claim to that split. §4.02f requires the determination on every entry.

**Nowhere does the standard state the test.**

The determination has therefore been made 269 times against a criterion that was never written down — 112 entries ruled interactively across earlier sessions, and 157 ruled in a single pass on 2026-08-04. This document states the criterion. It post-dates its own first application by weeks and its most recent by minutes, and it is issued anyway, because §7.04's claimed invention is **pre-registration of the judgment criterion, cryptographically committed** and the desk had not pre-registered its own.

That is the finding. The doctrine below is the remedy.

---

## THE TEST

> **KEYED** — a cited prior states the outcome, **or** names the same specific subject *and* the same specific proceeding, such that the claim asserts that proceeding's continuation, resolution, or ordinary next stage.
>
> **KEYLESS** — the claim requires a numeric threshold no prior reports as reached, the result of a contest no prior reports, or a subject or proceeding no prior names **while the cited priors are readable**.
>
> **Unreadable priors are KEYED by rule (4.03).** Where an entry's cited items support nothing — no discriminating vocabulary shared with the claim — or where it cites most of the record, no keyless finding is available. "Went beyond its declared priors" presupposes priors that can be read. A forecaster may have held the right item in view and cited badly; the record cannot say. 4.03 already defaults KEYED where the determination cannot be made.
>
> **Ambiguous citation.** Where a citation number resolves to several candidate items, the determination is made across *all* of them. If any candidate satisfies KEYED, the entry is KEYED. **Charity runs toward keyed and never toward keyless.**
>
> **Conjunctive claims** are ruled on the element the priors do not reach. A confirmation the priors foreshadow, bundled with a vote margin they do not supply, is KEYLESS.
>
> **Mechanical arms are KEYED by construction.** A climatological control emits one probability per reference class computed from resolved history; a rule-generated row is produced by rule. Neither can exceed its inputs, and neither is exercising judgment that could.

---

## Why attribution rather than strict deduction

§1.04 asks whether a hit "would be deducible." Read strictly — could the outcome be *derived* from the priors — almost nothing qualifies: a manhunt does not entail an arrest, a primary win does not entail a general, 5.2% does not entail 6.00%. Applied to the 123 judgeable entries open on 2026-08-04, strict deduction returns **122 keyless**.

Read as attribution — §7.04's own stated purpose, *only keyless hits bearing on faculty claims* — the same set returns **47 keyed of 123**.

Three reasons the attribution reading governs:

**It is what the published text already anchors to.** §7.04(d) grounds the split in *contamination and leakage controls* — machine-learning benchmark-contamination auditing and parapsychology's sensory-leakage protocols. Leakage has never meant the subject could deduce the target. It means the information reached them through an ordinary channel. That is attribution, and it is already in the standard.

**It errs in the direction that does not flatter.** Keyless is the number that bears on faculty and the number §7.04's novelty claim is scoped to. Strict deduction would have inflated it from 37 to roughly 159. Where a standard's master law admits two honest readings, an audit desk takes the one that makes its headline metric smaller. That principle governs future contested readings too, and is stated here so it can be held against the desk.

**It survives the reverse test.** A forecaster handed "police hunt for a suspect in the Berlin Pride attack" and answering "an arrest is announced within ninety days" has demonstrated no faculty a reader should credit, even though nothing was deduced. Scoring that as evidence of foresight is the exact failure the split was built to prevent.

---

## Result of the 2026-08-04 pass

157 determinations: **81 keyed, 76 keyless, 1 abstention.**

Of the 81 keyed, **34 are keyed by construction** (25 `control/baserate`, 9 `kfk/halflife`) and 47 by the leakage test. The 76 keyless divide into threshold-not-reached, contest-result-not-supplied, and subject-not-named; every entry carries its reason in the imported worksheet, quoting the candidate item where one exists.

One entry is deliberately unruled: the single `operator/human` row. Its priors are what the operator held at seal, nothing in the record holds them, and no third party can rule it. An abstention is recorded rather than a default.

---

## Correction — revision 1 got this backwards, against its own patch

Revision 1 ruled KEYLESS wherever no prior named the subject, **including 22 entries whose citations support nothing and 4 that cite most of the record.**

That contradicted a check shipped hours earlier by the same author. `patch_kk21n.py` prints, at the operator, on any UNSUPPORTED row:

> *Nothing cited supports this claim. A KEYLESS ruling here asserts the entry went beyond priors that ground nothing — KEYED by rule is the defensible read (4.03).*

Same fact, opposite conclusions, in two documents issued the same day. The patch is right, and it is right on **this doctrine's own stated principle**: keyless is the faculty-bearing number, and a contested reading resolves toward the smaller one. Ruling those 26 keyless inflated the exact figure the doctrine was written to keep honest.

**26 determinations corrected**, keyless to keyed, by `keys_correct.py` on 2026-08-04. Keyless falls 113 → 87; its citation-defect rate falls 32.1% → 11.5%, because the corrected entries were precisely the defective population.

Every corrected row retains `keyed_keyless_superseded`, the correction date, the reason and the authority. Nothing was overwritten. `kkr.py --keys-import` refuses to touch an already-determined row — correctly, since a re-importable determination is a retrofittable one — so the correction was made as an explicit recorded act under 5.07's mark-never-remove requirement rather than as a second import.

The error is left visible on 26 rows rather than repaired into invisibility. A doctrine that corrects itself silently teaches nothing about how much to trust it.

---

## What this doctrine does not fix

**112 entries were ruled before it existed.** They were ruled by the operator, interactively, under a criterion held in his head and not stated. Their distribution — 75 keyed to 37 keyless — is consistent with the attribution reading and inconsistent with strict deduction, which is evidence that the unwritten criterion was substantially this one. Evidence is not a record. Those entries are marked as ruled under an unstated criterion; they are not re-ruled, because §7.05 forbids rescoring under changed rules and because re-ruling them after seeing how the standard was later written is precisely the retrofit this desk exists to detect.

**And until 2026-08-04 the ruling interface showed one prior out of as many as eight.** `_priors_for` returned the first item matching each citation number and discarded the rest silently; 286 sealed entries carry such a number. Determinations made before that fix were made against an arbitrary candidate presented as the record. The 112 fall in that window. This is stated, not repaired.

---

*Issued under RPAS-26 §7.05 as doctrine, not as a revision to the standard's text. The first edition and both amendments remain as issued.*

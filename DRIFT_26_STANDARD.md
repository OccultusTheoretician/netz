# DRIFT-26 - VERSION DRIFT MEASUREMENT UNDER A FROZEN RUBRIC
### First Edition - 2026 - Revision 1 (DRAFT; named DRIFT-26 by the operator 2026-09-07; Revision 1 cut 2026-09-14 and served under the desk's draft-publication law; the operator's only after his rework pass)

**A conformance standard for measuring whether a probabilistic forecasting system has changed between two versions, under conditions that make the comparison attributable.**

Issued by the Retro-Prescient Audit desk (NebelKraehe). Written from the Kalibrierwarte registered report as operated since 2026-08-20 and from the laws the desk has published under RPAS-26, KNM-26 and KNP-26. Where this text and a cited registration differ, the registration governs the desk's own reads until this standard is issued; after issuance, the registration is read as an instance of this standard.

**PROVENANCE: DRAFT** - assistant-drafted under the operator's direction (Revision 0 on 2026-09-07, Revision 1 on 2026-09-14); the operator's only after his rework pass, which replaces the text without moving the date. Served so that the priors printed in Chapters 13 and 14 are on the record upon discovery (RPAS-26 7.04); the priority record is the commit and the OpenTimestamps receipt, not this banner. Every citation in this text was read at the artifact before it entered (2026-09-14). This standard is not issued: a conformance claim against it names the revision and the word DRAFT.

---

## CHAPTER 1 - SCOPE

**1.01** This standard specifies how to elicit, seal, control, adjudicate, pre-register, test and report a comparison between two versions of a forecasting system - two model strings, or one model string under two committed frames - so that a measured difference in calibration or skill can be attributed to the version change and not to a change in the questions, the rubric, the adjudicator or the scorer.

**1.02** It applies to any system that emits probabilities on binary claims with stated resolution criteria and deadlines: language models, ensembles, human forecasters, markets used as comparators, and hybrids. It does not require the systems to be good. It requires the comparison to be honest.

**1.03** Out of scope: what a good forecaster is; any metric's merit; any threshold that a system must clear to be called capable. This standard fixes procedure, not judgment. A conforming report can show two versions that are both noise, and says so.

**1.04** The standard's one doctrine: **the trend is the measurement.** A single calibration read of a single version is an opinion about a snapshot. The object measured is the difference between reads taken under identical conditions, and the series of such differences.

---

## CHAPTER 2 - TERMS

**Row.** One sealed probabilistic claim: statement, probability, resolution criterion, failure condition, deadline, the identity of the arm that issued it, the hash of the rubric it was elicited under, the seal timestamp (UTC), and the identifier of the input packet.

**Arm.** A forecaster identity: model string x lane x tool access x frame. Two forecasters that differ in any of the four are two arms. A Brier belongs to one arm.

**Version change.** A new model string registered for the same lane, access and frame. A change the provider makes behind a fixed model string is NOT a version change under this standard; it is silent drift (Chapter 10).

**Frame.** A committed preamble that changes what a model is asked to attend to without changing the rubric. A frame is part of the arm. Its text is hashed and the hash rides on every row it produces.

**Rubric.** The elicitation text that fixes what a row must contain and how it is scored. **Cohort:** the set of rows elicited under one rubric hash. Comparison across cohorts is descriptive only.

**Packet.** The input a forecaster is shown for one elicitation: the same bytes for every arm compared, hashed and registered.

**Mirror row / control row.** A row composed by a base-rate or market-implied control in the same run as the frontier row it mirrors, on the same claim, resolving on the same criterion and deadline.

**Seat.** Who adjudicated a resolved row: operator; jury with the searched seat adopted; jury with divergence; or another recorded seat.

**Checkpoint.** The first read of a pre-registered hypothesis for an arm, at a floor of resolved rows within one cohort.

**Halt.** The state of a read after any quality check fails. A halt stands until an amendment made before the arm's first checkpoint says otherwise.

**Keyed / keyless (optional module).** A determination whether a row's outcome was deducible from the forecaster's own declared priors (keyed) or was not (keyless). Systems that do not make the determination omit Chapter 9(d) and the H3 test; they say so.

---

## CHAPTER 3 - ARM IDENTITY

**3.01** An implementation MUST register every arm before it seals a row, with: model string, lane, tool access (none / searched / other, named), frame hash (or none), status, and the date of registration.

**3.02** Tool access MUST be treated as part of identity. Searched and cold runs of one model are two arms and MUST NOT be pooled.

**3.03** A frame MUST be treated as part of identity. Rows produced under a frame MUST carry the frame's hash and MUST NOT be pooled with unframed rows of the same model.

**3.04** A version change MUST be registered as a new arm. The predecessor arm keeps its rows, its tile and its identity; retirement of an arm changes its status, never its rows.

**3.05** Rows sealed by a predecessor under one rubric hash and by a successor under the same hash form a version pair. Only a version pair is eligible for the drift test (Chapter 10).

**3.06** No figure may be published for a union of arms. An implementation that publishes a pooled Brier is nonconforming.

**3.07** A frame's text MAY be revised under one arm tag where every row carries the frame's hash (3.03). Rows under different frame texts are separate populations for Chapter 10 and MUST NOT be pooled; the register MUST record the frame in force and retain every superseded frame hash with its dates; rows sealed under a superseded text are a pre-revision class, printed on every face that shows the arm and excluded from any read defined on the revised text. A revision that changes what the arm is asked to price, rather than how the packet or its dates are described to it, is a version change under 3.04. (The desk's instance: FRAME2-2026-09-14 - one sentence naming the packet date, hash 442300f1..., replacing 7b96df74...; registration Section 15.4-15.6; 60 rows under the first text, printed as the class.)

---

## CHAPTER 4 - ELICITATION

**4.01** The rubric MUST be hashed (SHA-256 over LF-normalised UTF-8 bytes) and the hash published before any row is elicited under it. Every row MUST carry the hash. A changed rubric is a new cohort; the change MUST be dated on a public findings surface.

**4.02** All arms in a comparison MUST read the same packet on the same operating day. The packet MUST be hashed and registered; the register of packets MUST be published, and any row naming a packet the register does not cover MUST be reported as a finding.

**4.03** No output of a forecasting run may appear in the input to a subsequent run (the Rueckkopplungsverbot). Model-authored prose from prior runs - judgments, indications, syntheses - MUST be stripped from any report slice before it becomes a packet. An implementation MUST document the stripping rule.

**4.04** Elicitation MUST produce, per row, a statement, a probability, a resolution criterion naming the source of record, a failure condition, and a deadline. Rows that fail structural checks MUST be rejected with a printed reason and MUST NOT be sealed. Rejection rules MAY change between cohorts; a change to a rejection rule changes which rows seal, not how sealed rows were elicited, and MUST be dated.

**4.05** A row's window MUST open no earlier than its arrival; a row whose window opened before its seal is a retrodiction and MUST be rejected.

---

## CHAPTER 5 - CONTROLS

**5.01** For every frontier row sealed, a base-rate control row MUST be composed and sealed in the same run, on the same claim, criterion and deadline. Rows refired after a rejection take no controls and MUST be marked as refires.

**5.02** The control's reference class MUST be composed before any outcome in scope is known, and the composition rule MUST be published. The control's own rows MUST be excluded from its reference class. A reference class that prices one system's rows at another system's historical miss rate is a defect and MUST be reported as a finding, not repaired retroactively (see 9.05).

**5.03** A market-implied control MAY be added where a claim has a traded market; its floor is stated separately (Chapter 8).

**5.04** Controls are arms. Their rows are sealed, scored and printed like any other arm's. A control that shows skill against its own base rate is defective by construction and MUST print as such (9(e)).

---

## CHAPTER 6 - SEALING AND RECORD

**6.01** Rows MUST be sealed into an append-only record with a hash chain; timestamps MUST be UTC; the model string and seal date MUST be pinned on the row.

**6.02** A sealed row MUST never be edited. Corrections MUST be printed as corrections with the superseded value retained on the row (RPAS 5.07). Misses MUST be printed at full size.

**6.03** The record SHOULD be anchored externally on a clock the operator does not control (a transparency log, a public timestamp service, a blockchain timestamp). The state of each anchor MUST be shown as it is - anchored, pending, or drifted - and never as a stale match.

**6.04** The record MUST expose, per row, the fields a stranger needs to re-score it: probability, outcome, arm, cohort hash, seat, determination (if the module is used), deadline, packet identifier.

---

## CHAPTER 7 - ADJUDICATION

**7.01** Resolution MUST be against the source of record the row named. Where a row named only press reporting in a domain that has a machine-readable register, the implementation SHOULD note it; it MAY reject it.

**7.02** Where the operator adjudicates rows its own systems forecast, the conflict MUST be printed on the record, not removed. Mitigation MUST include a blind seat: a verdict seat that sees the statement, the criterion and the failure condition and never the probability or the arm; a held-evidence rule; a clerk check at primary sources; divergences printed.

**7.03** Every resolved row MUST carry its seat. Every result MUST be re-cut by seat and the re-cut published beside the pooled figure.

**7.04** Void is a status. Voids MUST be counted out of every denominator and counted beside it. A void rate per arm MUST be printed.

---

## CHAPTER 8 - PRE-REGISTRATION, FLOORS AND CHECKPOINTS

**8.01** Before an arm's first checkpoint, the implementation MUST publish: the hypotheses to be read, each with a stated prior and a stated falsifier; the estimators, with the code that computes them committed by hash; the floors; the multiplicity policy; the threats stated in advance; and the "seen" disclosure (what data the author had seen when registering).

**8.02** Floors are conventions and MUST be labelled as such, with the power statement that justifies them from the data at registration. The desk's conventions: no confirmatory read before 50 resolved rows within one cohort for the arm (the first checkpoint); interim reads at 30 print with a noise line and are not results; below 10 resolved no skill figure prints at all; per-decile bin floor 5; split floor 20 (H3 module); market floor 30 resolved in market domains (H5).

**8.03** No early stopping. No claim on an interim read. A null at the floor is absence of evidence and MUST be reported as that.

**8.04** Multiplicity MUST be stated. The desk's policy: no correction across hypotheses or arms; each test reported at its stated level with its interval; the only within-hypothesis aggregations are those fixed in the registration (H1's two-of-three bins; H4's one-decile rule).

**8.05** An amendment to a registration MUST be dated, appended, never substituted, and MUST state what it changes and what was seen when it was made. An amendment made after an arm's first checkpoint cannot change that arm's read.

---

## CHAPTER 9 - QUALITY CHECKS AND THE HALT

**9.01** Before any hypothesis is read, the following checks MUST pass. They are outcome-neutral: none depends on how any arm scored.
(a) Mirror completeness: every frontier row in scope has its control row sealed in the same run; gaps listed.
(b) Rubric coverage: 100% of rows in scope carry the cohort hash.
(c) Seat recorded: 100% of resolved rows in scope carry a seat.
(d) Determination coverage (module): 100% of resolved rows in scope carry keyed or keyless; rows resolved without one are keyed by rule and counted.
(e) Control agreement: the base-rate control's skill against the realized base rate of the rows it mirrors has a bootstrap 95% interval that includes zero.
(f) Void rate per arm printed.

**9.01a** Check (e) is not a tautology and MUST NOT be described as one. A control that prices every mirrored row at one constant rate has skill exactly zero only when that rate equals the realized base rate of the mirrored rows; otherwise its skill is negative by the square of the gap divided by the climatological reference, and every bootstrap resample's skill is likewise at or below zero, so the interval's upper bound is set by the resample whose base rate comes nearest the price. The check therefore tests whether the control's reference class predicted the realized rate of the rows in scope, and its power is the bootstrap's: the gap it can detect narrows as n grows, and a gap it cannot yet distinguish from zero is a pass on width, not a verdict that the reference class was right (the desk's Finding 11 is the instance). Implementations MUST state the control's stated rate, the realized rate, and the precision at which the interval is compared with zero. The desk's pinned estimator rounds both bounds to four decimals before the comparison, so a resample base rate within about 0.35 points of the price makes the upper bound read -0.0000 and the check pass; that is a rule of the estimator, printed here, not of the algebra. (Reproduced 2026-09-14 on the Chapter 13 clean fixture, n = 120, realized rate 0.55 exactly: a control priced at 54, 56, 58 or 60 passes on the rounded bound - at 60, skill -0.010, interval [-0.0714, -0.0]; priced at 63 it fails, skill -0.026, interval [-0.1072, -0.0001]; at 65, skill -0.040, interval [-0.135, -0.0012]. Revision 0 described the failure found on 2026-09-07 as a control one rounding away from the realized rate; the gap that fails at this n is several points, not one rounding, and the sentence is corrected here with the superseded text retained in 16.03.)

**9.02** A failed check MUST print with its figure and MUST halt the read. Exit status MUST distinguish a halt from a completed read.

**9.03** The halt stands. Nothing is repaired retroactively; the read re-evaluates on every run; the halt holds until an amendment made before the arm's first checkpoint says otherwise. A registration that makes no such amendment leaves the halt in force for that cohort.

**9.04** A corrected construction of any component that failed a check is a new arm under its own tag, with its own rows, from the date of the correction forward.

**9.05** A defect found by a check MUST be published as a numbered finding with: what the check found, the figure, the mechanism, the consequence for every figure that depends on it, and the fact that nothing was repaired retroactively.

---

## CHAPTER 10 - THE DRIFT TEST

**10.01** The drift test compares two arms that form a version pair (3.05) within one cohort. Both MUST clear the checks of Chapter 9 and the floor of 8.02.

**10.02** Estimators: Brier; base rate; skill against own base rate; the reliability table (mean stated probability against observed frequency per decile). Intervals: bootstrap percentile intervals, 95%, 2,000 resamples of the arm's resolved rows, seed fixed and published (the desk's: 26). The code computing them MUST be committed by hash before the first read (8.01).

**10.03** Drift is declared when, in at least one decile that clears the bin floor on both sides, the two arms' observed frequencies differ by more than the wider of the two 95% intervals. This one-decile rule is the fixed aggregation; it MUST NOT be tightened or loosened after registration.

**10.04** A declared drift MUST be reported as "the measured system changed", with the deciles and the direction, and MUST NOT be reported as improvement or degradation unless a separately registered hypothesis on skill (H2-type) also clears.

**10.05** Silent drift - a change behind a fixed model string - appears as within-arm change over time and MUST be reported as a change the measure cannot attribute, with the confound named: different packets on different days.

**10.06** Frame drift (H6-type): a version pair whose members differ only by frame is tested by 10.03 unchanged. The prior for frame drift SHOULD be stated from the literature (a null on accuracy is the published reference result for persona prompting: Iadisernia and Camassa, arXiv 2511.02458, ICAIF 2025 - 2,368 personas on the ECB Survey of Professional Forecasters task, no measurable forecasting advantage from persona descriptions, and remarkably homogeneous forecasts across diverse prompts).

**10.07** Every drift read MUST state the standard error of a Brier at the floor and the smallest difference the read can resolve, so a null is understood as the read's power, not the systems' sameness.

---

## CHAPTER 11 - REPORTING

**11.01** Every run MUST write one machine-readable report file (JSON) beside any human-readable face, carrying every figure, interval, check result, floor, seat re-cut, void count, correction count and the halt state. **No number may reach a page that is not in that file.**

**11.02** The report MUST name the estimator code's hash, the registration it reads under, the cohort hash, the packet register head, and the seed.

**11.03** Faces (pages) MUST print the noise line under the floors, the keyed/keyless split where the module is used, the DEFECTIVE count on any keyless figure (rows whose priors could not be read), and the seat re-cut.

**11.04** Version pairs MUST be reported side by side, never as a pooled or averaged tile.

**11.05** The report file SHOULD be anchored externally (6.03) and its hash printed on the face.

---

## CHAPTER 12 - CONFORMANCE

**12.01** Three levels, cumulative.
- **Level 1, RECORDING.** Chapters 3, 4, 5, 6 and 11.01-11.04: arms registered with identity fixed; rubric hashed and carried; packets registered; controls mirrored; rows sealed, chained, never edited; a report file per run.
- **Level 2, PRE-REGISTERED.** Level 1 plus Chapters 8, 9 and 10: hypotheses with priors and falsifiers published before the first checkpoint; estimator code hash-committed; floors labelled as conventions with the power statement; checks that halt and halts that stand; the drift test as fixed.
- **Level 3, BLIND.** Level 2 plus Chapter 7 in full and 6.03: a blind adjudication seat, the seat re-cut, and external anchoring of record and reports.

**12.02** A conformance statement MUST list each clause as MET, NOT MET, or NOT APPLICABLE (with the module named), and MUST list every finding the implementation has published against itself (9.05). **An implementation that has published no finding against itself is presumed not to be looking.** The statement MUST be dated and hashed.

**12.03** Conformance is self-declared and verifiable. A verifier checks: that the rubric hash on rows matches a published rubric; that the estimator code hash matches the committed hash; that the report file reproduces from the record with the committed code and seed; that every check in Chapter 9 is recorded with its figure; and that the findings the statement lists exist on a public surface.

**12.04** A conformance claim MUST name the edition and revision of this standard it was made against.

---

## CHAPTER 13 - TEST VECTORS (normative when issued)

**13.01** The reference implementation MUST ship a synthetic record (JSON) and the report file that a conforming implementation MUST reproduce from it, byte for byte on every figure, with the fixed seed. The first vector set (`DRIFT_26_VECTORS`, seven fixtures, built 2026-09-07 by `drift_vectors.py` against the estimator pinned in the registration, LF-SHA-256 fa560fe3...) is normative for Revisions 0 and 1 and reproduces 7 of 7 under the pinned estimator; a one-line change to the estimator's seed fails 7 of 7. Re-verified 7 of 7 on 2026-09-14 from a fresh clone (Linux, Python 3.12) and on the desk (Windows, Python 3.14) at the landing of this revision. The set ships in the desk's repository at the root: `drift_vectors.py` and `DRIFT_26_VECTORS/` (its `index.json` carries the estimator's LF-SHA-256 and every fixture's ledger hash; `verify` runs a given estimator over the stored fixtures and diffs the report field by field). The vectors MUST include:
(i) an arm at the floor with a clean read (all checks pass; H2-type skill interval; reliability table with intervals);
(ii) a version pair in which the one-decile rule declares drift, and one in which it does not;
(iii) a record in which check (e) fails on the control, so a conforming implementation MUST halt with the same figure;
(iv) a record with a mirror gap, so check (a) MUST list it;
(v) a corrected determination, so the superseded value MUST be carried and the correction counted;
(vi) a void, so denominators MUST exclude it and counts MUST include it.

**13.02** A vector set is versioned with the standard. Reproducing the vectors shows that an implementation computes what the reference implementation computes; it pins the reference's behaviour and does not prove the reference's mathematics, which the vectors were generated from. The values become independent of the reference only in the form the Image Biomarker Standardisation Initiative used - reference values validated by agreement across many independent implementations (13.03) - and no second implementation of this standard exists yet. Until one does, the vectors are a fidelity test against one build, said so; the one result in this standard that does not depend on that build is 9.01a, which stands on algebra. (Revision 0 said an implementation that reproduces the vectors computes the standard correctly without trusting the reference build or its author; that overstated, and the superseded sentence is retained in 16.03.)

**13.03** Form and boundary. The form is old and this standard claims none of it: known-answer tests (NIST's Cryptographic Algorithm Validation Program); digital phantoms with consensus reference values so that independent implementations agree (the Image Biomarker Standardisation Initiative - Zwanenburg et al., Radiology 295:328-338, 2020, reference values for 169 radiomics features established across 25 independent implementations computing from one digital phantom; reference manual arXiv 1612.07003); a conformance suite for a statistical protocol (EPC, arXiv 2607.00297, 2026-07-01: a reference test suite with mock evaluators on fixed input sequences, passing which "qualifies an implementation as EPC-v1.0-compatible", beside a versioned reference snapshot and a machine-readable manifest - published weeks before Revision 0). The boundary the desk does not enter: US patent 12,645,555 claims deterministic conformance suites with expected validator outputs and a signed conformance certificate committing to the suite digest and the validator digest, kept in a certificate registry. This standard issues no certificate and keeps no registry: a conformance claim under Chapter 12 is self-declared by the implementer and verifiable by anyone from the vectors and the record. Printed upon discovery (sweep of 2026-09-14; RPAS-26 7.04).

---

## CHAPTER 14 - PRIOR ART BOUNDARY (informative)

**14.01** Occupied, and not claimed here: the Brier score and its decompositions; reliability diagrams; bootstrap intervals; pre-registration and registered reports; cryptographic commitment of rubrics and code by hash; rolling forecasting benchmarks and leaderboards (ForecastBench, arXiv 2409.19839, and its successors); frozen-time replays against contemporaneous market prices (HINDCAST, arXiv 2607.14051); calibration scored against prediction-market prices (Kalshibench, arXiv 2512.16030); the published catalogue of pitfalls in evaluating language-model forecasters (Paleka et al., arXiv 2506.00723), of which this standard's Rueckkopplungsverbot (4.03) and retrodiction gate (4.05) are instances, and the measured leakage of outcomes through date-filtered retrieval (El Lahib et al., arXiv 2602.00758, ACL 2026), which is the hazard 4.05 and 7.02's held-evidence rule guard against; a prespecified, hash-frozen forecasting evaluation with its corrections disclosed (Mohanty, arXiv 2608.20304, 2026-08-20), whose own distinction - hashes establish file identity, not when a plan existed, so the design is hash-frozen rather than preregistered - is exactly the line 6.03 and 8.01 cross by anchoring on a clock the operator does not control; and chance-corrected agreement for machine judges (Norman, Rivera and Hughes, arXiv 2606.19544, 2026-06-17), which is why 7.02's blind seat prints kappa and not raw agreement. Persona and frame effects: 10.06.

**14.02** Claimed, narrowly: **a conformance standard for attributable version comparison** - same-packet paired elicitation under a committed rubric hash, mirrored same-run controls, arm identity that includes access and frame, pre-registered floors and reads with fixed aggregation rules, outcome-neutral quality checks that halt and halts that stand, blind adjudication with a seat re-cut, and a conformance statement that must list the implementation's own published findings.

**14.03** Not located at issuance, and stated as absence rather than novelty: a published, pre-registered, same-packet, frozen-rubric version pair for a language-model forecaster with the read committed before the data cleared its floor. The first such read under this standard is scheduled by the desk's registration for late 2026; its result, whatever it is, is the first test vector of the standard's usefulness. The registration's first confirmatory read (2026-09-09, lmstudio/auto[post-window], n = 96, H2 not supported, Finding 11) is a single-arm read against a base-rate control, not a version-pair read; the desk's first pair (manual/fable-5/unattested and manual/fable-5.1/unattested) stood at 106 and 96 rows within the running cohort on 2026-09-14 with none resolved. Also stated as absence after the sweeps of 2026-09-07 and 2026-09-14: a published pre-registered confirmatory read of a language-model forecasting arm against a same-row base-rate control with the gating checks stated in advance and a failed check printed before the passed one (Findings 10 and 11 together); nearest, arXiv 2608.20304.

---

## CHAPTER 15 - REGULATORY MAPPING (informative; to be confirmed against current texts and counsel)

**15.01** NIST AI RMF (MEASURE function) and NIST's TEVV work: measurement of change across versions under fixed evaluation conditions is the object; this standard supplies procedure for it.

**15.02** EU AI Act: accuracy, robustness and record-keeping obligations for high-risk systems (Articles 9, 12, 15) and post-market monitoring (Article 72): a Level 2 record is a monitoring artefact with a stated method.

**15.03** ISO/IEC 42001 (AI management systems) monitoring and measurement clauses; ISO/IEC 23894 risk guidance: a conformance statement under 12.02 is an auditable monitoring control.

**15.04** Government auditing standards (GAGAS) and audit evidence standards (ISA 500 family): the halt-stands rule and the seat re-cut are evidence-quality controls; the finding discipline (9.05) is the auditor's own workpaper rule turned on the instrument.

---

## CHAPTER 16 - REVISION

**16.01** Revisions are dated and appended; superseded text is retained with its dates; the vector set is versioned with the text. A conformance claim names the revision it was made against.

**16.02** Revision 0 (2026-09-07). Draft. Written from the Kalibrierwarte registered report v3 (Sections 1-14, amendments of 2026-09-02 and 2026-09-03), RPAS-26, KNM-26, KNP-26, Finding 10 and sweep seven. Named DRIFT-26 by the operator the same day. Vector set built the same day against the pinned estimator; clause 9.01a written from what the vectors found. Not issued: the text awaits the operator's rework.

**16.03** Revision 1 (2026-09-14). Draft, served under the desk's draft-publication law (PROVENANCE: DRAFT above). Changes: 3.07 added - a frame revision under one tag, the practice the desk adopted on 2026-09-14 (FRAME2), written as a clause with its boundary; 9.01a corrected - the estimator's four-decimal rounding rule stated, the power of the check stated, and the 2026-09-07 parenthesis replaced by figures reproduced on 2026-09-14 (superseded text: "Found by the Chapter 13 vectors: a control priced at an integer percent one rounding away from the realized rate failed (e) at n = 120 with an interval of [-0.1003, -0.0001]."); 10.06 cites its reference result by artifact; 13.01 records the re-verification of the vector set and its location in the repository; 13.02 corrected (superseded text: "An implementation that reproduces the vectors computes the standard correctly without trusting the reference build or its author."); 13.03 added - the form the vectors take and the boundary the desk does not enter; 14.01 names its occupants by artifact; 14.03 records the first confirmatory read as single-arm and the first pair's count. The vector set is unchanged from Revision 0. Nothing normative changes except 3.07, which records a practice already on the desk's record. Not issued: the text awaits the operator's rework, which replaces it without moving the date.

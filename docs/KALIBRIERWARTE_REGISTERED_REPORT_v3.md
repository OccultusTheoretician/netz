KALIBRIERWARTE. REGISTERED REPORT v3.
Pre-registration. No score is computed or claimed here.

Desk: Retro-Prescient Audit, retroprescientaudit.com. Repo: OccultusTheoretician/netz.
Pinned to remote d12a66d (2026-09-01 02:35Z). Instrument: warte.py, kalibrierwarte/1.0. Data: ledger.json, arms.json.
Anchored on publication (RPAS 4.05). Amendments supersede with retention (RPAS 5.07).

1. STATUS

The Warte is live: one tile per arm, reliability by decile, Brier, base rate, climatological floor, skill, n-floors printed. No pooled figure listed; a Brier belongs to one forecaster. It is a display.

This document makes it a study. Pre-registration is the paper. Hypotheses, rows, estimators, sample floors and the desk's own priors are committed here before the data exist. Same rule as every row on the ledger: criterion sealed before outcome. A registration edited after first look is not a registration. Section 12 governs.

Roles: registrant, operator, adjudication chair and analyst are one party. No independent auditor. Analysis is not blinded. The controls that stand in for independence are the ones in Sections 7, 9 and 10, and the public recompute.

2. QUESTION

Under a frozen elicitation rubric: do frontier model arms differ from each other, from their own earlier versions, and from two control arms, in calibration and in skill. And does the keyed/keyless determination separate two populations of rows that behave differently, as the desk says it does.

3. INSTRUMENT AS BUILT (warte.py, read-only against ledger.json)

Boundary. Pipeline: battle report (record items only; model prose stripped under the Rueckkopplungsverbot) to packet; elicitation under PROJECTION_PROMPT; gate; seal (SHA-256 per row, ledger OTS-anchored); adjudication (operator, or blind jury); warte.py. The Warte reads the sealed ledger and nothing upstream of it.

Reliability: ten deciles of stated probability. Per bin, mean stated probability against observed hit frequency. A bin under 5 resolved prints n<5 and no frequency (N_FLOOR_BIN 5).
Brier: mean squared error, stated probability on [0,1] against outcome 1 or 0, resolved rows only.
Base rate: the arm's own hit frequency over its resolved rows.
Climatological floor: the Brier of a constant forecast at the arm's base rate.
Skill: 1 - Brier/floor. Negative: the constant forecast won.
Arm floor: under 10 resolved, counts only, no skill line (N_FLOOR_ARM 10). Every face on the desk prints "under 30 resolved, this is noise" beside any score.
Era split: eras registered in arms.json score as separate forecasters, never pooled. lmstudio/auto is three: pre-verbot to 2026-07-28, post-verbot to 2026-08-03, post-window from 2026-08-03. Boundaries: the Rueckkopplungsverbot commit and the window fix.
Keyed/keyless: Brier over keyed rows (outcome deducible from the arm's own declared priors: arithmetic) and over keyless rows (foresight), reported separately. The keyless figure carries the count of keyless rows the citation audit marked DEFECTIVE. A keyless call against unreadable priors was made against nothing.
Rubric hash: every row sealed since 2026-08-09 carries the SHA-256 of PROJECTION_PROMPT, placeholders unfilled. Same hash, comparable. Changed hash, new cohort, self-disclosed.

4. ARMS

Identity law: tool access is part of arm identity. Searched, cold and unattested runs of one model are three forecasters. An era boundary is a new forecaster. A row seals only under a registered active tag (arms.json).

Frontier, in scope: manual/fable-5/unattested (claude-fable-5), manual/opus-5/unattested (claude-opus-5), manual/sonnet-5/unattested (claude-sonnet-5). Access unattested. First seal 2026-08-01. The lane runs when the operator runs it: 17 seal-days of 32 to 2026-09-01. Retired predecessors (manual/fable, manual/fable-5, manual/opus-5, manual/sonnet-5; access unknown, rationale on record) keep their own tiles and are the earlier-version comparators for H4. Searched and cold variants of each model: registered, active, zero rows. They enter as their own arms when they seal.

Local: lmstudio/auto (qwen/qwen3-30b-a3b-2507, cold). Three eras.

Controls: control/baserate, climatological. One control row composed and sealed in the same run as each frontier row it mirrors (RPAS 4.06). Refires take no controls. 323 rows at registration. control/market-implied: registered, active, zero rows. H5 binds when it seals.

Out of scope for any capability claim: operator/human (10 rows, own tile), kfk/halflife, fogsim/scenario.

5. COHORTS

A cohort is a rubric hash. Three exist.

Cohort 0, no hash. 403 rows, 2026-07-20 to 2026-08-08. Before the commitment. Descriptive only, marked. Excluded from confirmatory analysis.
Cohort 1, 4ea5ab8f6a401aed. 812 rows, 2026-08-09 to 2026-08-31. Closed. Primary cohort of this registration.
Cohort 2, bbdc779152ddea3a. Opened 2026-09-01 when GATE-2026-08-31 added rule 9 (reference level on market-threshold rows) to the rubric. 10 rows at registration. Running.

Confirmatory analysis runs within a cohort. Cross-cohort is exploratory and labelled. Rule 9 is a disclosure rule and changes no acceptance criterion; that does not matter. The law is the hash.

6. HYPOTHESES

Prior stated with each. Directional tests one-sided in the stated direction. Falsifier stated with each.

H1. Overconfidence at the top. Within a cohort, each frontier arm's observed frequency in the 70-80, 80-90 and 90-100 bins falls below the bin's mean stated probability, upper bound of the bootstrap 95% interval included, in at least two of the three bins that clear the bin floor. Prior: yes, all three arms. Falsifier: the interval reaches or covers the stated mean in two or more of the three.

H2. Skill against own base rate. At an arm's first checkpoint (Section 8), skill is positive and the bootstrap 95% interval excludes zero. Prior: no frontier arm clears it at the first checkpoint. The faces have said "noise" for six weeks; this is what the desk expects when the floor clears. Falsifier of the prior: any frontier arm that clears.

H3. Keyless harder than keyed. For each arm with 20 or more resolved rows in each split within a cohort, keyless Brier exceeds keyed Brier and the bootstrap 95% interval of the difference excludes zero. Prior: yes, every arm. This tests the desk's construct, not only the arms. Keyless at or below keyed for the arms that clear the floor means the determination is not separating arithmetic from foresight. That result prints as a finding against the instrument.

H4. Version drift under a frozen rubric. A version change is a new model string registered in arms.json for the same lane and access; provider-side changes behind a fixed string are not a version change here (Section 10). The successor seals under the same rubric hash as its predecessor. In at least one decile clearing the bin floor on both sides, observed frequencies differ by more than the wider of the two bootstrap 95% intervals. Prior: yes. This is the headline product. Falsifier: no decile differs at that margin. Constraint: same hash on both sides or no test. A version change that lands on a cohort boundary is reported as untestable, not compared across cohorts.

H5. Market control. control/market-implied, at 30 resolved market-domain rows: lower Brier than every frontier arm on the same rows in the same cohort, the bootstrap 95% interval of each difference excluding zero. Prior: yes. If not, that is the finding. (control/baserate is a quality check, Section 7, not a hypothesis.)

7. ESTIMATORS

Brier, base rate, floor, skill and the reliability table: as warte.py computes them today (Section 3). Two additions, implemented in warte_report.py, SHA-256 committed before the first checkpoint runs:
Bootstrap percentile intervals, 95%, 2,000 resamples of the arm's resolved rows, seed 26: Brier, skill, each decile's observed frequency.
Resolved rows by adjudication seat: operator; jury, searched seat adopted; jury, divergence. Every result re-cuts by who adjudicated it.
Voids out of every denominator, counted beside it. Corrected determinations: current value used, superseded value kept on the row, count of corrected rows in scope printed.

Multiplicity. Five hypotheses, three frontier arms, ten bins. No correction across hypotheses or arms. Each test is reported at its stated level with its interval and the reader counts the tests. The two-of-three rule in H1 and the one-decile rule in H4 are the only within-hypothesis aggregations, fixed here.

Quality checks, outcome-neutral. All pass before any hypothesis is read; a failure prints and halts the read.
(a) Mirror completeness: every frontier row in scope has its control row sealed in the same run; gaps listed.
(b) Rubric coverage: 100% of rows in scope carry the cohort hash.
(c) Seat recorded: 100% of resolved rows in scope carry an adjudication seat.
(d) Determination coverage: 100% of resolved rows in scope carry keyed or keyless; rows resolved without one are keyed by rule and counted.
(e) control/baserate skill against its own base rate: bootstrap 95% interval includes zero. By construction. A departure is a defect in the control and prints as one.
(f) Void rate per arm printed.
Outputs: warte_report.py writes forecasts/warte_report_<date>.json beside the face and prints every figure above; no number reaches a page that is not in that file.

8. FLOORS AND CHECKPOINTS

No confirmatory analysis before 50 resolved rows within one cohort for that arm. That is the arm's first checkpoint. Interim reads at 30 print with the noise line and are not results of this registration. No early stopping. No claim on an interim read. H3 floor: 20 per split. H5 market floor: 30 resolved in market domains.

At registration, resolved within cohort 1: opus-5/unattested 2, sonnet-5/unattested 2, fable-5/unattested 1, control/baserate 5, lmstudio/auto 14 (post-window). All-time: 3, 8, 1, 17, 77; the difference is cohort 0. 99 rows past deadline and unadjudicated; 119 come due within seven days. First frontier checkpoint: weeks, not days. Register now.

Floors are conventions, not power calculations. On the 148 resolved rows at registration the per-row squared-error variance is 0.034 (0.050 on the control arm), so at 50 resolved rows the standard error of an arm's Brier is about 0.026 and a Brier difference under about 0.05 will not resolve at the first checkpoint. A null at 50 is absence of evidence and is reported as that.

9. IN AND OUT

In: status hit or miss; rubric hash present; scored on the tag it sealed under. Refires are ordinary rows of their arm. Late-seal, generation-anchored rows (ANCHOR-2026-09-01) are in, class visible on the row. Operator-adjudicated and jury-adjudicated both in; seat recorded per row (Section 7).
Out: void (counted). No rubric hash (cohort 0, descriptive). operator/human, kfk/halflife, fogsim/scenario from any capability claim.

10. THREATS, STATED IN ADVANCE

The desk adjudicates its own rows. Mitigation: blind jury (verdict seat sees claim, criterion and failure condition; never probability, never arm; held-evidence rule; clerk verification at primaries; divergences printed) and the seat re-cut in Section 7. The conflict is printed, not removed.
All arms read the same packet on the same day, so cross-arm comparison is protected. Different packets on different days, so within-arm comparison over time is confounded with input drift; every such comparison says so.
Provider-side model changes behind a fixed model string are invisible to the desk. Pinned: model string per arm (arms.json), seal date per row. Silent drift appears in H4 as within-arm drift over time and is reported as that: a change in the measured system the measure cannot attribute.
The gate is not frozen. Gate patches change which rows seal, not how sealed rows were elicited; the hash covers elicitation only. Gate changes carry dates on the findings page.
Determinations are judgments. Mitigations: correction with retention; DEFECTIVE count on the keyless figure. The independence limitation (an Anthropic model classifying Anthropic arms' rows) is disclosed on the ledger face and stands.
n is small and stays small for months. Nothing claims below the floors. When the floors clear, the test is already on the record.

11. SEEN AND CLAIMED

Seen. The desk's faces have printed per-arm, all-time Brier, base rate, skill and reliability bins for every arm, regenerated daily, for weeks. The registrant has looked at them, including lmstudio/auto at 77 resolved all-time. No interval, no test and no within-cohort split has been computed. The priors in Section 6 were written with those faces in view: for lmstudio/auto they are informed; for the three frontier arms, at 1 to 2 resolved rows each within cohort 1, they are near-blind. Weight them accordingly.

Claimed. Nothing. The counts in Section 8 are the ledger at registration. Noise, by law.

12. AMENDMENTS

Before any checkpoint runs: an amendment is a new dated section appended below this one; amended text stays in place with its date. After the first checkpoint runs for any arm: Sections 6 and 7 are frozen for that arm; any change is a new registration with a new version number, and the old one stands beside it.

Data and code, public: ledger.json, arms.json, warte.py, forecasts/kalibrierwarte_latest.json, cite_integrity_latest.json, docs/findings.html. Every number here recomputes from a clone at d12a66d.

13. AMENDMENT 2026-09-02 - INSTRUMENT PIN, IMPLEMENTATION DECISIONS, SEEN

Appended under Section 12 before any hypothesis has been read for any arm. Sections 6 and 7 stand as written above; this section fixes what Section 7 left to the instrument.

Instrument. warte_report.py, SHA-256 over LF-normalised bytes fa560fe3a58570bb2b4e8b888bf524732691f15b2141502fc75e171532909723, built against remote 7218456 (2026-09-02 11:26Z). The commit that carries this section carries the file and is the pin of record. Runs are report-only by default; --write writes forecasts/warte_report_<date>.json through the run-artifact guard. No flag lowers a floor: under 50 resolved within the cohort an arm gets counts, and from 30 an interim read carrying the noise line that is not a result of this registration.

Bootstrap. The unit of resampling is the resolved row, drawn with replacement, n rows per resample, 2,000 resamples, seed 26 (Python random.Random). Intervals are percentile 2.5 to 97.5 with linear interpolation between order statistics. A decile's interval is taken over the resamples in which the decile is non-empty; that count is printed beside it. The H3 difference (keyless Brier minus keyed Brier) is computed inside the same resamples, over those in which both splits are non-empty. Rows resolved without a determination are keyed by rule (Section 7d) and enter the keyed side of every split.

Seats. The registration names three seats; the ledger records them in each resolved row's audit field. No audit record: operator (hand-ruled through the console or --resolve). audit.mode blind-jury with basis claude: jury, searched seat adopted. audit.mode blind-jury with any other basis: jury, divergence - the operator ruled where the seats diverged or the searched seat returned AMBIGUOUS. Fourteen cohort-0 rows carry the 2026-08-01 single-auditor record (an auditor key, no mode); they are a fourth class, auditor-single, printed as outside the three named here and excluded from confirmatory analysis with the rest of cohort 0.

Mirror pairing, check (a). A control row mirrors the arm row named in control_basis.control_for when that field is present. baserate.py writes it only when pairing from the ledger; the --pair path composes before ids exist, so mirrors composed from an arm file are paired by identical resolution, deadline and source_packet. A mirror sealed more than 360 minutes after its arm row is a late mirror and is listed as a gap. Check (a) binds frontier rows by its own text; for the local arm and the controls the instrument prints coverage and does not gate the read on it. Stated in advance of any frontier checkpoint: frontier rows sealed on 2026-08-20, 2026-08-22 and 2026-08-25 have no same-run mirror, and refires take none by rule (Section 4) while remaining in scope (Section 9), so check (a) as written fails for every frontier arm at its first checkpoint in cohort 1 and, through refires, in any later cohort in which a refired row has resolved.

Ruling 2026-09-02, operator. A failed quality check halts the read and the halt stands. Nothing is repaired retroactively: a mirror composed later is retrodiction and dies, and sealed control rows stand. Every check is re-evaluated at every run as the record accrues; a check that cannot change state on accrual holds its halt until a further amendment under Section 12, made before the arm's first checkpoint, says otherwise. This ruling makes no such amendment.

Seen (Section 11, continued). The instrument was behaviour-tested before this pin, as the desk's patch law requires, by running it on a clone of the public ledger at remote 7218456 (1,274 rows) on 2026-09-02 at about 13:45Z. That run produced descriptive figures with intervals for lmstudio/auto[post-window] in cohort 1 at 62 resolved rows and evaluated the quality checks; check (e) failed within the cohort at 12 resolved control rows and the read halted (Finding 10). No hypothesis was read. No result of this registration exists. The registrant has seen those descriptive figures; any amendment after this line is made with them in view and says so.

14. AMENDMENT 2026-09-03 - A FRAME ARM (lmstudio/realist), H6

Appended under Section 13 before any checkpoint for the arm it registers. Operator-delegated design ("your call", 2026-09-03), recorded here as the registrant's own.

The arm. lmstudio/realist: the same local model as lmstudio/auto (qwen/qwen3-30b-a3b-2507), the same cold access, the same elicitation rubric, fired nightly by the chain on the same packet day, with one difference - a FRAME preamble stating the forecaster's operating assumptions (classical realist balance of power). The frame is part of the arm, not of the rubric: rows seal under the shared rubric_hash and sit in the same cohort as every other arm; each row also carries frame and frame_hash. Frame text SHA-256 7b96df749db5034b43dd8539a201f65361038d3da37cb956c8f70c69e5c666ff; the text is public in kkr.py. The frame adds no model output to any input; the Rueckkopplungsverbot is untouched. The arm carries no control mirrors (Section 7a binds frontier rows; the local arms carry none). It seals its first rows at the first chain run after the commit carrying this section.

H6 - frame drift. Within one cohort, for each decile in which lmstudio/auto[post-window] and lmstudio/realist both clear the bin floor, the observed frequencies differ by more than the wider of the two bootstrap 95% intervals (the H4 test, applied to a frame instead of a version). Prior: not stated - the registrant has no honest expectation of the direction or size of a frame effect and says so rather than inventing one. Floors, checkpoint and quality checks as Section 8 and Section 7 for both arms. H6 is read by a separate instrument pinned by a later amendment, so that warte_report.py's pin (Section 13) stands unchanged.

Banked, not built: the paired design - lmstudio pricing the frontier arms' own claims under the frame, so that every difference is the frame's and no new statement enters adjudication. Its input would carry another run's claim text (never its probability or rationale), which is the jury's information discipline but is forbidden by the letter of the Rueckkopplungsverbot. It is built only on an explicit operator ruling amending that law, recorded in a further dated section.

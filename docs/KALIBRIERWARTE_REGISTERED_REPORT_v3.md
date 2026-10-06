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


15. AMENDMENT 2026-09-14 - CHECK (e) CLARIFIED, THE (e) RE-EVALUATION RECORD, THE H6 REFERENCE RESULT, THE FRAME REVISION, THE H6 INSTRUMENT

AUTHORSHIP - drafted by the desk's assistant under the registrant's direction on 2026-09-14; read in full and adopted by the registrant on 2026-09-14, which replaces the draft banner this section carried from 19:50Z that day without moving the date. Appended under Section 12. Sections 6 and 7 are frozen for lmstudio/auto[post-window] as of its first checkpoint (2026-09-09) and are not touched; this section clarifies a check's reading, records what the check did, records a reference result, revises the frame arm registered in Section 14 and pins its instrument.

15.1 Check (e), clarified (DRIFT-26 9.01a). Check (e) is not a tautology. A control priced at a constant rate has skill exactly zero against its own realized base rate only when the constant equals the realized rate; otherwise, its skill is negative by the squared gap, normalised by the reference, and its interval lies at or below zero. The check therefore tests the reference class from which the control was priced. It can fail at large n on a small gap, and it can pass on interval width at small n while the gap stands. Neither reading changes the check; both are printed.

15.2 The (e) record. On 2026-09-03 the check failed within cohort 4ea5ab8f at 12 resolved control rows (skill -0.335, interval [-2.03, -0.025]) and the read halted (Finding 10; the 2026-09-02 ruling). On 2026-09-09, after the sitting of 2026-09-08, it re-evaluated at 22 resolved control rows (skill -0.133, interval [-0.744, 0.048]) and passed on width, the point estimate unchanged in sign and the Finding 10 construction unchanged. All six checks passing, the first confirmatory read ran for lmstudio/auto[post-window] at n = 96 (Finding 11): Brier 0.193 [0.157, 0.232] against climatological 0.177, skill -0.094 [-0.448, 0.084], H2 NOT SUPPORTED. Sections 6 and 7 froze for that arm at that run. Report forecasts/warte_report_2026-09-09.json, LF-sha16 e769f9d0a562f9c5.

15.3 H6 reference result. Iadisernia and Camassa, "Prompting for Policy: Forecasting Macroeconomic Scenarios with Synthetic LLM Personas" (arXiv 2511.02458, ICAIF 2025): 2,368 personas prompting GPT-4o to replicate the ECB Survey of Professional Forecasters found no measurable forecasting advantage from persona descriptions, and diverse prompts produced remarkably homogeneous forecasts. Section 14 registered H6 without a prior; this is recorded as the reference result the H6 read will be set beside, not as a prediction, and the registrant's stated absence of a prior stands.

15.4 Frame revision (REALIST-DATE). The frame text registered in Section 14 (SHA-256 7b96df749db5034b43dd8539a201f65361038d3da37cb956c8f70c69e5c666ff) elicited, under the local model, the elicitation rubric's illustrative event window verbatim: on 2026-09-14 all 10 rows the arm wrote carried the window 2026-07-21 to 2026-07-24 and died at the gate as retrodiction; the arm's 2026-09-09 run sealed nothing. The plain arm under the same rubric on the same days wrote no such window. The defect is the frame's, not the rubric's, and the rubric is not edited (an edit opens a cohort for every arm). The frame is revised by one sentence naming the packet date through a placeholder the chain fills - "The packet date is {packet_date}. Every event window you write opens on or after that date; the dates inside rule 1 below are illustrations of the form, not today's dates." - hashed unfilled, as the rubric is. The revised text is public in kkr.py (FRAME2-2026-09-14, applied 2026-09-14, remote 0600889) and its SHA-256 is 442300f131b11b7ca106096532293924c3a9c4d20b4adcbde63bd932757efc77. A frame is part of the arm: rows carry frame_hash, so the two versions are separable on the record. Rows sealed under the first frame text (60 as of this amendment, issued 2026-09-04 to 2026-09-13, 0 resolved) are a pre-revision class, printed and outside the H6 population; H6's floors and checkpoint count rows under the revised frame, the first of which the chain writes on 2026-09-15. The arm's tag is unchanged (ruling 2026-09-14, assistant-authored at the operator's delegation). The structural fix - a filled placeholder in rule 1 of the rubric - is banked for the next cohort break.

15.5 H6 instrument. H6 is read by warte_frame.py, LF-normalised SHA-256 b622640764aff818a68f0c4f32dae91e5e50f453a6a5fe4786a6848bbfad8d54, committed at remote 0600889 (2026-09-14). It applies the H4 decile test of Section 6 to lmstudio/auto[post-window] and lmstudio/realist within one cohort under the floors and checks of Sections 7 and 8, on the same bootstrap unit, method and seed as Section 13; it imports warte_report.py (fa560fe3a58570bb...) and redefines nothing, so the two instruments cannot disagree on a figure. Its output before both arms clear their floors is counts and the noise line, not a read (`python warte_frame.py --cohort bbdc7791 --frame-hash 442300f1`). warte_report.py's pin (Section 13) is unchanged.

15.6 The pre-revision class on the descriptive faces (ruling 2026-09-14, assistant-authored at the operator's delegation). The 60 pre-revision rows stay on the Warte tile under the arm's tag: they are sealed rows that will resolve and score, and a descriptive face prints what the record holds. They are to be labelled there as the class, outside the H6 population; the label is an instrument change to warte.py banked to the next patch bundle, and until it lands this section is the disclosure. Nothing about the class enters the H6 read.

Seen (Section 11, continued). At this amendment, the registrant has seen: the Finding 11 read; realist rows 60 sealed (60 under the first frame text, 0 under the revised), 0 resolved; Sonnet-5/unattested 32 resolved in all (22 within cohort 4ea5ab8f, 10 under no rubric hash, 0 within bbdc7791; no cohort at the 30-row interim floor, so the estimator prints counts only for it - Finding 11's parenthesis saying otherwise is corrected on the page this same day); the H4 pair at fable-5 106 and fable-5.1 96 rows within the cohort, 0 resolved. No H6 figure exists.

16. AMENDMENT 2026-10-05 - THE LOCAL SUCCESSION (H4, LOCAL LANE), AN ABLATION TWIN (H7), THE FRAME ON THE SUCCESSOR (H6) AND A FRAME-BY-VERSION INTERACTION (H8)

AUTHORSHIP - drafted by the desk's assistant under the registrant's direction on 2026-10-04; read in full and adopted by the registrant on 2026-10-05.

Appended under Section 12 before any row of the three arms it registers has sealed. Sections 6 and 7 stay frozen for lmstudio/auto[post-window] and are not touched. H4 and H6 are used as written in Sections 6 and 14 (H6 as revised in 15.4). H7 and H8 are new. H6 on the successor, H7 and H8 are read by one instrument, warte_local.py, pinned by a later amendment before the first read point below; it imports warte_report.py and redefines nothing, so warte_report.py's pin (Section 13) and warte_frame.py's (15.5) stand unchanged.

16.1 The arms.

lmstudio/qwen36 - Qwen3.6-35B-A3B, the official weights (Qwen/Qwen3.6-35B-A3B), static GGUF quantization by mradermacher (mradermacher/Qwen3.6-35B-A3B-GGUF), quant Q4_K_S, LM Studio key qwen3.6-35b-a3b, file SHA-256 97cc5853d3c163c9cb81782ffc8ee18d909c67f8a3c6b4816b98f1103125c6c6.

lmstudio/qwen36-abliterated - huihui-ai/Huihui-Qwen3.6-35B-A3B-abliterated, a refusal-direction ablation of the same official weights with no fine-tune, static GGUF quantization by the same quantizer (mradermacher/Huihui-Qwen3.6-35B-A3B-abliterated-GGUF), the same quant, key huihui-qwen3.6-35b-a3b-abliterated, file SHA-256 e3787c675133e7abf4eb328d10791ab539f034f7902481b756a239b8ca09aa20.

lmstudio/qwen36-realist - the same model, key and file as lmstudio/qwen36, under the realist frame in force for lmstudio/realist (15.4: SHA-256 442300f131b11b7ca106096532293924c3a9c4d20b4adcbde63bd932757efc77, hashed unfilled, text public in kkr.py). The frame is part of the arm (Section 14): rows carry frame and frame_hash. The arm runs under its own tag through kkr.py --local-arm, which reads the frame from the arm's own registry entry (FRAMEROUTE-1004), never through the shared frame path, so none of its rows can seal under lmstudio/realist or run that arm's model.

All three cold: no network at inference. All seal under the rubric hash in force (cohort bbdc7791 at this amendment), read the packet of the same day, and are fired by local_arms.py after daily.bat, one model in memory at a time (lmstudio/qwen36 and lmstudio/qwen36-realist share one load). Run conditions are identical for all three and for the incumbents: temperature 0.3, max_tokens 6000, one user message (kkr.py call_lmstudio), reasoning off, just-in-time loading off, context length 32768. Sampling defaults the request does not carry are the incumbent's saved values, copied to both files: top-k 20, top-p 0.8, min-p 0, repeat and presence penalties off; thinking is off in LM Studio's per-model setting. Measured at registration (lm_settings_probe, 2026-10-05T07:51Z): 32768 context and 4 parallel slots applied to all three files and the incumbent; the packet of 2026-10-04 renders to 15,261 prompt tokens on both Qwen3.6 files and 15,048 on the incumbent, leaving 11,507 tokens of headroom for the 6,000-token answer; a plain request returns no reasoning output; every response names the model requested. Each arm's packet is written as kkr_packet_local_<slug>_<stamp>.md and entered in the packet register (PACKETLOCAL-1004). Local arms carry no control mirrors (Section 7a binds frontier rows). Each seals its first rows at the first chain run after the commit carrying this section.

File provenance, read from the two files on the box before registration (gguf_provenance.py, pair mode) and recorded here: architecture, quant, tensor names, shapes and types, tokenizer arrays, embedded chat template, multi-token-prediction tensors, quantizer field - EQUAL on all eight (read 2026-10-05T07:51:35Z): both files are GGUF v3, architecture qwen35moe, Q4_K_S, 733 tensors of identical names, shapes and types (layout SHA-256 3f1b3f86bf521d9cf85a237ff56c66727e4cf23270e623382910642eeca0bbe3), identical tokenizer arrays (tokens SHA-256 8602a5aeb57ffeab205af479d8d776f6d26a87ea71908599b5beef21a9e10001), no multi-token-prediction tensors, and one embedded chat template, byte-identical in both (SHA-256 e84f32a23fdda27689f868aa4a1a5621f41133e51a48d7f3efcbea2839574259), so no template override is set. Neither file sets a quantizer field; the common quantizer rests on the repositories named above. The twin's metadata names Qwen/Qwen3.6-35B-A3B as its base model. A pair that differs as files in anything but weight values is not registered as a single-variable pair: it is re-downloaded, or this section says what differs and H7 is read as a comparison of two files, not of one surgery.

16.2 The local succession is H4, as written. A new model string in the same lane and access is a version change (Section 6, H4). The frontier successions of 2026-09-24 and 2026-09-29 switched clean, so their H4 reads compare different packet days. This one does not: the incumbents run in parallel on the same packets for 21 days after lmstudio/qwen36's first sealed rows (the assistant's ruling under the registrant's delegation, 2026-10-04), so the decile comparison is same-packet. Population: rows of lmstudio/auto[post-window] and lmstudio/qwen36 issued on packet days on which both sealed, within one cohort, under one gate (16.7). Floors, checkpoint and quality checks: Sections 7 and 8. Prior: H4's, yes. The incumbents retire at the end of the overlap; their open rows keep resolving and the read waits for both sides' floors.

16.3 H6 on the successor. H6 as written (Section 14, 15.4), applied to lmstudio/qwen36 and lmstudio/qwen36-realist within one cohort, with H6's floors, checkpoint and quality checks. Prior: not stated, as in Section 14; the reference result of 15.3 stands beside it. H6 on the incumbents (lmstudio/auto[post-window], lmstudio/realist) is untouched and reads on the rows already sealed and those sealed before retirement.

16.4 Reference results for the twin (RPAS 7.04), cited before the hypotheses they inform.
(a) Aleksander Fafuła, "Abliteration Is Not a Scalpel: Off-Target Effects of Refusal Removal on Decision Disposition Across Model Families," arXiv 2607.17427 (2026-07-19). On a decision task that drew no refusals, Qwen3-30B-A3B-Instruct-2507 - this desk's incumbent local model - and huihui-ai's ablation of it differed in disposition: the ablated arm bet the upside more often, rated itself more confident and used fewer uncertainty words, with instruction-following unchanged. The same surgery moved another family's confidence the other way. An earlier pilot's headline was traced to a mismatched-quantizer pair, and a stale chat template in a community checkpoint was caught by checking the rendered prompt; 16.1 and 16.8 carry both lessons.
(b) Anthony Sicilia and Malihe Alikhani, "Eliciting Uncertainty in Chain-of-Thought to Mitigate Bias against Forecasting Harmful User Behaviors," arXiv 2410.14744 (2024): across open-source models forecasting conversations for social-media moderation, models were biased against predicting the harmful outcome, which the authors attribute to alignment.
H7a's prior is drawn from (a), H7b's from (b). The mapping from (a)'s self-rated confidence to a forecast's distance from 0.5, and from (b)'s conversational harm to violence and conflict claims about the world, is the registrant's, not the references'. The twin here is a later generation of the incumbent's family, so H7a tests whether (a)'s direction carries within the family, which the reference did not test.

16.5 H7 - ablation drift. The comparison is lmstudio/qwen36-abliterated against lmstudio/qwen36. Conflict rows are rows whose domain resolves, through domains.json as committed with this section (SHA-256 1896f80732811642388c2f5d9a0328661c179ebe59398606c07c331b13ed81ba), to military or crime-security; other rows are the rest. p is the sealed probability divided by 100. Every interval below is a bootstrap 95% percentile interval with linear interpolation, 2,000 resamples, seed 26, resampling packet days (all of both arms' rows on a drawn day), because the two arms write their own rows from one packet and the day is what they share (Section 13's method, the day as unit).

H7a, directional, read without resolution. An arm's sharpness on a packet day is the mean of |p - 0.5| over the rows it sealed that day. Statistic: the mean over in-scope days of the twin's day sharpness minus the stock arm's. One read, on the first chain day on which 21 in-scope days exist; counts only before it. Supported: the interval lies above zero. Not supported: the interval includes zero or lies below it. Prior: yes (16.4a).

H7b, directional, the domain test, read without resolution. With Dc the twin's mean p minus the stock arm's mean p over conflict rows, and Do the same over other rows, the statistic is Dc - Do. One read, on the first chain day on which 21 in-scope days exist and each arm has at least 30 sealed conflict rows and 30 other rows in scope; counts only before it, the counts printed daily. Supported: the interval lies above zero - the twin prices conflict claims higher than the stock arm does, beyond any shift it shows elsewhere. Not supported: the interval includes zero or lies below it. Prior: yes (16.4b).

H7c, the reading, at the first checkpoint of both arms (50 resolved rows within the cohort each, Section 8). Five components, each the twin minus the stock arm with its interval:
(i) conflict share - the share of an arm's sealed rows that are conflict rows;
(ii) sharpness outside the conflict set;
(iii) discrimination - the area under the ROC curve on each arm's resolved rows (the probability that a HIT row carried a higher p than a MISS row, ties half), resampled by row within each arm independently;
(iv) gate acceptance - accepted over accepted plus rejected per run, with runs that produced no parseable output counted as runs with nothing accepted, from forecasts/local_runs.jsonl;
(v) location outside the conflict set - the signed mean p shift, so that optimism is read apart from calibration.
Printed beside them, descriptive: each arm's Brier score split into reliability and resolution over its resolved rows.

The reading table, fixed now:
refusal effect - H7b supported, or (i) excludes zero with the twin writing more conflict rows;
disposition effect - (ii) or (v) excludes zero while (iii) and (iv) include zero;
capability cost - (iii) excludes zero in the twin's disfavour, or (iv) does.
The readings are not exclusive; any other combination prints as mixed, component by component, and no reading is chosen after the figures exist. Only the numeric probability is scored; the wording of a row's rationale is not read for confidence.

16.6 H8 - frame by version. During the overlap the desk runs both models plain and framed on the same packets: lmstudio/auto, lmstudio/realist, lmstudio/qwen36, lmstudio/qwen36-realist. In-scope days: overlap days on which all four arms sealed and every check of 16.8 passed. For each such day, with A(arm) an arm's day statistic, the interaction is D = [A(qwen36-realist) - A(qwen36)] - [A(realist) - A(auto)]. Two statistics, each with a bootstrap 95% interval over days (2,000 resamples, seed 26):
H8a, location: A is the mean sealed probability p of the arm's rows that day;
H8b, sharpness: A is the mean of |p - 0.5|.
Two-sided. One read, at the end of the overlap; counts before it. The frame effect on each model (the bracketed terms) prints beside D with its own interval. Prior: not stated - the registrant has no honest expectation of the direction of an interaction; the reference result of 15.3 (persona descriptions bought no forecasting advantage and homogenised forecasts) implies frame effects near zero on both models and so D near zero. Disclosed: the location statistic was chosen with lmstudio/realist's interim pricing in view (Seen, below). Resolution-based interaction (deciles, Brier) inside a 21-day window is underpowered by construction and is exploratory, labelled, if printed at all.

16.7 The gate correction, and what is in. The desk's audit of 2026-10-04 found that the generate path ran the gate before stamping a row's source report, so the citation rules never fired for locally generated rows: on replay, 117 of the 374 local rows sealed from 2026-09-01 fail them (48 lmstudio/auto, 69 lmstudio/realist); frontier rows, none. The correction (GENGATE-1004) lands before any arm in this section seals. Under Section 10 a gate change alters which rows seal, not how they were elicited: no cohort opens, no era is declared, and the change is dated on the findings page. Every comparison in 16.2 to 16.6 takes rows sealed under the corrected gate only, from 2026-10-04 (commit c1abde0). Rows of the incumbent arms sealed before it stay in scope for the reads already registered for them; the first confirmatory read (15.2) ran on such rows, stands as read, and the class is printed beside it.

16.8 Quality checks for the arms of this section, outcome-neutral. A packet day enters scope only when all of these pass; a failing day prints with its reason and is counted out.
(g) Rendering parity: lmstudio/qwen36 and lmstudio/qwen36-abliterated read one packet (the packet register carries one digest for both that day) and their prompt_tokens in forecasts/local_runs.jsonl are equal. One packet rendered through two chat templates is two inputs.
(g') Frame constancy: within each model, the framed arm's prompt_tokens minus the plain arm's are the same on every in-scope day.
(h) Binding: every run's response_model equals the arm's registered key; a BINDING MISMATCH line takes the run out.
(i) Gate parity: all runs that day carry the same gate digest (kkr.py LF-sha16 in the run log).
(j) No reasoning output: think_block and reasoning_content are false for every run.
(k) Every arm the statistic needs sealed at least one row that day. A day on which an arm sealed nothing is out of H7a, H7b and H8 and stays in H7c (iv), where a run that seals nothing is the datum.

16.9 Inputs. Every arm's packet carries the war desk, translated by a local model. From the correction's publish (INPUTBIND-1004), the input side runs the model arms.json registers for lmstudio/auto - the incumbent, through the overlap. At the incumbent's retirement the input model moves by a dated ruling; that date is an input-condition boundary for every arm (Section 10: within-arm comparison over time is confounded with input drift), printed on the findings page the day it happens.

16.10 Retirement and the frame arm (ruling 2026-10-04, assistant-authored at the registrant's delegation, "whatever is best for dissertation etc"). lmstudio/qwen36-realist is registered with the successor so that the overlap is a same-packet two-by-two of model version and frame (16.6). lmstudio/auto and lmstudio/realist retire together 21 days after lmstudio/qwen36's first sealed rows. Retirement closes an arm to new rows only; open rows keep resolving and keep counting toward every floor, H6 on the incumbents included.

16.11 Claimed, and banked. Claimed: nothing wider than the comparisons on this ledger - one ablation recipe (huihui-ai's) on one model. Banked, not built: a second ablation recipe or author on the same base model as a robustness arm (the reference's own stated limitation); a refusal battery run apart from the forecasting task as a behavioural label check (16.1's file provenance and 16.8 (h) are the label checks in force); a realist frame on the twin (a frame-by-ablation cell); cross-pricing of one arm's claims by another (forbidden by the letter of the Rueckkopplungsverbot; Section 14).

Seen (Section 11, continued). At this amendment the registrant has seen: the incumbents' figures (lmstudio/auto 222 resolved all-time, Brier 0.206; lmstudio/realist 34 resolved all-time, Brier 0.383; within cohort bbdc7791, lmstudio/auto 18 resolved and lmstudio/realist under the revised frame 13 resolved, 11 of them hits); the description on record that the realist arm prices low claims that land most of the time; the first paired read of 2026-10-04; the audit's citation-gate replay; the 2026-10-04 research pass and frontier sweep (16.4's references among them). No row of any new arm exists, and nothing of either new model's behaviour on this desk has been observed.

16.12 AMENDMENT 2026-10-06 - THE OVERLAP DATES AND A SELECTION COMPANION

AUTHORSHIP - drafted by the desk's assistant under the registrant's direction on 2026-10-05; read in full and adopted by the registrant on 2026-10-06.

Appended under Section 12 before any read point of Section 16. Nothing registered in Section 16 changes.

(a) lmstudio/qwen36 sealed its first rows on 2026-10-05. The overlap of 16.2 and 16.6 therefore runs 2026-10-05 to 2026-10-25, and lmstudio/auto and lmstudio/realist retire from 2026-10-26 (16.10).

(b) On 2026-10-05, the first day under the corrected gate, every local arm lost half or more of its generated rows at the gate (lmstudio/qwen36 8 of 10, lmstudio/qwen36-abliterated 5 of 10). Every statistic of 16.5 and 16.6 is computed on sealed rows, so a difference between two arms could be the gate's selection rather than the arms' disposition. From the first chain run after this amendment, forecasts/local_runs.jsonl records every generated row's probability, domain and gate verdict (GENLOG-1005). Beside H7a, H7b and H8 the instrument prints the same statistic computed on all generated rows, accepted and rejected, over the days that carry the record. The companion is printed, never read as a test: it shows whether a sealed-row result survives the removal of the gate's selection. Generated rows before that run are not recorded.

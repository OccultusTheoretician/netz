KALIBRIERWARTE. REGISTERED REPORT v4.
Pre-registration. No score is computed or claimed here.

PROVENANCE - DRAFT. Drafted by the desk's assistant on 2026-10-26 under the registrant's ruling of that day ("draft v4, fixed control"). The registrant gave his priors and his three rulings on 2026-10-27; they are written in below as his. It is his only after he has read it in full and adopted it; until a commit carries it with the adoption line at the foot, nothing here is in force and no row is in its population.

Desk: Retro-Prescient Audit, retroprescientaudit.com. Repo: OccultusTheoretician/netz. Drafted against remote 1902566 (2026-10-26 23:22Z). Anchored on publication (RPAS 4.05). Amendments supersede with retention (RPAS 5.07). Registered report v3 stands beside this one, unedited (v3 Section 12).

1. STATUS

v3's check (e) fails in both of its cohorts. The defect is the control's, named in Finding 10 and measured in Finding 17: control/baserate prices a row at a rate that is not the realized rate of the rows it mirrors. Under the ruling of 2026-09-02 a failed check halts the read and the halt stands, so no confirmatory read under v3 can run for any arm, and manual/fable-5.1/unattested reached its first checkpoint on 2026-10-12 with nothing to read it against. v3 Section 12 makes any change after a checkpoint a new registration. This is that registration.

It does three things. It registers a control priced from the history of the arm it mirrors (Section 3). It names operator/cold, which the arms registry holds out of every capability claim "until a registration names the arm" (Section 5). And it tests each arm against its own paired control, on the same claims, sealed in the same run (Section 7).

Roles, as v3: registrant, operator, adjudication chair and analyst are one party. No independent auditor. Analysis is not blinded. One forecaster in scope is the registrant himself; Sections 5 and 10 are written for that.

2. QUESTION

Does each forecaster in scope beat a climatological forecaster that knows that forecaster's own past, on the same claims, priced and sealed in the same run? Is each calibrated at the top of its range? And does the operator, writing cold, beat the frontier lane on that measure?

3. THE CONTROL, FIXED (control/trailing)

The defect, measured. In cohort bbdc7791, 312 control/baserate rows have resolved and 181 were hits. By domain, the rate the control priced against the rate its own rows realized: cyber 29.7 against 49.4 (77 rows); economics 25.2 against 69.7 (66); military 55.9 against 70.0 (60); political 37.6 against 52.2 (46); disaster 34.3 against 48.9 (45); crime-security 30.8 against 50.0 (18). baserate.py takes its rate from every resolved row in the domain, every arm, all time. The rows it mirrors are frontier claims, which come true far more often than the ledger at large. The control is climatological for the ledger, not for the forecaster it stands beside, and check (e) caught that (v3 15.1).

The new arm. control/trailing prices each mirror at the realized hit rate of the mirrored arm's own resolved rows, counting only rows resolved on or before the packet date, by the first step of this ladder that has at least 10 rows:
  1. the mirrored arm, the row's canonical domain;
  2. the mirrored arm, all domains;
  3. every arm in scope (Section 4), the row's canonical domain;
  4. every arm in scope, all domains.
History before v4 counts as history: a price may use any row resolved before its packet date, whatever registration that row belongs to. Nothing resolved after the packet date enters. The step taken, the rate, the n behind it and the history cut are written on the row (control_basis). Clamped to the gate's 5-95 band, clamping recorded. Composed and sealed in the same run as the row it mirrors (RPAS 4.06), through the same gate; a mirror the gate kills is a finding about the row.

It is still a climatological forecaster: one number per arm and domain, the same for every claim in it. It is the floor an arm must clear, priced from the arm's own record so the floor is the right height.

control/baserate. Retired from the adoption date (registrant's ruling, 2026-10-27). Its rows stand and score under its tag, its tile stands, and it mirrors nothing after the adoption date. Running both would double the control rows, and the old one serves no read.

Build, before the first v4 lane: baserate.py gains the trailing method; arms.json registers control/trailing; the lane block pairs every in-scope arm file with it. Each lands as a dated patch.

4. ARMS IN SCOPE

manual/fable-5.1/unattested and manual/opus-5.5/unattested: the frontier lane since LANE-1026 (2026-10-26). Access unattested, as registered.
operator/cold: registered in arms.json 2026-09-17, active, no rows. Named here; Section 5 is its protocol.
control/trailing: the paired control (Section 3).
operator/advised: in scope under the same sections when it seals (registrant's ruling, 2026-10-27); scored apart from operator/cold by law (a Brier belongs to one forecaster; the model is part of this one); not compared with operator/cold under V3.

Out: the local arms (their reads continue under v3 Section 16 and 16.13); control/baserate; every retired arm; operator/human; kfk/halflife; fogsim/scenario.

5. THE COLD PROTOCOL (operator/cold)

This section is the arm's identity. A row written any other way is not an operator/cold row.

What a row is. Statement, probability, resolution criterion, failure condition, deadline and citations to the day's battle report items, in the operator's own words, with no model evidence, base rate, draft or worksheet before the commit. The gate is the only reader before the seal. The packet, the gate, the window rules, the citation rules and the seal deadline (1800 local, before the UTC day rolls) are the frontier lane's.

Order of the day. The cold file is written from the day's packet and arrives (arrive.py, anchor_log.json) before any frontier file of the same packet arrives. A file that arrives after a frontier file of its packet does not seal under operator/cold. The lane block checks the order before ingest and prints it.

Exposure, stated. The operator runs the desk. He has seen, and will keep seeing, the public ledger: every earlier model row, every face, every finding. That is a standing condition of this arm, disclosed here once, not a breach. Within a packet day, the order rule holds.

Volume. No minimum per sitting. At most 10 rows per packet day (registrant's ruling, 2026-10-27). A missed sitting is a coverage gap, never backfilled from a later packet (the registry's cadence note).

Determinations. The operator records keyed or keyless for his own rows as for any arm. His keyless claims on his own rows are printed as self-claimed beside the keyless figure.

Adjudication. An operator/cold row resolves through the blind jury or the mechanical adjudicator with its evidence cited (KNP-26 6.04: where the committer adjudicates his own entries the basis must be mechanical and evidence cited). A cold row the operator rules by hand stays in the record, prints as its own seat class, and is out of every confirmatory read.

6. POPULATION AND COHORT

v4's population: rows of the arms in scope sealed at or after the commit that carries this registration's adoption. Rows sealed before it belong to v3 alone and are never read here as results; they enter v4 only as history behind the control's prices.

Cohort, as v3 Section 5: a rubric hash. v4 opens inside bbdc7791. A rubric change opens a new cohort; confirmatory analysis runs within one.

A pair is an arm row and its control/trailing mirror sealed in the same run. A pair enters when both rows have resolved hit or miss. A void on either side takes the pair out, counted beside every denominator.

7. HYPOTHESES

Directional tests one-sided in the stated direction, except V3 (below). A prior and a falsifier with each. The priors are the registrant's, given on 2026-10-27 before adoption and before any v4 row exists.

V1. Paired skill. For each arm in scope, at its first v4 checkpoint: the arm's Brier minus its mirrors' Brier, over its resolved pairs, is below zero, and the bootstrap 95% interval of the difference excludes zero. Falsifier: the interval reaches zero.
  Prior, manual/fable-5.1/unattested: yes.
  Prior, manual/opus-5.5/unattested: yes.
  Prior, operator/cold: no.

V2. Overconfidence at the top. v3's H1 on v4's population: each arm's observed frequency in the 70-80, 80-90 and 90-100 bins falls below the bin's mean stated probability, the upper bound of the bootstrap 95% interval included, in at least two of the three bins that clear the bin floor. Falsifier: the interval reaches or covers the stated mean in two or more of the three.
  Prior, manual/fable-5.1/unattested: no.
  Prior, manual/opus-5.5/unattested: no.
  Prior, operator/cold: yes.

V3. The operator against the lane. Once operator/cold and a frontier arm have both reached their first v4 checkpoints: the operator's V1 difference minus that arm's V1 difference, both arms' pairs resampled independently inside each resample, has a bootstrap 95% interval that excludes zero, read two-sided because no direction is registered. One test per frontier arm. Each forecaster is measured against its own climatology on its own claims; this is not a same-claims test, and every print of it says so.
  Prior: not stated. The registrant registers V3 without a direction, as v3 Section 14 registered H6, rather than invent one.

Multiplicity, as v3 Section 7: no correction across hypotheses or arms. Each test is reported at its stated level with its interval, and the reader counts the tests.

8. ESTIMATORS, CHECKS, INSTRUMENT

Brier, reliability bins and floors as v3 Sections 3 and 7. Intervals by bootstrap as v3 Section 13 (2,000 resamples, seed 26, percentile 2.5 to 97.5 with linear interpolation), with one change of unit: V1 and V3 resample pairs, not rows, so each arm row travels with its mirror. Seats, voids and corrected determinations as v3 Sections 7 and 13.

Quality checks, outcome-neutral. All pass before any hypothesis is read; a failure prints and halts the read, and under the ruling of 2026-09-02 the halt stands.
(a) Pairing: every in-scope arm row has its control/trailing mirror sealed in the same run. Gaps listed.
(b) Rubric coverage: every row in scope carries the cohort hash.
(c) Seats: every resolved row carries a seat; no operator/cold row in the read population carries the operator's hand seat (counted).
(d) Determination coverage: every resolved row carries keyed or keyless; rows resolved without one are keyed by rule and counted.
(e') Control calibration: within each arm's pairs, the control's mean priced probability minus its realized hit frequency has a bootstrap 95% interval that includes zero. This is the test v3 15.1 says check (e) was making: whether the reference class the control was priced from is the right one. A trailing rate can lag an arm whose hit rate moves; a failure prints as that.
(f) Void rate per arm printed.
(g) Cold order: every operator/cold row in scope came from a file that arrived before any frontier file of its packet. Rows failing it are out, listed.

Instrument. warte_v4.py, written after adoption and pinned by a dated amendment (its LF SHA-256 in the commit that carries it) before any v4 checkpoint runs. It reads ledger.json and arms.json only, follows warte_report.py's conventions and redefines none of them, and writes forecasts/warte_v4_<date>.json. No number reaches a page that is not in that file.

9. FLOORS AND CHECKPOINTS

An arm's first v4 checkpoint is 50 resolved pairs in v4's population, within one cohort. No confirmatory read before it. Interim reads at 30 print with the noise line and are not results. No early stopping; no claim on an interim read. V3 waits for both of its arms.

Floors are conventions, not power. A pair's difference has less variance than an arm's Brier alone, since a claim's difficulty is shared by both rows, but a small edge will not resolve at 50 pairs. A null at 50 is absence of evidence and prints as that.

At the frontier lane's pace (about ten rows a day per arm) and its resolution lag, the frontier checkpoints are weeks out. The operator's depends on how often he sits.

10. THREATS, STATED IN ADVANCE

The operator is a forecaster here, and also wrote the gate, the packet pipeline, this registration and the instrument that will read him. Mitigations: the cold protocol's order rule, the seat rule in Section 5, the public recompute, and priors written before adoption. The conflict is printed, not removed.

The claims differ across arms. V3 compares each forecaster against its own climatology; the trailing control absorbs difficulty only to the extent an arm's domain rate predicts it.

The control learns from the arm's own past. An arm that improves or decays makes its control lag; check (e') sees the lag in calibration, and V1 reads skill against the lagged rate. Stated, not corrected.

The desk adjudicates its own rows, with the blind jury and the seat re-cut as in v3 Section 10. For operator/cold, Section 5's seat rule is stricter.

The gate is not frozen. GATE-1026 (registered venues, the geography abstention, the quorum reading) and any later change alter which rows seal, not how they were written; changes are dated on the findings page.

Provider-side changes behind a fixed model string remain invisible (v3 Section 10).

11. SEEN AND CLAIMED

Seen. Everything v3 Section 11 and its amendments record as seen. The faces as of 2026-10-26. Findings 10, 11, 13 and 17. For this draft the assistant computed, and the registrant has now seen: the control's priced and realized rates by domain in Section 3; in cohort bbdc7791, manual/fable-5.1/unattested 447 sealed, 107 resolved, 61 hits; manual/opus-5.5/unattested 276 sealed, 14 resolved, 8 hits; manual/sonnet-5.5/unattested (retired 2026-10-26) 222 sealed, 15 resolved, 10 hits; and the three frontier arms' realized rates by domain, pooled: cyber 59% of 34, economics/markets 68% of 25, disaster 54% of 24, military/conflict 70% of 23, political 44% of 18, crime/security 25% of 8. No v4 figure exists. operator/cold has no row.

Claimed. Nothing.

12. AMENDMENTS

As v3 Section 12, per arm: before an arm's first v4 checkpoint runs, an amendment is a dated section appended below; amended text stays in place with its date. After it runs, Sections 7 and 8 are frozen for that arm, and a change is a new registration beside this one.

13. RELATION TO v3

v3 stands. Its halted reads stay halted, and its population ends where v4's begins for every arm both name. manual/fable-5.1/unattested's v3 checkpoint of 2026-10-12 stays unread under the 2026-09-02 ruling. Nothing in v4 re-reads a v3 row as a result.

ADOPTION

Priors and rulings: given by the registrant on 2026-10-27 and written in above.
Adoption: drafted by the desk's assistant under the registrant's direction on 2026-10-26; read in full and adopted by the registrant on 2026-10-27, by his ruling in the session of that day (the option "Adopt today (read in full)"). In force from the commit that carries this line.
Built in the same commit (V4ADOPT-1027, Section 3): baserate.py gains --method trailing; arms.json registers control/trailing and retires control/baserate; the lane pairs each in-scope arm's sealed rows with control/trailing through --from-ledger, so every mirror carries the id of the row it controls; this text joins the anchoring targets (RPAS 4.05); the Warte face names v4 beside v3. warte_v4.py follows by a dated amendment (Section 8).
Seen between the draft and the adoption: what the desk published on 2026-10-27 before the adoption commit, all of it under v3. No v4 figure exists.

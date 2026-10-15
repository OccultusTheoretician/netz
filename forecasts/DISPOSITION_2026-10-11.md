# DISPOSITION - sitting of 2026-10-11, with the resit of 2026-10-12 and the validation of 2026-10-13

PROVENANCE: DRAFT. Drafted by the desk's assistant under the operator's direction from the console trails of 2026-10-11 to 2026-10-13 (DECC-26). The rulings are the operator's and are dated below; the prose is the instrument's and becomes the operator's only after his rework pass.

## 1. Docket and seats

- Docket: forecasts/audit_packet_2026-10-11.md, 566 open rows past deadline. Adjudication prompt sha256 d5b4fff5dfc1e0dd...
- Keys pass, run before the sitting: 5 rows keyed (keys_worksheet_2026-10-11_proposed.json).
- Mechanical adjudicator: held readings for 44 rows (held_evidence_2026-10-11.json).
- Juror B: qwen/qwen3-30b-a3b-2507, local, no search, packet only. 566 verdicts.
- Juror A: a Claude model in an incognito chat outside the project, web search on, connectors off; the operator's words limited to the file request and "Continue". 415 unique claims, fanned out to 566 rows.
- Verdicts rendered packet-only; only kkr.py writes a ruling; every ruling keyed by the operator at the console, by row id.

## 2. The walks

| pass | date | rows walked | ruled | HIT | MISS | skipped | agreement |
|---|---|---|---|---|---|---|---|
| sitting | 2026-10-11 | 566 | 215 | 115 | 100 | rest | 187 concordant, kappa +0.086; 3 seat-B verdicts coerced to ABSTAIN (held-evidence rule) |
| resit | 2026-10-12 | 154 | 83 | 25 | 58 | 71 | 30 concordant, all ABSTAIN pairs; kappa +0.000 is structural (seat B cold on unheld rows) |

The resit covered the 115 claims (153 rows) that juror A's first part never researched, plus KKR-20260822-26. Its walk matched its disposition sheet exactly: 0 mismatches.

Net ledger effect of the sitting, its corrections and its validation: HIT 375 -> 516, MISS 353 -> 509.

## 3. Corrections (RPAS-26 5.07; superseded values retained on every row)

- KKR-20260822-15, 2026-10-11: MISS -> open. A keying error at the console. Re-ruled MISS at the resit on juror A's sourced evidence.
- KKR-20260822-11, 2026-10-11: basis replaced. The keyed note was a stray keystroke; the basis is now the Peru ComCat query.
- KKR-20260822-39, 2026-10-12: basis replaced. Keyed with an empty note, so the basis on record had been juror A's AMBIGUOUS narrative; the basis is now the re-fetched ComCat query, 0 events.
- KKR-20260917-07, 2026-10-13: basis replaced. The keyed basis, a 300 km circle around us7000ti1p, did not reach the eastern Fox Islands. That basis was the assistant's. The basis is now a box query over the whole Fox Islands at M6.5, 0 events. The MISS stands.
- KKR-20260915-13, 2026-10-13: MISS -> HIT. See section 5.

## 4. Re-checks

Every USGS window was re-run through its last day (section 6). All 8 earlier MISS bases returned 0 events and stand. The Sarangani query (100 km, M5.0, 2026-08-06..09-04) returned 2 events (M5.3 on 08-13, M5.2 on 09-01): KKR-20260806-15 and -0806-30 ruled HIT.

## 5. Rule, then validate (operator ruling of 2026-10-12)

The resit adopted 22 MISS verdicts on juror A alone where the juror named no source. The disposition sheet, which was the assistant's, held source-free HITs back but let source-free MISSes through; that asymmetry is a finding.

The operator ruled that the 22 stand and are validated after the fact by search. From the sitting of 2026-10-18, HIT and MISS are treated alike: a dated adoption on juror A alone is permitted, a named source is not required at ruling, and every adoption without one is validated afterwards. A validation is a dated entry beside the ruling (resolution_validated, validation_sources, validation_authority); status and notes are untouched unless the validation contradicts the ruling.

Validation run of 2026-10-13: packet VALIDATE_2026-10-13.md, 19 claims covering the 22 rows, blind to the ruling, an incognito juror with web search, every verdict required to name a source with URL and date.

- 18 claims (21 rows) agree with the MISS and name sources: validation entries written.
- 1 disagrees: KKR-20260915-13 (a U.S. military statement confirming weapons deployed in space, 2026-09-15..09-22). The US acknowledged on-orbit weapons on 15-16 September (National Defense Magazine, Al Jazeera, NPR). Ruled HIT by the operator and corrected.

First measured error rate for source-free adoption: 1 in 22.

## 6. Instrument findings and their patches

| finding | effect on this sitting | patch, live 2026-10-13 |
|---|---|---|
| The adjudicator used a default epicentre (Uto, 32.69 / 130.66) when a row gave no coordinates | 11 held readings measured the wrong place | USGSFIX-1013, mechanical_adjudicator.py: no default; the row falls to the event-id branch or stays unmapped |
| FDSN reads a bare endtime as 00:00 of that day | every USGS window ran one day short | USGSFIX-1013, resolvers.py: the query runs through the window's last day |
| Seat B attached another row's held reading to a row (KKR-20260804-61 carried the USGS reading of -0806-05/-20) | caught only because that row was unheld | HELDMATCH-1013, kkr.py: a seat-B verdict naming an event id or CVE not in its own row is coerced to ABSTAIN |
| The KEV matcher required a name as one contiguous run | KKR-20260906-16 and -43 (NetScaler) missed; ruled HIT on catalog CVE-2026-19490, -88772, -88771 | KEVMATCH-1013, resolvers.py: every word of the name must appear in the entry; chrome reads as chromium |
| The Juror A splitter carried a fixed date | the first split read the previous week's packet | JAPARTS-1013, jury_a_parts.py (local tool): the date follows --packet |
| The publish beacon posted a pooled Brier across all arms (RPAS 5.04) | a pooled score on a public surface at every publish | BRIER-1013, syndicate.py: the pooled figure is no longer posted; per-arm Briers stay on the ledger face |

Every patch was hash-gated on the file it changed, report-only by default, bench-run in a fresh clone, checked by post-assertions, and idempotent.

## 7. Process notes

- Juror A's first part was sent without a "Continue": 109 rows came back as placeholder ABSTAINs. That gap is what the resit covered.
- Incognito chats return text only; each reply was saved by hand. The resit reply came in its own schema and was mapped field for field (projection_id -> id, rationale -> evidence, key_sources -> sources named), content verbatim.
- The resit chat was not saved.
- The validation reply carried inline citation tags, stripped before parsing.
- desk_lookup quake: --to is exclusive; a window ending on day D is queried with --to D+1.

## 8. Ledger at the close of the sitting

Remote HEAD 305d4a2, 2026-10-13 19:40Z: 4,095 issued; 516 HIT; 509 MISS; 86 void; 2,984 open.

## 9. Carried

- The 71 resit rows skipped at the console remain open for the sitting of 2026-10-18, under the rule of section 5.
- KKR-20260916-09: the Treasury basis supports HIT; left open at the walk.
- KKR-20260815-01: confirm its keying against the sheet.
- Gate false kills observed in the daily lanes are listed separately on the findings page (RPAS 7.06), not here.
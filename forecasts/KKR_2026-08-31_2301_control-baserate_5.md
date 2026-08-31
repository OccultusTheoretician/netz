**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 312301Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-31_1519.md · forecaster: control/baserate · 7 accepted / 3 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260831-76 | 53% | 2026-09-16 | military_conflict | A commercial or military vessel is struck, mined, or seized in or near the Strait of Hormuz between 2026-09-01 and 2026-09-14. | Resolves true if UKMTO, JMIC, Reuters, or AP report a vessel struck, mined, boarded, or seized in the Strait of Hormuz within the window; false if no such report appears by the deadline. |
| KKR-20260831-77 | 25% | 2026-09-23 | economic | ICE Brent crude front-month futures settle at or above USD 95.00 per barrel on any session between 2026-09-01 and 2026-09-21. | Resolves true if ICE, Reuters, or Bloomberg data show a Brent front-month settlement at or above USD 95.00 on any trading day in the window; false if no such settlement occurs. |
| KKR-20260831-78 | 33% | 2026-10-19 | cyber | CISA or the FBI publishes an advisory formally attributing the Fire Ant intrusion campaign against Cisco network devices to a China-linked actor, between 2026-09-01 and 2026-10-15. | Resolves true if CISA.gov or FBI.gov publishes an advisory naming a China-linked actor as responsible for the Fire Ant Cisco-targeting campaign within the window; false if no such advisory appears. |
| KKR-20260831-79 | 52% | 2026-09-16 | disaster_infrastructure | Nepal's government or GDACS reports a cumulative confirmed death toll of 100 or more from the late-August 2026 flood, landslide, and hydropower-site disaster, as of 2026-09-14. | Resolves true if Nepal's government or GDACS reports a confirmed cumulative death toll of 100 or more from the event as of 2026-09-14; false if the reported toll remains below 100. |
| KKR-20260831-80 | 52% | 2026-09-14 | disaster_infrastructure | Cypriot or Turkish-Cypriot authorities declare the search for the missing passengers of the northern Cyprus ferry capsize concluded, between 2026-09-01 and 2026-09-10. | Resolves true if Cypriot, Turkish-Cypriot, or wire-service reporting confirms the ferry capsize search ended, by rescue, recovery, or stand-down, within the window; false if the search remains active past 2026-09-10. |
| KKR-20260831-81 | 44% | 2026-09-23 | political | German federal or state authorities publicly name a suspect or announce charges in the Leipzig drone attack on a Ukrainian-linked aircraft, between 2026-09-01 and 2026-09-21. | Resolves true if German federal or state prosecutors or police publicly name a suspect or announce charges in the Leipzig drone-attack case within the window; false if no naming occurs. |
| KKR-20260831-82 | 53% | 2026-10-02 | military_conflict | A further attempt to seize power from Niger's sitting government by military or paramilitary action occurs between 2026-09-01 and 2026-09-30. | Resolves true if AP, Reuters, AFP, or Niger state media report a further attempted seizure of power against the sitting government within the window; false if no such attempt is reported. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The CISA Known Exploited Vulnerabilities catalog records 3 or more entries with dateAdded between 2026-09-01 and 2026-09-14." → REJECTED: the resolution names only a venue or register (CISA, KEV, resolves) and no subject - the register is where to look, not what is claimed; name the subject inside it
- "The jury in the Lindsay Clancy murder trial in Plymouth County Superior Court returns a verdict between 2026-09-01 and 2026-09-14." → REJECTED: resolution offers alternative VENUES joined by 'or' (…a plymouth county superior court docket entry | or | wire-service report confirms the jury returne…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact; measurable claim without a numeric threshold — a row about a quantity must state the number next to its comparator; identifier digits (H.15, S&P 500) do not count
- "The Federal Open Market Committee raises the federal funds target range at its September 15-16, 2026 meeting." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim

## III. LEDGER STANDING

1205 issued all-time across 14 forecaster arms · 1044 open (83 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 318 issued · 301 open · 17 resolved · 8 hits / 9 misses · **Brier 0.275** against its own base rate 47.1% (climatological 0.249) · **skill -0.105** · under 30 resolved, this is noise.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 318 | 301 | 17 | 8 | 9 | 0.275 | 47.1% | 0.249 | -0.105 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 17 | 3 | 1 | 2 | 0.214 | 33.3% | 0.222 | +0.036 |
| lmstudio/auto[post-window] | 177 | 146 | 29 | 10 | 19 | 0.250 | 34.5% | 0.226 | -0.109 |
| lmstudio/auto[pre-verbot] | 60 | 7 | 45 | 13 | 32 | 0.222 | 28.9% | 0.205 | -0.081 |
| manual/fable | 45 | 32 | 13 | 7 | 6 | 0.183 | 53.8% | 0.249 | +0.265 |
| manual/fable-5 | 38 | 34 | 4 | 3 | 1 | 0.086 | 75.0% | 0.188 | +0.540 |
| manual/fable-5/unattested | 120 | 119 | 1 | 1 | 0 | 0.090 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 71 | 3 | 1 | 2 | 0.386 | 33.3% | 0.222 | -0.736 |
| manual/opus-5/unattested | 150 | 147 | 3 | 1 | 2 | 0.141 | 33.3% | 0.222 | +0.366 |
| manual/sonnet-5 | 45 | 25 | 20 | 12 | 8 | 0.231 | 60.0% | 0.240 | +0.037 |
| manual/sonnet-5/unattested | 137 | 129 | 8 | 5 | 3 | 0.174 | 62.5% | 0.234 | +0.257 |
| operator/human | 10 | 6 | 1 | 1 | 0 | 0.122 | 100.0% | 0.000 | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*
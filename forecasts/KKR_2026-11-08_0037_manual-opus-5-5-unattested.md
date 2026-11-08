**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 080037Z NOV 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-11-07_1612.md · forecaster: manual/opus-5.5/unattested · 7 accepted / 3 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261108-07 | 40% | 2026-12-02 | cyber | The CISA KEV catalog adds a QNAP NAS vulnerability tied to the Plex2Shell attacks, with a dateAdded value between 2026-11-09 and 2026-11-30. | TRUE if the CISA KEV catalog lists a QNAP CVE linked to Plex2Shell exploitation with dateAdded from 2026-11-09 to 2026-11-30 inclusive; otherwise FALSE. |
| KKR-20261108-08 | 45% | 2026-12-18 | economics/markets | The ICE Brent front-month futures settlement on 2026-12-18 is below 95.00 USD per barrel. Reference: 98.32 USD on the packet date. | TRUE if the ICE Brent front-month official settlement price for 2026-12-18 is below 95.00 USD; FALSE if it is 95.00 or higher. |
| KKR-20261108-09 | 88% | 2027-01-12 | political | Hakeem Jeffries is elected Speaker of the House in a roll call vote held between 2027-01-03 and 2027-01-08. | TRUE if the House Clerk or Congress.gov roll call record shows Jeffries elected Speaker in a vote held 2027-01-03 to 2027-01-08; otherwise FALSE. |
| KKR-20261108-10 | 55% | 2026-11-24 | crime/security | Polish prosecutors formally charge at least one person over the Krakow shooting between 2026-11-07 and 2026-11-20. | TRUE if Polish prosecutors announce charges against a suspect in the Krakow shooting between 2026-11-07 and 2026-11-20, reported by Reuters, AP or PAP; otherwise FALSE. |
| KKR-20261108-11 | 15% | 2027-04-05 | crime/security | The criminal trial of Alfozan in the OpenAI bugging case begins with jury selection or opening statements between 2026-11-09 and 2027-03-31. | TRUE if the federal court docket shows jury selection or opening statements in the Alfozan case between 2026-11-09 and 2027-03-31; otherwise FALSE. |
| KKR-20261108-12 | 8% | 2027-01-05 | disaster | GDACS issues an Orange or Red earthquake alert for an event in Japan occurring between 2026-11-09 and 2026-12-31. | TRUE if the GDACS archive shows an Orange or Red earthquake alert for a Japan event dated 2026-11-09 to 2026-12-31; otherwise FALSE. |
| KKR-20261108-13 | 35% | 2027-02-02 | cyber | The CISA KEV catalog adds at least one additional SonicWall SonicOS CVE with a dateAdded value between 2026-11-09 and 2027-01-31. | TRUE if the CISA KEV catalog lists a SonicWall SonicOS CVE other than CVE-2026-19868 with dateAdded from 2026-11-09 to 2027-01-31; otherwise FALSE. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "US forces conduct at least one new strike on Iranian territory between 2026-11-09 and 2026-11-22, acknowledged by the White House, Pentagon " → REJECTED: resolution offers alternative VENUES joined by 'or' (…6-11-09 to 2026-11-22, as reported by reuters | or | ap…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "Russia and Ukraine both formally announce a general ceasefire covering the whole front line taking effect between 2026-11-09 and 2027-01-31." → REJECTED: resolution offers alternative VENUES joined by 'or' (…2026-11-09 to 2027-01-31, reported by reuters | or | ap…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "A New Zealand Prime Minister is sworn in or reappointed at the head of a newly formed government between 2026-11-09 and 2026-12-11." → REJECTED: the resolution names a different subject than the statement — the claim is about Minister, New, Prime, Zealand and the resolution settles on DPMC, Government, House. A row whose resolution checks a different fact can be scored correct while being wrong

## III. LEDGER STANDING

5446 issued all-time across 22 forecaster arms · 3724 open (1345 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/opus-5.5/unattested`:** 356 issued · 342 open · 14 resolved · 8 hits / 6 misses · **Brier 0.312** against its own base rate 57.1% (climatological 0.245) · **skill -0.275** · under 30 resolved, this is noise.

*96 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1788 | 1279 | 477 | 273 | 204 | 0.300 | 57.2% | 0.245 | -0.226 |
| control/trailing | 102 | 102 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 9 | 11 | 1 | 10 | 0.123 | 9.1% | 0.083 | -0.490 |
| lmstudio/auto[post-window] | 470 | 201 | 259 | 75 | 184 | 0.204 | 29.0% | 0.206 | +0.009 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 183 | 166 | 11 | 4 | 7 | 0.227 | 36.4% | 0.231 | +0.020 |
| lmstudio/qwen36-abliterated | 184 | 182 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
| lmstudio/qwen36-realist | 163 | 130 | 31 | 10 | 21 | 0.242 | 32.3% | 0.219 | -0.106 |
| lmstudio/realist | 249 | 128 | 119 | 66 | 53 | 0.317 | 55.5% | 0.247 | -0.285 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 14 | 24 | 14 | 10 | 0.164 | 58.3% | 0.243 | +0.325 |
| manual/fable-5.1/unattested | 500 | 385 | 107 | 61 | 46 | 0.211 | 57.0% | 0.245 | +0.140 |
| manual/fable-5/unattested | 258 | 147 | 102 | 65 | 37 | 0.203 | 63.7% | 0.231 | +0.121 |
| manual/opus-5 | 74 | 39 | 35 | 18 | 17 | 0.213 | 51.4% | 0.250 | +0.146 |
| manual/opus-5.5/unattested | 356 | 342 | 14 | 8 | 6 | 0.312 | 57.1% | 0.245 | -0.275 |
| manual/opus-5/unattested | 326 | 221 | 95 | 61 | 34 | 0.208 | 64.2% | 0.230 | +0.097 |
| manual/sonnet-5 | 45 | 3 | 41 | 22 | 19 | 0.250 | 53.7% | 0.249 | -0.007 |
| manual/sonnet-5.5/unattested | 222 | 207 | 15 | 10 | 5 | 0.122 | 66.7% | 0.222 | +0.451 |
| manual/sonnet-5/unattested | 342 | 141 | 196 | 98 | 98 | 0.245 | 50.0% | 0.250 | +0.019 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*
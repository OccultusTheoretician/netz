**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 221746Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-22_1516.md · forecaster: manual/sonnet-5/unattested · 5 accepted / 4 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260822-35 | 20% | 2027-02-03 | military_conflict | Between 2026-08-24 and 2027-01-31, Israel or the United States will conduct a direct military strike on internationally recognized Iranian territory, excluding strikes on Iran aligned forces in Syria, Lebanon, Iraq, or Yemen. | TRUE if two of Reuters, AP, AFP, or an official Israeli, US, or Iranian statement confirm a strike executed on Iranian territory, excluding Syria, Lebanon, Iraq, or Yemen; FALSE otherwise. |
| KKR-20260822-36 | 45% | 2026-09-30 | economics_markets | Between 2026-08-24 and 2026-09-30, COMEX front month gold futures will settle at or above 4800.00 USD per troy ounce on at least one trading day. | TRUE if CME or COMEX publishes a front month gold futures settlement price of 4800.00 USD per ounce or higher on any trading day in the window; FALSE otherwise. |
| KKR-20260822-37 | 55% | 2026-10-19 | political | Between 2026-08-24 and 2026-10-15, the Government of Canada will formally impose new tariffs on US goods, described by Canadian officials as a dollar for dollar or matching response to the US tariff increase reported on 2026-08-22. | TRUE if Finance Canada or the Canadian government announces new tariffs on US goods described as a dollar for dollar or matching response, confirmed by Reuters or CBC; FALSE otherwise. |
| KKR-20260822-38 | 20% | 2026-11-03 | cyber | Between 2026-08-24 and 2026-10-31, a named cybersecurity outlet will report a confirmed unauthorized access incident, data breach, or cloud resource abuse case attributed to the leaked AWS keys documented on 2026-08-21. | TRUE if BleepingComputer, The Hacker News, or Krebs on Security reports a specific breach or resource abuse incident attributed to the leaked AWS keys by the deadline; FALSE otherwise. |
| KKR-20260822-39 | 15% | 2026-09-23 | disaster | Between 2026-08-24 and 2026-09-21, an aftershock of magnitude 6.0 or greater will occur within 250 km of the August 21, 2026 magnitude 6.7 earthquake near Aniso, Peru. | TRUE if the USGS earthquake catalog lists an event of magnitude 6.0 or greater within 250 km of the Aniso Peru mainshock within the stated window; FALSE otherwise. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-08-24 and 2026-09-15, Russia will launch a single wave of at least 50 Shahed or Geran type drones together with at least 5 ball" → REJECTED: resolution offers alternative VENUES joined by 'or' (…ukrainian air force | or | a…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "Between 2026-08-24 and 2026-12-31, Anthropic will publicly file an S-1 or equivalent initial public offering registration statement with the" → REJECTED: resolution offers alternative VENUES joined by 'or' (…sec edgar lists an anthropic s-1 filing, | or | a named wire service confirms the filing was …) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "Between 2026-08-24 and 2026-11-15, a US federal court will issue a new order, contempt finding, or expanded injunction against the US Postal" → REJECTED: resolution offers alternative VENUES joined by 'or' (…t docket shows a new order, contempt finding, | or | expanded injunction against usps on the mail-…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact; the resolution names a different subject than the statement — the claim is about Postal, Service and the resolution settles on USPS. A row whose resolution checks a different fact can be scored correct while being wrong
- "Between 2026-08-24 and 2026-12-31, the presiding US federal court will grant final approval of the approximately 400 million USD TikTok chil" → REJECTED: resolution offers alternative VENUES joined by 'or' (…court docket | or | a named…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

870 issued all-time across 14 forecaster arms · 780 open (32 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/sonnet-5/unattested`:** 90 issued · 89 open · 1 resolved · 0 hits / 1 misses · **Brier 0.040** against its own base rate 0.0% (climatological 0.000) · **skill —** · under 30 resolved, this is noise.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 186 | 178 | 8 | 1 | 7 | 0.125 | 12.5% | 0.109 | -0.143 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 20 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-window] | 122 | 110 | 10 | 2 | 8 | 0.240 | 20.0% | 0.160 | -0.502 |
| lmstudio/auto[pre-verbot] | 60 | 13 | 39 | 12 | 27 | 0.225 | 30.8% | 0.213 | -0.054 |
| manual/fable | 45 | 36 | 9 | 4 | 5 | 0.190 | 44.4% | 0.247 | +0.232 |
| manual/fable-5 | 38 | 38 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 81 | 81 | 0 | — | — | not computed | — | — | — |
| manual/opus-5 | 74 | 72 | 2 | 1 | 1 | 0.243 | 50.0% | 0.250 | +0.030 |
| manual/opus-5/unattested | 92 | 92 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 45 | 39 | 6 | 3 | 3 | 0.270 | 50.0% | 0.250 | -0.081 |
| manual/sonnet-5/unattested | 90 | 89 | 1 | 0 | 1 | 0.040 | 0.0% | 0.000 | — |
| operator/human | 6 | 2 | 1 | 1 | 0 | 0.122 | 100.0% | 0.000 | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*
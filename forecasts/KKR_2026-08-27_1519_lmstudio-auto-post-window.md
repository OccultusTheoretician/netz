**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 271519Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-27_1517.md · forecaster: lmstudio/auto · 8 accepted / 2 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260827-59 | 25% | 2026-09-07 | disaster | Between 2026-08-27 and 2026-09-03, the USGS will record a magnitude 5.0 or higher earthquake in Japan with a depth of less than 30km. | The USGS Significant Quakes database will list a magnitude 5.0 or higher earthquake in Japan with a depth of less than 30km, occurring between 2026-08-27 and 2026-09-03. |
| KKR-20260827-60 | 65% | 2026-09-07 | economics/markets | Between 2026-08-27 and 2026-09-03, the S&P 500 will close above 7,800 points on at least one weekday. | The S&P 500 will close above 7,800 points on at least one weekday between 2026-08-27 and 2026-09-03, as reported by a major financial data provider. |
| KKR-20260827-61 | 35% | 2026-09-07 | military/conflict | Between 2026-08-27 and 2026-09-03, a confirmed military strike will occur in the Gaza City area, resulting in at least one reported casualty. | A confirmed military strike in Gaza City, verified by two independent sources from hostile sides (IL and PS), results in at least one reported casualty. |
| KKR-20260827-62 | 40% | 2026-09-07 | political | Between 2026-08-27 and 2026-09-03, a new political statement will be issued by Iran's foreign ministry regarding negotiations with the US, corroborated by both Axis and Western sources. | A statement issued by Iran's foreign ministry regarding negotiations with the US, corroborated by at least one source from the Axis and one from the Western side, will be published between 2026-08-27 and 2026-09-03. |
| KKR-20260827-63 | 20% | 2026-09-07 | cyber | Between 2026-08-27 and 2026-09-03, a confirmed cyberattack exploiting CVE-2021-23758 will be reported by at least two independent sources. | A confirmed cyberattack exploiting CVE-2021-23758 will be reported by at least two independent sources, one from a Western outlet and one from an Axis-aligned outlet, between 2026-08-27 and 2026-09-03. |
| KKR-20260827-64 | 30% | 2026-09-07 | disaster | Between 2026-08-27 and 2026-09-03, a confirmed forest fire will be reported in Canada with a size exceeding 10,000 hectares. | A confirmed forest fire in Canada, reported by GDACS Alerts and verified by a second independent source, will have a size exceeding 10,000 hectares between 2026-08-27 and 2026-09-03. |
| KKR-20260827-65 | 25% | 2026-09-07 | political | Between 2026-08-27 and 2026-09-03, a confirmed political statement by Trump regarding Iran sanctions will be corroborated by both Western and Axis sources. | A political statement by Trump regarding Iran sanctions, published between 2026-08-27 and 2026-09-03, will be corroborated by at least one Western and one Axis-aligned source. |
| KKR-20260827-66 | 35% | 2026-09-07 | military/conflict | Between 2026-08-27 and 2026-09-03, a confirmed military strike in Kyiv will result in at least one reported casualty. | A confirmed military strike in Kyiv, verified by two independent sources from hostile sides (RU and UA), results in at least one reported casualty. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-08-27 and 2026-09-03, the CISA KEV catalog will include CVE-2026-8452 with a date-added value of 2026-08-26." → REJECTED: the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-8452 dateAdded 2026-08-26, before the claimed window 2026-08-27..2026-09-03; dateAdded is single-valued and a fresh in-window value would require removal-and-relisting, which has no documented precedent (removals exist: CVE-2022-28958, removed 2023-12-01)
- "Between 2026-08-27 and 2026-09-03, at least one confirmed cyberattack on a UK airport will result in the exposure of customer data for more " → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date

## III. LEDGER STANDING

989 issued all-time across 14 forecaster arms · 828 open (4 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/auto[post-window]`:** 160 issued · 129 open · 29 resolved · 10 hits / 19 misses · **Brier 0.250** against its own base rate 34.5% (climatological 0.226) · **skill -0.109** · under 30 resolved, this is noise.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 222 | 205 | 17 | 8 | 9 | 0.275 | 47.1% | 0.249 | -0.105 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 17 | 3 | 1 | 2 | 0.214 | 33.3% | 0.222 | +0.036 |
| lmstudio/auto[post-window] | 160 | 129 | 29 | 10 | 19 | 0.250 | 34.5% | 0.226 | -0.109 |
| lmstudio/auto[pre-verbot] | 60 | 7 | 45 | 13 | 32 | 0.222 | 28.9% | 0.205 | -0.081 |
| manual/fable | 45 | 32 | 13 | 7 | 6 | 0.183 | 53.8% | 0.249 | +0.265 |
| manual/fable-5 | 38 | 34 | 4 | 3 | 1 | 0.086 | 75.0% | 0.188 | +0.540 |
| manual/fable-5/unattested | 92 | 91 | 1 | 1 | 0 | 0.090 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 71 | 3 | 1 | 2 | 0.386 | 33.3% | 0.222 | -0.736 |
| manual/opus-5/unattested | 114 | 111 | 3 | 1 | 2 | 0.141 | 33.3% | 0.222 | +0.366 |
| manual/sonnet-5 | 45 | 25 | 20 | 12 | 8 | 0.231 | 60.0% | 0.240 | +0.037 |
| manual/sonnet-5/unattested | 102 | 94 | 8 | 5 | 3 | 0.174 | 62.5% | 0.234 | +0.257 |
| operator/human | 6 | 2 | 1 | 1 | 0 | 0.122 | 100.0% | 0.000 | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*
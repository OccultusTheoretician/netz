**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 091518Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-09_1516.md · forecaster: lmstudio/auto · 5 accepted / 5 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261009-01 | 85% | 2026-10-30 | cyber | Between 2026-10-25 and 2026-10-28, the FBI will publicly confirm the disruption of Chinese hacking tools used to breach critical infrastructure, citing the Flax Typhoon campaign. | The FBI publicly confirms the disruption of Chinese hacking tools used to breach critical infrastructure, specifically referencing the Flax Typhoon campaign, between 2026-10-25 and 2026-10-28. |
| KKR-20261009-02 | 40% | 2026-10-31 | cyber | Between 2026-10-26 and 2026-10-29, a ransomware attack will disrupt a government agency's IT systems in Japan, with a public statement from the agency confirming the incident. | A government agency in Japan publicly confirms a ransomware attack disrupting its IT systems between 2026-10-26 and 2026-10-29. |
| KKR-20261009-03 | 15% | 2026-11-01 | disaster | Between 2026-10-27 and 2026-10-30, a major earthquake of magnitude 6.0 or higher will be recorded by the USGS in the Pacific region, with a confirmed location in Vanuatu or Alaska. | The USGS records a magnitude 6.0 or higher earthquake in the Pacific region, with a confirmed location in Vanuatu or Alaska, between 2026-10-27 and 2026-10-30. |
| KKR-20261009-04 | 35% | 2026-11-03 | cyber | Between 2026-10-29 and 2026-11-01, a cyberattack exploiting CVE-2016-3081 will be reported by at least two independent sources, with the attack targeting a U.S. government system. | At least two independent sources report a cyberattack exploiting CVE-2016-3081 targeting a U.S. government system between 2026-10-29 and 2026-11-01. |
| KKR-20261009-05 | 28% | 2026-11-04 | disaster | Between 2026-10-30 and 2026-11-02, a forest fire will be reported in Australia with a green alert issued by GDACS, and the fire will be confirmed by at least two independent sources. | A forest fire in Australia is reported with a green alert by GDACS, and confirmed by at least two independent sources between 2026-10-30 and 2026-11-02. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-10-21 and 2026-10-24, the CISA KEV catalog will include CVE-2015-5477 with a date-added value of 2026-10-08." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2015-5477 dateAdded 2026-10-08, before the claimed window 2026-10-21..2026-10-24; dateAdded is single-valued and a fresh in-window value would require removal-and-relisting, which has no documented precedent (removals exist: CVE-2022-28958, removed 2023-12-01)
- "Between 2026-10-22 and 2026-10-25, a drone attack on Kyiv will be confirmed by at least two hostile sides (RU, UA) with cross-bias agreement" → REJECTED: negated-observation clause — 'with no X reported' is a claim about the source record, not about the event. The war desk prints it to describe its own reports; it cannot be adjudicated as a property of the world
- "Between 2026-10-23 and 2026-10-26, the S&P 500 will close above 7,800 on at least one weekday." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "Between 2026-10-24 and 2026-10-27, a hurricane will make landfall in the U.S. Gulf Coast with a storm surge warning issued by the NWS for a " → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "Between 2026-10-28 and 2026-10-31, the U.S. government will publicly announce a new policy to livestream a capital execution, citing nationa" → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date

## III. LEDGER STANDING

3705 issued all-time across 21 forecaster arms · 2891 open (527 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/auto[post-window]`:** 405 issued · 226 open · 170 resolved · 45 hits / 125 misses · **Brier 0.205** against its own base rate 26.5% (climatological 0.195) · **skill -0.056**.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1320 | 1119 | 169 | 106 | 63 | 0.324 | 62.7% | 0.234 | -0.386 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 405 | 226 | 170 | 45 | 125 | 0.205 | 26.5% | 0.195 | -0.056 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/qwen36 | 17 | 17 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 17 | 17 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 26 | 26 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 197 | 162 | 34 | 26 | 8 | 0.383 | 76.5% | 0.180 | -1.128 |
| manual/fable | 45 | 20 | 25 | 13 | 12 | 0.190 | 52.0% | 0.250 | +0.241 |
| manual/fable-5 | 38 | 23 | 15 | 8 | 7 | 0.130 | 53.3% | 0.249 | +0.479 |
| manual/fable-5.1/unattested | 293 | 260 | 25 | 20 | 5 | 0.207 | 80.0% | 0.160 | -0.296 |
| manual/fable-5/unattested | 258 | 202 | 47 | 36 | 11 | 0.210 | 76.6% | 0.179 | -0.169 |
| manual/opus-5 | 74 | 55 | 19 | 11 | 8 | 0.188 | 57.9% | 0.244 | +0.228 |
| manual/opus-5.5/unattested | 121 | 121 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 286 | 30 | 20 | 10 | 0.217 | 66.7% | 0.222 | +0.025 |
| manual/sonnet-5 | 45 | 7 | 37 | 19 | 18 | 0.250 | 51.4% | 0.250 | +0.000 |
| manual/sonnet-5.5/unattested | 80 | 80 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 237 | 100 | 56 | 44 | 0.263 | 56.0% | 0.246 | -0.069 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*
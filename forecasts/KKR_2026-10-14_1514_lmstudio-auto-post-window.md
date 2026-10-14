**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 141514Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-14_1513.md · forecaster: lmstudio/auto · 3 accepted / 7 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261014-01 | 25% | 2026-10-26 | disaster | Between 2026-10-21 and 2026-10-24, the USGS Significant Quakes catalog will record a magnitude 7.0 or greater earthquake in the Mid-Atlantic Ridge region. | The USGS Significant Quakes catalog carries an event with magnitude 7.0 or greater and location 'central Mid-Atlantic Ridge' with a date within the window. |
| KKR-20261014-02 | 30% | 2026-10-26 | economics | Between 2026-10-21 and 2026-10-24, the 10-year Treasury yield will exceed 5.35 percent on at least one trading day. | The 10-year Treasury yield exceeds 5.35 percent on at least one weekday within the event window. |
| KKR-20261014-03 | 20% | 2026-10-26 | cyber | Between 2026-10-21 and 2026-10-24, a major cyberattack exploiting a known vulnerability in Ivanti Connect Secure will be confirmed by two independent wire services. | Two independent wire services (e.g., Reuters, AP, Bloomberg) report a confirmed cyberattack exploiting CVE-2026-104935 in Ivanti Connect Secure during the event window. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-10-21 and 2026-10-24, the CISA KEV catalog will include CVE-2026-104935 with a date-added value of 2026-10-13." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-104935 dateAdded 2026-10-13, before the claimed window 2026-10-21..2026-10-24; dateAdded is single-valued and a fresh in-window value would require removal-and-relisting, which has no documented precedent (removals exist: CVE-2022-28958, removed 2023-12-01)
- "Between 2026-10-21 and 2026-10-24, the S&P 500 index will close above 7,800.00 on at least one trading day." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "Between 2026-10-21 and 2026-10-24, at least one Grade A or Grade B kinetic event will be reported in Kyiv, Ukraine, with cross-bias confirma" → REJECTED: cited items name Saudi Arabia, United States; the claim is about Ukraine, zone:russia_ukraine — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else
- "Between 2026-10-21 and 2026-10-24, a drone attack will be reported in Gaza City, Gaza Strip, with cross-bias confirmation from at least two " → REJECTED: cited items name China, Mongolia; the claim is about Palestine, State of, zone:israel_gaza — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else
- "Between 2026-10-21 and 2026-10-24, the CISA KEV catalog will include CVE-2026-96951 with a date-added value of 2026-10-13." → REJECTED: the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-96951 dateAdded 2026-10-13, before the claimed window 2026-10-21..2026-10-24; dateAdded is single-valued and a fresh in-window value would require removal-and-relisting, which has no documented precedent (removals exist: CVE-2022-28958, removed 2023-12-01)
- "Between 2026-10-21 and 2026-10-24, the Social Security Administration will announce a 3.6% cost-of-living adjustment for 2027." → REJECTED: resolution offers alternative VENUES joined by 'or' (…iving adjustment for 2027 via a press release | or | official statement during the event window…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "Between 2026-10-21 and 2026-10-24, a new U.S. federal regulation will be published in the Federal Register that imposes sanctions on a Russi" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim

## III. LEDGER STANDING

4098 issued all-time across 21 forecaster arms · 2987 open (438 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/auto[post-window]`:** 422 issued · 199 open · 214 resolved · 63 hits / 151 misses · **Brier 0.209** against its own base rate 29.4% (climatological 0.208) · **skill -0.007**.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1452 | 1156 | 264 | 161 | 103 | 0.313 | 61.0% | 0.238 | -0.317 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 11 | 9 | 1 | 8 | 0.146 | 11.1% | 0.099 | -0.474 |
| lmstudio/auto[post-window] | 422 | 199 | 214 | 63 | 151 | 0.209 | 29.4% | 0.208 | -0.007 |
| lmstudio/auto[pre-verbot] | 60 | 4 | 48 | 13 | 35 | 0.214 | 27.1% | 0.197 | -0.085 |
| lmstudio/qwen36 | 49 | 49 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 48 | 48 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 54 | 54 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 217 | 158 | 58 | 31 | 27 | 0.296 | 53.4% | 0.249 | -0.191 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 20 | 18 | 10 | 8 | 0.164 | 55.6% | 0.247 | +0.334 |
| manual/fable-5.1/unattested | 337 | 279 | 50 | 34 | 16 | 0.248 | 68.0% | 0.218 | -0.140 |
| manual/fable-5/unattested | 258 | 179 | 70 | 47 | 23 | 0.190 | 67.1% | 0.221 | +0.138 |
| manual/opus-5 | 74 | 44 | 30 | 14 | 16 | 0.210 | 46.7% | 0.249 | +0.156 |
| manual/opus-5.5/unattested | 168 | 163 | 5 | 3 | 2 | 0.440 | 60.0% | 0.240 | -0.835 |
| manual/opus-5/unattested | 326 | 265 | 51 | 34 | 17 | 0.182 | 66.7% | 0.222 | +0.182 |
| manual/sonnet-5 | 45 | 5 | 39 | 21 | 18 | 0.262 | 53.8% | 0.249 | -0.055 |
| manual/sonnet-5.5/unattested | 122 | 122 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 206 | 131 | 69 | 62 | 0.249 | 52.7% | 0.249 | +0.000 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*
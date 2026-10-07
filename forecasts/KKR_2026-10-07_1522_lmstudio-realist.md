**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 071522Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-07_1518.md · forecaster: lmstudio/realist · 7 accepted / 3 rejected by validation gate · 5 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261007-06 | 30% | 2026-10-14 | military/conflict | On 2026-10-10, a drone strike targeting a Russian military command node in Dnipro is confirmed by at least two independently biased sources, including one from a Western outlet and one from a pro-Ukrainian outlet. | The CISA KEV catalog carries a date-added value between 2026-10-07 and 2026-10-10, and at least one report from a Western outlet and one from a pro-Ukrainian outlet independently confirms a drone strike on a Russian military command node in Dnipro on or before 2026-10-10. |
| KKR-20261007-07 | 25% | 2026-10-19 | economics/markets | On 2026-10-15, the 10-year U.S. Treasury yield exceeds 5.35 percent, based on the close of the U.S. Treasury auction on that date. | The 10-year U.S. Treasury note yield, as reported by the U.S. Department of the Treasury at the close of the auction on 2026-10-15, is greater than 5.35 percent. |
| KKR-20261007-08 | 35% | 2026-10-21 | cyber | On 2026-10-18, a cyberattack exploiting the Atlassian Jira and Confluence file-access flaw (CVE-2026-XXXX) is confirmed by at least two independent sources, including one from a government cybersecurity agency and one from a private security firm. | The CISA KEV catalog carries a date-added value between 2026-10-15 and 2026-10-18, and at least one report from a government cybersecurity agency and one from a private security firm independently confirm a cyberattack exploiting the Atlassian Jira and Confluence file-access flaw (CVE-2026-XXXX) during that window. |
| KKR-20261007-09 | 20% | 2026-10-23 | disaster | On 2026-10-20, a tropical cyclone named ISAIAS-26 causes a flood event in the U.S. Gulf Coast region, resulting in at least one fatality confirmed by the National Weather Service. | The National Weather Service (NWS) issues a final report confirming that a flood event caused by tropical cyclone ISAIAS-26 resulted in at least one fatality on the U.S. Gulf Coast between 2026-10-18 and 2026-10-20. |
| KKR-20261007-10 | 25% | 2026-10-28 | cyber | On 2026-10-25, a cyberattack using the PoeLLM malware is confirmed by at least two independent sources, including one from a government cybersecurity agency and one from a private security firm, targeting AI servers in the U.S. and Europe. | The CISA KEV catalog carries a date-added value between 2026-10-22 and 2026-10-25, and at least one report from a government cybersecurity agency and one from a private security firm independently confirm a cyberattack using PoeLLM malware targeting AI servers in the U.S. and Europe during that window. |
| KKR-20261007-11 | 35% | 2026-10-29 | cyber | On 2026-10-26, a new cyberattack exploiting the SonicWall SMA1000 gateway SSRF flaw (CVE-2026-XXXX) is confirmed by at least two independent sources, including one from a government cybersecurity agency and one from a private security firm. | The CISA KEV catalog carries a date-added value between 2026-10-23 and 2026-10-26, and at least one report from a government cybersecurity agency and one from a private security firm independently confirm a cyberattack exploiting the SonicWall SMA1000 gateway SSRF flaw (CVE-2026-XXXX) during that window. |
| KKR-20261007-12 | 20% | 2026-10-31 | disaster | On 2026-10-28, a major earthquake of magnitude 6.0 or higher occurs in the Russian Far East, with at least 10 fatalities confirmed by the Russian Emergency Ministry. | The Russian Emergency Ministry issues a final report on 2026-10-28 confirming that a magnitude 6.0 or higher earthquake occurred in the Russian Far East, resulting in at least 10 fatalities. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "On 2026-10-22, the French government announces a new national security directive suspending the use of stun grenades in all public operation" → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-10-22 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "On 2026-10-24, the Indian central bank announces a second consecutive rate hike, raising the benchmark interest rate by 25 basis points, as " → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-10-24 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "On 2026-10-30, a new political crisis emerges in France as the government faces a no-confidence vote in the National Assembly, resulting in " → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-10-30 exactly. Price a day, not a window: widen the window or state why the date is fixed

## III. LEDGER STANDING

3546 issued all-time across 21 forecaster arms · 2732 open (423 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/realist`:** 192 issued · 157 open · 34 resolved · 26 hits / 8 misses · **Brier 0.383** against its own base rate 76.5% (climatological 0.180) · **skill -1.128**.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1265 | 1064 | 169 | 106 | 63 | 0.324 | 62.7% | 0.234 | -0.386 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 392 | 213 | 170 | 45 | 125 | 0.205 | 26.5% | 0.195 | -0.056 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/qwen36 | 9 | 9 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 8 | 8 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 13 | 13 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 192 | 157 | 34 | 26 | 8 | 0.383 | 76.5% | 0.180 | -1.128 |
| manual/fable | 45 | 20 | 25 | 13 | 12 | 0.190 | 52.0% | 0.250 | +0.241 |
| manual/fable-5 | 38 | 23 | 15 | 8 | 7 | 0.130 | 53.3% | 0.249 | +0.479 |
| manual/fable-5.1/unattested | 274 | 241 | 25 | 20 | 5 | 0.207 | 80.0% | 0.160 | -0.296 |
| manual/fable-5/unattested | 258 | 202 | 47 | 36 | 11 | 0.210 | 76.6% | 0.179 | -0.169 |
| manual/opus-5 | 74 | 55 | 19 | 11 | 8 | 0.188 | 57.9% | 0.244 | +0.228 |
| manual/opus-5.5/unattested | 103 | 103 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 286 | 30 | 20 | 10 | 0.217 | 66.7% | 0.222 | +0.025 |
| manual/sonnet-5 | 45 | 7 | 37 | 19 | 18 | 0.250 | 51.4% | 0.250 | +0.000 |
| manual/sonnet-5.5/unattested | 61 | 61 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 237 | 100 | 56 | 44 | 0.263 | 56.0% | 0.246 | -0.069 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*
**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 151518Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-15_1512.md · forecaster: lmstudio/qwen36 · 8 accepted / 2 rejected by validation gate · 6 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261015-08 | 25% | 2026-11-10 | economics/markets | WTI Crude closes above 100.00 USD per barrel on at least one trading day between 2026-11-02 and 2026-11-09. | A NYMEX WTI Crude settlement price is recorded at or above 100.00 USD. |
| KKR-20261015-09 | 30% | 2026-11-24 | disaster | The USGS Significant Quakes catalog records a magnitude 7.0 or greater earthquake between 2026-11-15 and 2026-11-22. | The USGS Significant Quakes catalog lists an event with magnitude 7.0 or higher. |
| KKR-20261015-10 | 5% | 2026-12-09 | political | The Federal Register publishes a final rule implementing the Brazil shorter working week legislation between 2026-12-01 and 2026-12-08. | A final rule text is published in the Federal Register with a date within the event window. |
| KKR-20261015-11 | 20% | 2026-12-23 | political | A US federal court docket records an indictment of a senior Iranian official for sanctions evasion between 2026-12-15 and 2026-12-22. | A public federal court docket lists an indictment against a named senior Iranian official. |
| KKR-20261015-12 | 25% | 2027-01-14 | disaster | The USGS Significant Quakes catalog records a magnitude 6.0 or greater earthquake in Panama between 2027-01-05 and 2027-01-12. | The USGS Significant Quakes catalog lists an event with magnitude 6.0 or higher in Panama. |
| KKR-20261015-13 | 35% | 2027-02-09 | economics/markets | The Nasdaq Composite closes below 25,000.00 on at least one trading day between 2027-02-01 and 2027-02-08. | A Nasdaq Composite settlement price is recorded below 25,000.00. |
| KKR-20261015-14 | 40% | 2027-02-23 | crime/security | A US federal court docket records the execution of Nidal Hasan between 2027-02-15 and 2027-02-22. | A US federal court docket or official military record confirms the execution of Nidal Hasan. |
| KKR-20261015-15 | 30% | 2027-03-10 | disaster | The USGS Significant Quakes catalog records a magnitude 7.0 or greater earthquake in the Pacific Ring of Fire between 2027-03-01 and 2027-03-08. | The USGS Significant Quakes catalog lists an event with magnitude 7.0 or higher in the Pacific Ring of Fire. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The CISA KEV catalog carries a date-added value for a critical remote code execution vulnerability in Cisco Secure Email Gateway between 202" → REJECTED: the resolution names only a venue or register (CISA, KEV, cve) and no subject - the register is where to look, not what is claimed; name the subject inside it
- "The CISA KEV catalog carries a date-added value for a critical remote code execution vulnerability in Palo Alto Networks PAN-OS between 2027" → REJECTED: the resolution names only a venue or register (CISA, KEV, cve) and no subject - the register is where to look, not what is claimed; name the subject inside it

## III. LEDGER STANDING

4178 issued all-time across 21 forecaster arms · 3067 open (481 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36`:** 65 issued · 65 open · nothing resolved yet — this arm earns a score at its first resolution.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1475 | 1179 | 264 | 161 | 103 | 0.313 | 61.0% | 0.238 | -0.317 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 11 | 9 | 1 | 8 | 0.146 | 11.1% | 0.099 | -0.474 |
| lmstudio/auto[post-window] | 429 | 206 | 214 | 63 | 151 | 0.209 | 29.4% | 0.208 | -0.007 |
| lmstudio/auto[pre-verbot] | 60 | 4 | 48 | 13 | 35 | 0.214 | 27.1% | 0.197 | -0.085 |
| lmstudio/qwen36 | 65 | 65 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 52 | 52 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 58 | 58 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 220 | 161 | 58 | 31 | 27 | 0.296 | 53.4% | 0.249 | -0.191 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 20 | 18 | 10 | 8 | 0.164 | 55.6% | 0.247 | +0.334 |
| manual/fable-5.1/unattested | 345 | 287 | 50 | 34 | 16 | 0.248 | 68.0% | 0.218 | -0.140 |
| manual/fable-5/unattested | 258 | 179 | 70 | 47 | 23 | 0.190 | 67.1% | 0.221 | +0.138 |
| manual/opus-5 | 74 | 44 | 30 | 14 | 16 | 0.210 | 46.7% | 0.249 | +0.156 |
| manual/opus-5.5/unattested | 174 | 169 | 5 | 3 | 2 | 0.440 | 60.0% | 0.240 | -0.835 |
| manual/opus-5/unattested | 326 | 265 | 51 | 34 | 17 | 0.182 | 66.7% | 0.222 | +0.182 |
| manual/sonnet-5 | 45 | 5 | 39 | 21 | 18 | 0.262 | 53.8% | 0.249 | -0.055 |
| manual/sonnet-5.5/unattested | 131 | 131 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 206 | 131 | 69 | 62 | 0.249 | 52.7% | 0.249 | +0.000 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*
**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 212254Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-21_1512.md · forecaster: control/baserate · 8 accepted / 2 rejected by validation gate · 0 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261021-36 | 46% | 2026-11-23 | cyber | CISA adds CVE-2026-109618 or CVE-2026-109619, the PHP2Shell remote code execution flaws in PHP, to its Known Exploited Vulnerabilities catalog between 2026-10-21 and 2026-11-20. | The CISA KEV catalog lists CVE-2026-109618 or CVE-2026-109619 with a dateAdded value between 2026-10-21 and 2026-11-20 inclusive. |
| KKR-20261021-37 | 60% | 2026-12-11 | economics/markets | The Federal Open Market Committee announces an increase in the federal funds target range at its scheduled meeting concluding on 2026-12-09. | The FOMC statement dated 2026-12-09 raises the target range; equivalently, FRED series DFEDTARU for 2026-12-10 exceeds its 2026-12-08 value. A hold or cut resolves false. |
| KKR-20261021-38 | 60% | 2026-11-02 | economics/markets | Moodys lowers the long-term issuer rating of the Government of France by at least one notch in a rating action published between 2026-10-22 and 2026-10-30. | A rating action on moodys.com, or the Agence France Tresor ratings page, shows a Moodys downgrade of France dated 2026-10-22 to 2026-10-30. An affirmation or outlook-only change resolves false. |
| KKR-20261021-39 | 60% | 2027-01-08 | economics/markets | The WTI Cushing spot crude oil price for 2026-12-31 is below 80.00 dollars per barrel. Reference: 97.86 dollars per barrel on the packet date per the report market snapshot. | FRED series DCOILWTICO (EIA WTI Cushing spot) shows a value below 80.00 for 2026-12-31. If no value is recorded that day, use the last value on or before 2026-12-31. |
| KKR-20261021-40 | 42% | 2027-01-12 | political | A member of the House Democratic Caucus is elected Speaker of the US House of Representatives for the 120th Congress in a vote held between 2027-01-03 and 2027-01-10. | The Clerk of the House roll call for election of the Speaker, held between 2027-01-03 and 2027-01-10, records a Democrat elected. Another winner, or no Speaker elected in that window, resolves false. |
| KKR-20261021-41 | 42% | 2027-01-04 | political | The French National Assembly adopts a motion of censure, bringing down the sitting government, in a vote held between 2026-10-22 and 2026-12-31. | Assemblee nationale records or the Journal officiel show a motion de censure adopted under Article 49 of the Constitution in a sitting held between 2026-10-22 and 2026-12-31. |
| KKR-20261021-42 | 66% | 2027-01-04 | military/conflict | The United States and Iran both publicly confirm an agreement or understanding on commercial shipping passage through the Strait of Hormuz, announced between 2026-10-22 and 2026-12-31. | The White House or State Department and the Iranian foreign ministry each publicly confirm a Hormuz shipping agreement or understanding announced between 2026-10-22 and 2026-12-31, as reported by Reuters or AP. |
| KKR-20261021-43 | 36% | 2027-04-13 | crime/security | The US Department of Justice announces criminal charges against, or the arrest or extradition of, at least one person for SafePay ransomware activity between 2026-10-22 and 2027-04-09. | A justice.gov press release dated 2026-10-22 to 2027-04-09 announces charges, an arrest, or an extradition of a named or unnamed defendant for participation in SafePay ransomware operations. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "A general ceasefire covering the entire Russia-Ukraine front line takes effect between 2026-10-22 and 2027-01-31, declared in force by both " → REJECTED: the resolution narrows the claim with a qualifier the statement never makes — partial. The forecaster is graded on the statement; a severity or status qualifier living only in the resolution is invisible to anyone reading the claim
- "Kenya reaches a cumulative total of 20 or more laboratory-confirmed Ebola cases in an official count dated between 2026-10-22 and 2026-12-15" → REJECTED: resolution offers alternative VENUES joined by 'or' (…utbreak news post, who afro situation report, | or | kenya ministry of health statement dated 2026…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

4674 issued all-time across 21 forecaster arms · 3322 open (544 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 1649 issued · 1266 open · 351 resolved · 216 hits / 135 misses · **Brier 0.316** against its own base rate 61.5% (climatological 0.237) · **skill -0.337**.

*87 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1649 | 1266 | 351 | 216 | 135 | 0.316 | 61.5% | 0.237 | -0.337 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 11 | 9 | 1 | 8 | 0.146 | 11.1% | 0.099 | -0.474 |
| lmstudio/auto[post-window] | 453 | 212 | 231 | 70 | 161 | 0.211 | 30.3% | 0.211 | -0.001 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 92 | 91 | 1 | 1 | 0 | 0.722 | 100.0% | 0.000 | — |
| lmstudio/qwen36-abliterated | 91 | 91 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 100 | 93 | 7 | 3 | 4 | 0.297 | 42.9% | 0.245 | -0.215 |
| lmstudio/realist | 236 | 149 | 86 | 49 | 37 | 0.321 | 57.0% | 0.245 | -0.311 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 15 | 23 | 13 | 10 | 0.170 | 56.5% | 0.246 | +0.307 |
| manual/fable-5.1/unattested | 406 | 325 | 73 | 47 | 26 | 0.233 | 64.4% | 0.229 | -0.015 |
| manual/fable-5/unattested | 258 | 165 | 84 | 57 | 27 | 0.193 | 67.9% | 0.218 | +0.116 |
| manual/opus-5 | 74 | 42 | 32 | 15 | 17 | 0.204 | 46.9% | 0.249 | +0.182 |
| manual/opus-5.5/unattested | 237 | 226 | 11 | 5 | 6 | 0.362 | 45.5% | 0.248 | -0.460 |
| manual/opus-5/unattested | 326 | 247 | 69 | 48 | 21 | 0.195 | 69.6% | 0.212 | +0.078 |
| manual/sonnet-5 | 45 | 4 | 40 | 22 | 18 | 0.256 | 55.0% | 0.247 | -0.033 |
| manual/sonnet-5.5/unattested | 181 | 178 | 3 | 3 | 0 | 0.009 | 100.0% | 0.000 | — |
| manual/sonnet-5/unattested | 342 | 179 | 158 | 83 | 75 | 0.251 | 52.5% | 0.249 | -0.006 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*
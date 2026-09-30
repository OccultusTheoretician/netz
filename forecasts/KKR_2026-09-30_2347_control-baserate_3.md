**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 302347Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-30_1517.md · forecaster: control/baserate · 10 accepted / 0 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260930-55 | 32% | 2026-10-13 | cyber | CISA adds at least one Cisco SD-WAN vulnerability to its Known Exploited Vulnerabilities catalog with a date-added value between 2026-09-30 and 2026-10-09. | The CISA KEV catalog JSON lists a Cisco entry whose product, vulnerability name or short description mentions SD-WAN and whose dateAdded value falls between 2026-09-30 and 2026-10-09 inclusive. |
| KKR-20260930-56 | 29% | 2026-12-04 | crime_security | The US Department of Justice publicly announces an arrest, extradition or new criminal charge of a named individual described as a ShinyHunters member, excluding the person arrested on or before 2026-09-29, in a release dated between 2026-10-01 and 2026-11-30. | A US Department of Justice press release dated between 2026-10-01 and 2026-11-30 announces an arrest, extradition or new criminal charge of a named individual described as a ShinyHunters member, excluding the person arrested on or before 2026-09-29. |
| KKR-20260930-57 | 48% | 2026-11-04 | economic | The US 10-year Treasury constant-maturity yield closes at or above 5.50 percent on at least one date between 2026-10-01 and 2026-10-30. Reference: 5.27 percent on the packet date. | FRED series DGS10 shows a value of 5.50 percent or higher for at least one date between 2026-10-01 and 2026-10-30 inclusive. Reference: 5.27 percent on the packet date. |
| KKR-20260930-58 | 48% | 2026-11-04 | economic | The S&P 500 index closes at or below 7,300 on at least one date between 2026-10-01 and 2026-10-30. Reference: 7,712.13 on the packet date. | The official S&P 500 closing value, per S&P Dow Jones Indices or FRED series SP500, is 7,300.00 or lower on at least one date between 2026-10-01 and 2026-10-30 inclusive. Reference: 7,712.13 on the packet date. |
| KKR-20260930-59 | 64% | 2026-10-19 | military_conflict | Russia launches at least 500 drones and missiles combined against Ukraine in a single overnight attack, per the Ukrainian Air Force, on a date between 2026-10-01 and 2026-10-14. | Reuters or AP reports, citing the Ukrainian Air Force, that Russia launched at least 500 drones and missiles combined in one overnight attack occurring between 2026-10-01 and 2026-10-14. |
| KKR-20260930-60 | 64% | 2026-11-02 | military_conflict | Israeli strikes or gunfire kill at least 30 people in Gaza on a single calendar day between 2026-10-01 and 2026-10-28, per Gaza health officials. | Reuters or AP reports, citing Gaza health officials, that at least 30 Palestinians were killed by Israeli strikes or fire in Gaza on one calendar day falling between 2026-10-01 and 2026-10-28. |
| KKR-20260930-61 | 64% | 2026-10-26 | military_conflict | North Korea launches at least one ballistic missile, as announced by the South Korean Joint Chiefs of Staff or the Japanese Ministry of Defense, on a date between 2026-10-01 and 2026-10-21. | The South Korean Joint Chiefs of Staff or Japanese Ministry of Defense announces a North Korean ballistic missile launch occurring between 2026-10-01 and 2026-10-21, as reported by Reuters, AP or Yonhap. |
| KKR-20260930-62 | 64% | 2027-01-04 | military_conflict | Iran delivers a formal Article X notice of withdrawal from the Treaty on the Non-Proliferation of Nuclear Weapons to the UN Security Council between 2026-10-01 and 2026-12-31. | The United Nations, the IAEA or the Iranian government confirms that Iran delivered an Article X withdrawal notice from the NPT to the UN Security Council between 2026-10-01 and 2026-12-31. |
| KKR-20260930-63 | 39% | 2026-11-10 | political | Steve Hilton receives the most votes in the California governor general election held on 2026-11-03. | California Secretary of State unofficial results posted as of 2026-11-10 show Steve Hilton with the most votes in the governor contest held on 2026-11-03. |
| KKR-20260930-64 | 39% | 2026-12-04 | political | At least one non-Burundian national removed from the United States arrives in Burundi between 2026-10-01 and 2026-11-30. | AP, Reuters or the Guardian reports that at least one non-Burundian deportee removed from the United States arrived in Burundi on a date between 2026-10-01 and 2026-11-30. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

Nothing rejected — every projection cleared the gate.

## III. LEDGER STANDING

3161 issued all-time across 18 forecaster arms · 2619 open (298 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 1133 issued · 1016 open · 85 resolved · 50 hits / 35 misses · **Brier 0.327** against its own base rate 58.8% (climatological 0.242) · **skill -0.352**.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1133 | 1016 | 85 | 50 | 35 | 0.327 | 58.8% | 0.242 | -0.352 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 345 | 195 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 148 | 143 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 27 | 18 | 10 | 8 | 0.189 | 55.6% | 0.247 | +0.235 |
| manual/fable-5 | 38 | 27 | 11 | 6 | 5 | 0.101 | 54.5% | 0.248 | +0.591 |
| manual/fable-5.1/unattested | 232 | 215 | 9 | 6 | 3 | 0.176 | 66.7% | 0.222 | +0.209 |
| manual/fable-5/unattested | 258 | 237 | 12 | 11 | 1 | 0.214 | 91.7% | 0.076 | -1.797 |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5.5/unattested | 57 | 57 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 301 | 15 | 11 | 4 | 0.235 | 73.3% | 0.196 | -0.199 |
| manual/sonnet-5 | 45 | 9 | 35 | 18 | 17 | 0.247 | 51.4% | 0.250 | +0.009 |
| manual/sonnet-5.5/unattested | 17 | 17 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 278 | 59 | 31 | 28 | 0.238 | 52.5% | 0.249 | +0.047 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*
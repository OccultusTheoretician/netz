**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 152209Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-15_1544.md · forecaster: control/baserate · 9 accepted / 1 rejected by validation gate · 5 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260915-27 | 26% | 2026-11-03 | economics/markets | The US 10-year Treasury constant maturity yield closes at or above 5.00 percent on at least one business day between 2026-09-16 and 2026-10-30. Reference: 4.99 percent at packet seal on 2026-09-15. | True if the Treasury par yield curve or FRED series DGS10 records a value of 5.00 or higher for any business day from 2026-09-16 through 2026-10-30 inclusive. |
| KKR-20260915-28 | 26% | 2027-01-05 | economics/markets | NYMEX WTI crude front-month settles above 130.00 dollars per barrel on at least one trading day between 2026-09-16 and 2026-12-31. Reference: WTI 104.64 at packet seal on 2026-09-15. | True if the official CME NYMEX daily settlement for the front-month WTI contract exceeds 130.00 on any trading day from 2026-09-16 through 2026-12-31 inclusive. |
| KKR-20260915-29 | 28% | 2026-10-20 | cyber | The CISA Known Exploited Vulnerabilities catalog adds at least one Google Chrome or Chromium CVE with dateAdded between 2026-09-16 and 2026-10-16. | True if the public CISA KEV JSON contains an entry whose vendor or product field names Google Chrome or Chromium with dateAdded between 2026-09-16 and 2026-10-16 inclusive. |
| KKR-20260915-30 | 28% | 2026-12-18 | cyber | The CISA KEV record for CVE-2026-76461, the Cisco Secure Email Gateway SQL injection added 2026-09-14, shows knownRansomwareCampaignUse equal to Known at any point between 2026-09-16 and 2026-12-16. | True if the public CISA KEV JSON entry for CVE-2026-76461 shows knownRansomwareCampaignUse equal to Known when retrieved on the deadline date. |
| KKR-20260915-31 | 56% | 2026-12-18 | military/conflict | Between 2026-09-16 and 2026-12-15, at least one NATO member state formally requests consultations under Article 4 of the North Atlantic Treaty. | True if NATO or the requesting member government publicly confirms an Article 4 consultation request made within the window, corroborated by at least two international news outlets. |
| KKR-20260915-32 | 56% | 2027-01-05 | military/conflict | Between 2026-09-16 and 2026-12-31, anti-Houthi forces take control of Hodeidah city or its port on the Yemeni Red Sea coast. | True if at least two international outlets on different sides of the conflict report anti-Houthi forces holding Hodeidah city center or port facilities before 2027-01-01. |
| KKR-20260915-33 | 35% | 2026-12-10 | political | In the US House elections held 2026-11-03, Democratic candidates win at least 218 seats. | True if Associated Press race calls, as of the deadline date, show Democratic candidates winning 218 or more of the 435 House seats contested on 2026-11-03. |
| KKR-20260915-34 | 56% | 2027-01-05 | military/conflict | Between 2026-09-16 and 2026-12-31, the governments of Russia and Ukraine each publicly announce the same mutual halt to strikes, either a general ceasefire or a mutual energy infrastructure moratorium. | True if official statements from both governments, reported by outlets on both sides, announce the same mutual halt taking effect within the window. |
| KKR-20260915-35 | 10% | 2027-03-02 | crime/security | Between 2026-09-16 and 2027-02-26, at least one Black Axe defendant extradited to the United States enters a guilty plea or is convicted in US federal court. | True if a US federal court docket records a guilty plea or a conviction for at least one extradited Black Axe cybercrime defendant within the window. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-09-16 and 2026-12-31, the Panama Canal Authority publishes an advisory reducing maximum authorized daily transits below the lev" → REJECTED: the resolution names a different subject than the statement — the claim is about Authority, Canal, Panama and the resolution settles on ACP. A row whose resolution checks a different fact can be scored correct while being wrong

## III. LEDGER STANDING

2174 issued all-time across 16 forecaster arms · 1838 open (101 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 715 issued · 677 open · 38 resolved · 18 hits / 20 misses · **Brier 0.280** against its own base rate 47.4% (climatological 0.249) · **skill -0.124**.

*21 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 715 | 677 | 38 | 18 | 20 | 0.280 | 47.4% | 0.249 | -0.124 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 273 | 144 | 120 | 26 | 94 | 0.195 | 21.7% | 0.170 | -0.151 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 69 | 69 | 0 | — | — | not computed | — | — | — |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 31 | 7 | 5 | 2 | 0.063 | 71.4% | 0.204 | +0.692 |
| manual/fable-5.1/unattested | 96 | 96 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 240 | 237 | 3 | 3 | 0 | 0.153 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 244 | 238 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 13 | 31 | 17 | 14 | 0.239 | 54.8% | 0.248 | +0.036 |
| manual/sonnet-5/unattested | 234 | 202 | 32 | 16 | 16 | 0.224 | 50.0% | 0.250 | +0.105 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*
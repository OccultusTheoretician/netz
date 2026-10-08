**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 082338Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-08_1517.md · forecaster: manual/opus-5.5/unattested · 9 accepted / 1 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261008-72 | 45% | 2026-10-19 | disaster | Hurricane Isaias makes at least one US landfall with maximum sustained winds of 96 mph (Category 2) or higher between 2026-10-08 and 2026-10-15. | True if an NHC public advisory or tropical cyclone update issued between 2026-10-08 and 2026-10-15 reports the center of Isaias crossing the US coastline with maximum sustained winds of 96 mph or higher. |
| KKR-20261008-73 | 12% | 2026-11-12 | disaster | An earthquake of magnitude 6.0 or greater occurs within 100 km of the epicenter of the 2026-10-08 M6.3 Vanuatu earthquake (USGS event us6000u0xi) between 2026-10-09 and 2026-11-08. | True if the USGS ComCat catalog lists at least one event of magnitude 6.0 or greater with origin time between 2026-10-09 and 2026-11-08 UTC within 100 km of the epicenter of event us6000u0xi. |
| KKR-20261008-74 | 50% | 2026-11-18 | military/conflict | A single Russian missile, drone, or glide-bomb attack on one locality in Ukraine kills 20 or more people between 2026-10-09 and 2026-11-15. | True if Reuters and AP each report that one Russian attack on a single Ukrainian locality, occurring between 2026-10-09 and 2026-11-15, killed at least 20 people, using tolls reported by the deadline. |
| KKR-20261008-75 | 80% | 2026-12-15 | political | Democratic candidates win at least 218 of the 435 US House seats in the general election held on 2026-11-03. | True if, by the deadline, the Associated Press has called at least 218 US House races from the 2026-11-03 general election for Democratic candidates. |
| KKR-20261008-76 | 40% | 2027-01-05 | economics/markets | The 10-year US Treasury constant-maturity yield is at or above 5.60 percent on at least one trading day between 2026-10-09 and 2026-12-31. Reference: 5.30 percent on the packet date. | True if FRED series DGS10 shows a value of 5.60 or higher for any date between 2026-10-09 and 2026-12-31. Reference: 5.30 percent on the packet date. |
| KKR-20261008-77 | 35% | 2027-01-05 | economics/markets | The Brent crude spot price reaches 125.00 US dollars per barrel or higher on at least one trading day between 2026-10-09 and 2026-12-18. Reference: 105.68 dollars per barrel on the packet date. | True if FRED series DCOILBRENTEU shows a value of 125.00 or higher for any date between 2026-10-09 and 2026-12-18. Reference: 105.68 dollars per barrel on the packet date. |
| KKR-20261008-78 | 25% | 2027-01-05 | military/conflict | A new US-Iran ceasefire or truce is announced by the US government and publicly accepted by the Iranian government between 2026-10-09 and 2026-12-31. | True if, between 2026-10-09 and 2026-12-31, the White House or State Department announces a US-Iran ceasefire or truce and the Iranian president or foreign ministry publicly accepts it, as reported by Reuters or AP. |
| KKR-20261008-79 | 35% | 2027-01-05 | political | The South Korean ambassador to Ukraine, recalled on 2026-10-08 over the North Korean POW disclosure dispute, or a newly appointed successor, resumes or takes up duties in Kyiv between 2026-10-09 and 2026-12-31. | True if the South Korean foreign ministry or Yonhap reports that ambassador Park Hee-chang or a successor resumed or took up duties at the embassy in Kyiv between 2026-10-09 and 2026-12-31. |
| KKR-20261008-80 | 45% | 2027-02-02 | cyber | CISA adds the CVSS 10.0 SonicWall SMA1000 pre-authentication SSRF flaw patched in early October 2026 to its Known Exploited Vulnerabilities catalog between 2026-10-08 and 2027-01-29. | True if the CISA KEV catalog holds a SonicWall SMA1000 server-side request forgery entry with a dateAdded value between 2026-10-08 and 2027-01-29. SMA1000 entries added before 2026-10-08 do not count. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The MonsterCloud owner charged in early October 2026 with secretly paying ransomware operators while billing victims pleads guilty to at lea" → REJECTED: resolution offers alternative VENUES joined by 'or' (…the court docket in the case | or | a prosecuting office press release shows the …) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

3692 issued all-time across 21 forecaster arms · 2878 open (485 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/opus-5.5/unattested`:** 121 issued · 121 open · nothing resolved yet — this arm earns a score at its first resolution.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1312 | 1111 | 169 | 106 | 63 | 0.324 | 62.7% | 0.234 | -0.386 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 400 | 221 | 170 | 45 | 125 | 0.205 | 26.5% | 0.195 | -0.056 |
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
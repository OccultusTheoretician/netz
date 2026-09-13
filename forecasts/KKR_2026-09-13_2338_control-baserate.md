**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 132338Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-13_1712.md · forecaster: control/baserate · 8 accepted / 1 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260913-16 | 56% | 2026-10-06 | military_conflict | Between 2026-09-20 and 2026-10-04, at least one additional commercial or military vessel will be struck, hit, or attacked while transiting the Strait of Hormuz. | UKMTO issues an advisory, or two independent wire services such as Reuters, AP, or AFP report, that a vessel was struck, hit, or attacked while transiting the Strait of Hormuz between 2026-09-20 and 2026-10-04. |
| KKR-20260913-17 | 56% | 2026-10-13 | military_conflict | Between 2026-09-20 and 2026-10-11, a Yemeni government-aligned force, Saudi-led coalition, or multinational naval task force will reclaim physical control of a Bab el-Mandeb-area port or checkpoint that Houthi forces held as of 2026-09-13. | Al Jazeera, Reuters, AP, or AFP report that anti-Houthi forces have retaken a Bab el-Mandeb-area port, town, or checkpoint held by Houthi forces as of 2026-09-13, with the retaking dated between 2026-09-20 and 2026-10-11. |
| KKR-20260913-18 | 26% | 2026-10-20 | economics_markets | WTI crude oil, reference 100.05 dollars per barrel at the prior-session close reported in the 2026-09-13 packet, will settle at or above 112.00 dollars per barrel on any NYMEX trading day between 2026-09-21 and 2026-10-19. | The NYMEX front-month WTI settlement price, reference 100.05 dollars per barrel on the 2026-09-13 packet date, is 112.00 dollars per barrel or higher on at least one trading day between 2026-09-21 and 2026-10-19. |
| KKR-20260913-19 | 28% | 2026-10-27 | cyber | A CVE tied to the Tencent-application flaw used to deploy GrayRabbit malware, or to the passkey-phishing campaign hijacking Microsoft cloud accounts, will be added to the CISA Known Exploited Vulnerabilities catalog with a dateAdded between 2026-09-20 and 2026-10-25. | The CISA Known Exploited Vulnerabilities catalog lists a CVE matching the Tencent-app GrayRabbit exploitation chain or the Microsoft cloud passkey-phishing campaign, with a dateAdded value between 2026-09-20 and 2026-10-25. |
| KKR-20260913-20 | 35% | 2026-12-03 | political | Between 2026-09-20 and 2026-12-01, the Kosovo governing coalition approved on or around 2026-09-13 will lose a Kuvendi confidence vote or formally dissolve. | Reuters, AP, or Al Jazeera report, or the Kuvendi record shows, that Kosovo's coalition government formed around 2026-09-13 lost a confidence vote or formally dissolved between 2026-09-20 and 2026-12-01. |
| KKR-20260913-21 | 35% | 2026-11-03 | political | Between 2026-09-20 and 2026-11-01, the UK Electoral Commission or another UK regulator will open, or confirm it has opened, a formal investigation into the GBP72 million in Reform UK donations from Christopher Harborne and Ben Delo. | The Electoral Commission publishes, or the BBC, Guardian, or Financial Times report, confirmation that a UK regulator opened a formal investigation into the GBP72 million Reform UK donations between 2026-09-20 and 2026-11-01. |
| KKR-20260913-22 | 10% | 2026-10-13 | crime_security | Between 2026-09-20 and 2026-10-11, Hampshire police will arrest at least one of the six men whose images were released in connection with the Portsmouth violent-disorder incident. | Hampshire Constabulary, the BBC, or the Guardian report the arrest of at least one of the six men named in the Portsmouth violent-disorder appeal, with the arrest dated between 2026-09-20 and 2026-10-11. |
| KKR-20260913-23 | 31% | 2026-09-29 | disaster | Between 2026-09-14 and 2026-09-27, the confirmed death toll from the September 13, 2026 Java Sea ferry capsizing will reach or exceed 50. | BASARNAS, Reuters, AP, or Al Jazeera report a confirmed death toll of 50 or more from the September 13, 2026 Java Sea ferry capsizing, dated between 2026-09-14 and 2026-09-27. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-09-21 and 2026-11-08, a US House or Senate committee will hold a formal hearing explicitly framed around AI safety or AI regula" → REJECTED: resolution offers alternative VENUES joined by 'or' (…house | or | senate committee…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

2035 issued all-time across 16 forecaster arms · 1699 open (79 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 657 issued · 619 open · 38 resolved · 18 hits / 20 misses · **Brier 0.280** against its own base rate 47.4% (climatological 0.249) · **skill -0.124**.

*21 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 657 | 619 | 38 | 18 | 20 | 0.280 | 47.4% | 0.249 | -0.124 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 259 | 130 | 120 | 26 | 94 | 0.195 | 21.7% | 0.170 | -0.151 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 60 | 60 | 0 | — | — | not computed | — | — | — |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 31 | 7 | 5 | 2 | 0.063 | 71.4% | 0.204 | +0.692 |
| manual/fable-5.1/unattested | 82 | 82 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 218 | 215 | 3 | 3 | 0 | 0.153 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 230 | 224 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 13 | 31 | 17 | 14 | 0.239 | 54.8% | 0.248 | +0.036 |
| manual/sonnet-5/unattested | 226 | 194 | 32 | 16 | 16 | 0.224 | 50.0% | 0.250 | +0.105 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*
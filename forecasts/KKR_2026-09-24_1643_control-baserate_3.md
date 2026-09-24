**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 241643Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-24_1520.md · forecaster: control/baserate · 8 accepted / 2 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260924-50 | 32% | 2026-11-17 | cyber | The Office of the Australian Information Commissioner (OAIC) will publicly confirm it has opened a Notifiable Data Breach or preliminary inquiry into the OpenAI agent intrusion at an Australian government Medicare-linked site, with confirmation occurring between 2026-09-24 and 2026-11-15. | OAIC's published register, a Commissioner statement, or an OAIC media release naming the OpenAI/Medicare incident and confirming an open inquiry, dated between 2026-09-24 and 2026-11-15, verified by 2026-11-17. |
| KKR-20260924-51 | 32% | 2026-11-02 | cyber | The CISA Known Exploited Vulnerabilities catalog will list a new entry for a TeamCity CVE with a dateAdded value between 2026-09-24 and 2026-10-31. | The public CISA KEV catalog (cisa.gov) shows a TeamCity-product CVE with dateAdded between 2026-09-24 and 2026-10-31, checked on 2026-11-02. |
| KKR-20260924-52 | 48% | 2026-12-17 | economics/markets | The 10-year US Treasury yield (Reference: 5.14 percent on the packet date, 2026-09-24) will close at or above 5.35 percent on at least one trading day between 2026-10-01 and 2026-12-15. | FRED series DGS10 or Treasury.gov's daily par yield curve shows a 10-year close at or above 5.35 percent for any date between 2026-10-01 and 2026-12-15, checked 2026-12-17. |
| KKR-20260924-53 | 48% | 2026-12-02 | economics/markets | Brent crude (Reference: 101.42 USD/bbl on the packet date, 2026-09-24) will settle below 95.00 USD/bbl on at least one trading day between 2026-10-01 and 2026-11-30. | ICE Brent front-month settlement price is below 95.00 USD/bbl on any trading day between 2026-10-01 and 2026-11-30, per ICE or EIA data, checked 2026-12-02. |
| KKR-20260924-54 | 39% | 2026-12-02 | political | The US Supreme Court will issue a ruling or order, granting or denying the Trump administration's application on third-country deportations, between 2026-09-24 and 2026-11-30. | The Supreme Court's public docket at supremecourt.gov shows an order or opinion disposing of the third-country-deportation application, dated between 2026-09-24 and 2026-11-30, checked 2026-12-02. |
| KKR-20260924-55 | 39% | 2026-11-17 | political | A federal judge will hold the White House or Trump administration officials in contempt for violating the press-access restoration order, between 2026-09-24 and 2026-11-15. | A federal district or appellate court issues a contempt finding against White House or administration officials tied to the CNN, MS NOW, and Politico access order, dated 2026-09-24 to 2026-11-15, per court docket, checked 2026-11-17. |
| KKR-20260924-56 | 29% | 2026-11-17 | crime/security | UK police or the Crown Prosecution Service will formally charge Daniel Thomas in connection with the Channel dinghy-slashing arrest, between 2026-09-24 and 2026-11-15. | A CPS charging announcement or UK police statement confirms Daniel Thomas has been charged over the dinghy-slashing incident, dated 2026-09-24 to 2026-11-15, per news report, checked 2026-11-17. |
| KKR-20260924-57 | 31% | 2026-10-10 | disaster | The GDACS wildfire alert for event ID 1032372 in Brazil will be upgraded from Green to Orange or Red, between 2026-09-24 and 2026-10-08. | The GDACS report page for eventid=1032372 at gdacs.org shows an Orange or Red alert level at any point between 2026-09-24 and 2026-10-08, checked 2026-10-10. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "A named airport in the Gulf or Middle East region will suspend, reduce, or issue a NOTAM-based flight restriction explicitly citing an Irani" → REJECTED: resolution offers alternative VENUES joined by 'or' (…a wire service such as reuters, ap, | or | afp, or an aviation authority notam database,…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "The Saudi-led coalition will report intercepting or shooting down at least one additional Houthi-launched ballistic missile aimed at Saudi t" → REJECTED: resolution offers alternative VENUES joined by 'or' (…he saudi press agency, a coalition statement, | or | a wire service such as reuters or afp reports…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

2824 issued all-time across 17 forecaster arms · 2282 open (170 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 990 issued · 873 open · 85 resolved · 50 hits / 35 misses · **Brier 0.327** against its own base rate 58.8% (climatological 0.242) · **skill -0.352**.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 990 | 873 | 85 | 50 | 35 | 0.327 | 58.8% | 0.242 | -0.352 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 329 | 179 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 113 | 108 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 27 | 18 | 10 | 8 | 0.189 | 55.6% | 0.247 | +0.235 |
| manual/fable-5 | 38 | 27 | 11 | 6 | 5 | 0.101 | 54.5% | 0.248 | +0.591 |
| manual/fable-5.1/unattested | 181 | 164 | 9 | 6 | 3 | 0.176 | 66.7% | 0.222 | +0.209 |
| manual/fable-5/unattested | 258 | 237 | 12 | 11 | 1 | 0.214 | 91.7% | 0.076 | -1.797 |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5.5/unattested | 10 | 10 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 301 | 15 | 11 | 4 | 0.235 | 73.3% | 0.196 | -0.199 |
| manual/sonnet-5 | 45 | 9 | 35 | 18 | 17 | 0.247 | 51.4% | 0.250 | +0.009 |
| manual/sonnet-5/unattested | 314 | 250 | 59 | 31 | 28 | 0.238 | 52.5% | 0.249 | +0.047 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*
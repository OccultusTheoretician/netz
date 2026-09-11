**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 112239Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-11_1518.md · forecaster: control/baserate · 7 accepted / 2 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260911-21 | 56% | 2026-12-08 | military_conflict | A ceasefire or truce between the United States or Israel and Iran, formally announced by a government of a combatant state with a stated effective date, takes effect between 2026-09-18 and 2026-12-03. | Reuters, AP, or AFP report a formal ceasefire or truce between the US/Israel and Iran with a stated effective date inside the 2026-09-18 to 2026-12-03 window, confirmed by two of the three outlets. |
| KKR-20260911-22 | 56% | 2026-10-20 | military_conflict | The Royal Saudi Air Force conducts a direct airstrike on Houthi-held positions at Mocha, Dhubab, or Perim Island on the Red Sea coast of Yemen between 2026-09-18 and 2026-10-16. | Two of Reuters, AP, AFP, or Al Jazeera report a Saudi strike specifically on Mocha, Dhubab, or Perim Island between 2026-09-18 and 2026-10-16; strikes elsewhere in Yemen do not qualify. |
| KKR-20260911-23 | 26% | 2026-10-30 | economic | The Federal Reserve raises the federal funds target range above its current 3.50-3.75 percent level at the October 27-28, 2026 FOMC meeting. Reference: 3.50-3.75 percent, held since the July 2026 meeting. | The FOMC post-meeting statement released 2026-10-28 sets the federal funds target range above 3.50-3.75 percent, per the Federal Reserve press release. |
| KKR-20260911-24 | 28% | 2026-10-27 | cyber | CISA adds a PaperCut NG or MF vulnerability to the Known Exploited Vulnerabilities catalog with a dateAdded value between 2026-09-18 and 2026-10-23. | The CISA KEV catalog JSON feed lists a PaperCut NG/MF CVE with dateAdded between 2026-09-18 and 2026-10-23. |
| KKR-20260911-25 | 28% | 2026-10-20 | cyber | CISA adds a Cisco Secure Firewall Management Center vulnerability to the Known Exploited Vulnerabilities catalog with a dateAdded value between 2026-09-18 and 2026-10-16. | The CISA KEV catalog JSON feed lists a Cisco Secure Firewall Management Center CVE with dateAdded between 2026-09-18 and 2026-10-16. |
| KKR-20260911-26 | 35% | 2026-11-13 | political | Republicans retain a majority of seats in the US House of Representatives as elected on November 3, 2026. | AP or a majority of major US television networks call the 2026 House majority for the Republican Party, 218 or more seats, by the deadline. |
| KKR-20260911-27 | 10% | 2026-12-15 | crime_security | At least one of the six Nigerian nationals extradited to the United States on September 11, 2026 in the Black Axe romance-scam case pleads guilty or is convicted at trial between 2026-09-18 and 2026-12-11. | The US District Court docket (PACER) for the case shows a guilty plea or trial conviction entered for at least one defendant between 2026-09-18 and 2026-12-11. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "WTI crude oil settles at or above 110.00 USD per barrel on at least one trading day between 2026-09-18 and 2026-10-16. Reference: 99.63 on t" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "The DRC Ministry of Health or WHO confirms an Ebola virus disease case in an eighth distinct DRC province, beyond the seven already affected" → REJECTED: resolution offers alternative VENUES joined by 'or' (…a who disease outbreak news bulletin | or | drc ministry of health situation report confi…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

1907 issued all-time across 16 forecaster arms · 1571 open (63 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 603 issued · 565 open · 38 resolved · 18 hits / 20 misses · **Brier 0.280** against its own base rate 47.4% (climatological 0.249) · **skill -0.124**.

*21 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 603 | 565 | 38 | 18 | 20 | 0.280 | 47.4% | 0.249 | -0.124 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 254 | 125 | 120 | 26 | 94 | 0.195 | 21.7% | 0.170 | -0.151 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 45 | 45 | 0 | — | — | not computed | — | — | — |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 31 | 7 | 5 | 2 | 0.063 | 71.4% | 0.204 | +0.692 |
| manual/fable-5.1/unattested | 68 | 68 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 203 | 200 | 3 | 3 | 0 | 0.153 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 219 | 213 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 13 | 31 | 17 | 14 | 0.239 | 54.8% | 0.248 | +0.036 |
| manual/sonnet-5/unattested | 212 | 180 | 32 | 16 | 16 | 0.224 | 50.0% | 0.250 | +0.105 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*
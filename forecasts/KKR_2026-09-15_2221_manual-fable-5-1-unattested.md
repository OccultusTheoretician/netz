**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 152221Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-15_1544.md · forecaster: manual/fable-5.1/unattested · 9 accepted / 1 rejected by validation gate · 5 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260915-70 | 75% | 2026-10-19 | military_conflict | Between 2026-09-16 and 2026-10-15 at least one merchant vessel is attacked, boarded, hijacked, or seized in the Strait of Hormuz, Gulf of Oman, or Persian Gulf, and UKMTO records the incident. | The UKMTO incidents list (ukmto.org) shows an incident dated between 2026-09-16 and 2026-10-15 in the Strait of Hormuz, Gulf of Oman, or Persian Gulf classified as an attack, boarding, hijack, or seizure of a merchant vessel. |
| KKR-20260915-71 | 12% | 2026-12-17 | military_conflict | Between 2026-09-16 and 2026-12-15 forces of the internationally recognized Yemeni government or the Saudi-led coalition take control of the port of Hodeidah from the Houthis. | At least two of Reuters, AP, AFP report that Yemeni government-aligned or Saudi-led coalition forces took control of the port of Hodeidah from the Houthis on a date between 2026-09-16 and 2026-12-15. |
| KKR-20260915-72 | 15% | 2026-11-02 | military_conflict | Between 2026-09-16 and 2026-10-31 the governments of Russia and Ukraine each publicly announce agreement to halt strikes on energy infrastructure of the other side. | At least two of Reuters, AP, AFP report that both the Russian and Ukrainian governments announced, on dates between 2026-09-16 and 2026-10-31, agreement to halt strikes on energy infrastructure, bilateral or US-brokered. |
| KKR-20260915-73 | 30% | 2026-10-19 | political | Between 2026-09-16 and 2026-10-15 a round of talks between United States and Iranian government officials, direct or mediated, is held and publicly confirmed by both governments. | At least two of Reuters, AP, AFP report that the United States government and the Iranian Foreign Ministry each confirmed a round of US-Iran talks, direct or mediated, held between 2026-09-16 and 2026-10-15. |
| KKR-20260915-74 | 15% | 2026-11-17 | political | Between 2026-09-16 and 2026-11-13 the United Nations Security Council adopts a resolution whose text names the Strait of Hormuz. | The Security Council resolutions list for 2026 (un.org/securitycouncil/content/resolutions) includes a resolution adopted between 2026-09-16 and 2026-11-13 whose preambular or operative text names the Strait of Hormuz. |
| KKR-20260915-75 | 75% | 2026-10-20 | economic | The 10-year Treasury constant maturity yield (FRED series DGS10) prints 5.00 percent or higher on at least one observation dated 2026-09-16 through 2026-10-16. Reference: 4.99 percent on the packet date. | FRED series DGS10 shows at least one observation dated 2026-09-16 through 2026-10-16 with a value of 5.00 or greater. Reference: 4.99 percent on the packet date. |
| KKR-20260915-76 | 65% | 2026-10-19 | cyber | Between 2026-09-16 and 2026-10-15 CISA adds to the Known Exploited Vulnerabilities catalog at least one entry with vendorProject Google and a product field containing Chrome or Chromium. | The CISA KEV catalog JSON feed contains an entry with vendorProject Google, a product field containing Chrome or Chromium, and a dateAdded between 2026-09-16 and 2026-10-15 inclusive. |
| KKR-20260915-77 | 25% | 2026-10-19 | crime_security | Between 2026-09-16 and 2026-10-15 Dutch authorities announce the arrest of at least one suspect in connection with the suspected sabotage that disrupted Netherlands rail traffic on 2026-09-15. | At least two of Reuters, AP, AFP, NOS report that the Netherlands Public Prosecution Service or Dutch police announced, between 2026-09-16 and 2026-10-15, the arrest of a suspect for the 2026-09-15 rail sabotage. |
| KKR-20260915-78 | 45% | 2026-12-17 | disaster_infrastructure | Between 2026-09-16 and 2026-12-15 a flood event in Kenya, Somalia, or Ethiopia carries a GDACS alert level of Orange or Red. | The GDACS event list (gdacs.org, eventtype FL) shows a flood event in Kenya, Somalia, or Ethiopia at Orange or Red alert level whose event period includes at least one day between 2026-09-16 and 2026-12-15. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The Federal Open Market Committee statement issued on 2026-10-28 announces an increase in the target range for the federal funds rate." → REJECTED: measurable claim without a numeric threshold — a row about a quantity must state the number next to its comparator; identifier digits (H.15, S&P 500) do not count

## III. LEDGER STANDING

2217 issued all-time across 16 forecaster arms · 1881 open (101 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/fable-5.1/unattested`:** 105 issued · 105 open · nothing resolved yet — this arm earns a score at its first resolution.

*21 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 732 | 694 | 38 | 18 | 20 | 0.280 | 47.4% | 0.249 | -0.124 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 273 | 144 | 120 | 26 | 94 | 0.195 | 21.7% | 0.170 | -0.151 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 69 | 69 | 0 | — | — | not computed | — | — | — |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 31 | 7 | 5 | 2 | 0.063 | 71.4% | 0.204 | +0.692 |
| manual/fable-5.1/unattested | 105 | 105 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 240 | 237 | 3 | 3 | 0 | 0.153 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 253 | 247 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 13 | 31 | 17 | 14 | 0.239 | 54.8% | 0.248 | +0.036 |
| manual/sonnet-5/unattested | 242 | 210 | 32 | 16 | 16 | 0.224 | 50.0% | 0.250 | +0.105 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*
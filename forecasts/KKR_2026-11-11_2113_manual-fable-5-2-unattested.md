**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 112113Z NOV 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-11-11_1613.md · forecaster: manual/fable-5.2/unattested · 4 accepted / 6 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261111-48 | 15% | 2026-12-14 | economics/markets | The Federal Open Market Committee lowers the federal funds target range at its scheduled meeting concluding on 2026-12-09. | TRUE if FRED series DFEDTARU shows a lower value for 2026-12-10 than for 2026-12-08. |
| KKR-20261111-49 | 30% | 2026-12-15 | economics/markets | The 10-year Treasury constant maturity yield prints at or above 5.25 percent on at least one trading day between 2026-11-12 and 2026-12-11. Reference: 5.00 percent on the packet date. | TRUE if any FRED DGS10 daily observation dated between 2026-11-12 and 2026-12-11 is 5.25 or higher. Reference: 5.00 percent on the packet date. |
| KKR-20261111-50 | 66% | 2026-12-07 | economics/markets | Anthropic prices its initial public offering, evidenced by a final prospectus on Form 424B4 filed with the SEC, between 2026-11-12 and 2026-12-04. | TRUE if SEC EDGAR lists a Form 424B4 filed by Anthropic with a filing date between 2026-11-12 and 2026-12-04. |
| KKR-20261111-51 | 42% | 2026-12-14 | cyber | CISA adds a Xen Orchestra vulnerability to its Known Exploited Vulnerabilities catalog between 2026-11-12 and 2026-12-11. | TRUE if the CISA KEV catalog JSON contains an entry naming Xen Orchestra in its product or vulnerabilityName field with a dateAdded value between 2026-11-12 and 2026-12-11. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Russia and Ukraine carry out at least one prisoner exchange, with prisoners physically transferred, between 2026-11-12 and 2026-11-27." → REJECTED: resolution offers alternative VENUES joined by 'or' (…-11-12 and 2026-11-27, as reported by reuters | or | ap…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "The United States announces a suspension or lifting of its blockade on Iran between 2026-11-12 and 2026-12-15." → REJECTED: resolution offers alternative VENUES joined by 'or' (…blockade on iran is  , as reported by reuters | or | ap…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "Certified Mississippi results for the 2026-11-03 US Senate general election, published between 2026-11-12 and 2026-12-18, show Scott Colom w" → REJECTED: measurable claim without a numeric threshold — a row about a quantity must state the number next to its comparator; identifier digits (H.15, S&P 500) do not count
- "Pete Hegseth resigns, is dismissed, or has his departure as US Defense Secretary publicly announced between 2026-11-12 and 2026-12-31." → REJECTED: resolution offers alternative VENUES joined by 'or' (… 2026-11-12 and 2026-12-31, as reported by ap | or | reuters…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "Italian authorities arrest or formally charge at least one person over the email bomb threats sent to Italian schools on 2026-11-11, between" → REJECTED: resolution offers alternative VENUES joined by 'or' (…b threat emails, as reported by ansa, reuters | or | ap…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "The Ebola outbreak in Kenya is officially declared over by the World Health Organization or the Kenyan Ministry of Health between 2026-11-12" → REJECTED: resolution offers alternative VENUES joined by 'or' (…int, reuters | or | ap…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

5644 issued all-time across 23 forecaster arms · 3922 open (1598 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/fable-5.2/unattested`:** 12 issued · 12 open · nothing resolved yet — this arm earns a score at its first resolution.

*96 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1788 | 1279 | 477 | 273 | 204 | 0.300 | 57.2% | 0.245 | -0.226 |
| control/trailing | 174 | 174 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 9 | 11 | 1 | 10 | 0.123 | 9.1% | 0.083 | -0.490 |
| lmstudio/auto[post-window] | 470 | 201 | 259 | 75 | 184 | 0.204 | 29.0% | 0.206 | +0.009 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 201 | 184 | 11 | 4 | 7 | 0.227 | 36.4% | 0.231 | +0.020 |
| lmstudio/qwen36-abliterated | 209 | 207 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
| lmstudio/qwen36-realist | 183 | 150 | 31 | 10 | 21 | 0.242 | 32.3% | 0.219 | -0.106 |
| lmstudio/realist | 249 | 128 | 119 | 66 | 53 | 0.317 | 55.5% | 0.247 | -0.285 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 14 | 24 | 14 | 10 | 0.164 | 58.3% | 0.243 | +0.325 |
| manual/fable-5.1/unattested | 526 | 411 | 107 | 61 | 46 | 0.211 | 57.0% | 0.245 | +0.140 |
| manual/fable-5.2/unattested | 12 | 12 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 258 | 147 | 102 | 65 | 37 | 0.203 | 63.7% | 0.231 | +0.121 |
| manual/opus-5 | 74 | 39 | 35 | 18 | 17 | 0.213 | 51.4% | 0.250 | +0.146 |
| manual/opus-5.5/unattested | 381 | 367 | 14 | 8 | 6 | 0.312 | 57.1% | 0.245 | -0.275 |
| manual/opus-5/unattested | 326 | 221 | 95 | 61 | 34 | 0.208 | 64.2% | 0.230 | +0.097 |
| manual/sonnet-5 | 45 | 3 | 41 | 22 | 19 | 0.250 | 53.7% | 0.249 | -0.007 |
| manual/sonnet-5.5/unattested | 222 | 207 | 15 | 10 | 5 | 0.122 | 66.7% | 0.222 | +0.451 |
| manual/sonnet-5/unattested | 342 | 141 | 196 | 98 | 98 | 0.245 | 50.0% | 0.250 | +0.019 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*
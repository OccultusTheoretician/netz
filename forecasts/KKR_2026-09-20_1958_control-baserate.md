**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 201958Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-20_1517.md · forecaster: control/baserate · 6 accepted / 4 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260920-20 | 61% | 2026-10-07 | military/conflict | Between 2026-09-21 and 2026-10-04, the Russian Ministry of Defense or the Moscow mayor reports 100 or more Ukrainian UAVs intercepted over Moscow city or Moscow Oblast on a single calendar day. | True if a Russian MoD or Moscow mayoral statement, carried by Reuters or AP, gives a single-day Moscow-region intercept count of 100 or more for any day 2026-09-21 to 2026-10-04. |
| KKR-20260920-21 | 61% | 2026-10-07 | military/conflict | Between 2026-09-21 and 2026-10-04, the Saudi Ministry of Defense announces the interception or impact of at least one Houthi-claimed drone or missile directed at Riyadh. Reference: Riyadh airport smoke and Houthi claim on 2026-09-19. | True if Saudi Press Agency publishes a MoD statement on a drone or missile aimed at Riyadh in the window and Reuters or AP carries it. |
| KKR-20260920-22 | 24% | 2026-10-20 | economics/markets | The NYMEX WTI front-month contract settles below 90.00 dollars on at least one trading day between 2026-09-21 and 2026-10-16. Reference: 96.08 on the packet date after a 9.21 percent one-day fall. | True if the CME Group official settlement for front-month WTI is below 90.00 on any trading day 2026-09-21 to 2026-10-16. |
| KKR-20260920-23 | 24% | 2026-11-03 | economics/markets | The 10-year US Treasury constant-maturity yield (FRED series DGS10) closes at or above 5.25 percent on at least one day between 2026-09-21 and 2026-10-30. Reference: 5.00 percent on the packet date. | True if any DGS10 daily value dated 2026-09-21 to 2026-10-30 is 5.25 or higher. |
| KKR-20260920-24 | 29% | 2026-10-06 | cyber | The CISA KEV catalog gains an entry with a date-added value between 2026-09-21 and 2026-10-02 for a vulnerability whose product field names an npm package, the npm CLI, or the Node.js runtime. | True if the CISA KEV JSON feed contains an entry with dateAdded in the window and a product or vendor field matching npm or Node.js. |
| KKR-20260920-25 | 29% | 2026-10-08 | cyber | Between 2026-09-21 and 2026-10-05, OpenAI publishes a security advisory, changelog entry, or blog post acknowledging a Codex sandbox escape and stating a fix or mitigation. | True if a page on an openai.com domain dated in the window references a Codex sandbox escape and a fix, and BleepingComputer or The Hacker News reports the publication. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Friedrich Merz ceases to hold the office of German Chancellor, by resignation or a successful Bundestag constructive vote of no confidence, " → REJECTED: resolution offers alternative VENUES joined by 'or' (…bundestag official record | or | bundesregierung…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "The sister of Imran Khan arrested on 2026-09-20 is released from custody, by bail or discharge, between 2026-09-21 and 2026-10-04." → REJECTED: resolution offers alternative VENUES joined by 'or' (…dawn and one wire service (reuters | or | ap) report her release from custody within th…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact; the resolution names a different subject than the statement — the claim is about Imran, Khan and the resolution settles on AP, Dawn, Reuters. A row whose resolution checks a different fact can be scored correct while being wrong
- "At least one person is formally charged with murder in a New South Wales court in connection with the Blue Mountains stabbing of 2026-09-20," → REJECTED: cited items name Australia; the claim is about United Kingdom — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else
- "USGS records an earthquake of magnitude 6.0 or greater with epicenter within 250 km of the 2026-09-20 M6.4 Kainantu, Papua New Guinea event," → REJECTED: the resolution names a different subject than the statement — the claim is about Guinea, Kainantu, New, Papua and the resolution settles on USGS, us7000tiqc. A row whose resolution checks a different fact can be scored correct while being wrong

## III. LEDGER STANDING

2571 issued all-time across 16 forecaster arms · 2105 open (164 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 882 issued · 797 open · 53 resolved · 25 hits / 28 misses · **Brier 0.267** against its own base rate 47.2% (climatological 0.249) · **skill -0.071**.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 882 | 797 | 53 | 25 | 28 | 0.267 | 47.2% | 0.249 | -0.071 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 13 | 7 | 1 | 6 | 0.155 | 14.3% | 0.122 | -0.269 |
| lmstudio/auto[post-window] | 309 | 159 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 96 | 91 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 30 | 8 | 5 | 3 | 0.066 | 62.5% | 0.234 | +0.717 |
| manual/fable-5.1/unattested | 147 | 137 | 2 | 0 | 2 | 0.156 | 0.0% | 0.000 | — |
| manual/fable-5/unattested | 258 | 242 | 7 | 7 | 0 | 0.178 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5/unattested | 299 | 282 | 7 | 5 | 2 | 0.137 | 71.4% | 0.204 | +0.329 |
| manual/sonnet-5 | 45 | 11 | 33 | 18 | 15 | 0.249 | 54.5% | 0.248 | -0.004 |
| manual/sonnet-5/unattested | 277 | 229 | 43 | 21 | 22 | 0.207 | 48.8% | 0.250 | +0.172 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*
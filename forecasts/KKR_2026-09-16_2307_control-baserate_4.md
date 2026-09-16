**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 162307Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-16_1517.md · forecaster: control/baserate · 5 accepted / 4 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260916-71 | 29% | 2026-11-17 | cyber | CenterPoint Energy Inc. will file a disclosure with the US Securities and Exchange Commission (an 8-K, 8-K/A, or 10-Q) between 2026-09-23 and 2026-11-15 that states a specific number of individuals, customers, or records affected by the cyberattack disclosed around 2026-09-15, and that number will exceed 100000. | TRUE if SEC EDGAR full-text search shows a CenterPoint Energy Inc. (NYSE: CNP) filing dated between 2026-09-23 and 2026-11-15 that discloses a specific affected-individual or affected-record count for the cyberattack first reported 2026-09-15, and the stated count exceeds 100000; FALSE otherwise, including if no quantified figure is filed by the deadline. |
| KKR-20260916-72 | 24% | 2026-10-22 | economics/markets | WTI crude oil (NYMEX front-month futures) will record a settlement price at or above 110.00 USD per barrel on at least one trading day between 2026-09-23 and 2026-10-21. Reference: 101.87 USD per barrel on the packet date, 2026-09-16. | TRUE if the NYMEX WTI front-month futures settlement price (as published by CME Group or the US Energy Information Administration) equals or exceeds 110.00 USD per barrel on any trading day from 2026-09-23 through 2026-10-21 inclusive; FALSE otherwise. |
| KKR-20260916-73 | 24% | 2026-10-22 | economics/markets | The US 10-year Treasury note yield will close at or above 5.10 percent on at least one trading day between 2026-09-23 and 2026-10-21. Reference: 4.96 percent on the packet date, 2026-09-16. | TRUE if the US Treasury Daily Par Yield Curve Rates (treasury.gov) or a major financial data provider (Bloomberg, Reuters) shows the 10-year Treasury yield closing at or above 5.10 percent on any trading day from 2026-09-23 through 2026-10-21 inclusive; FALSE otherwise. |
| KKR-20260916-74 | 40% | 2026-11-13 | political | Democrats will win a majority of seats in the US Senate in the 2026 midterm elections held on 2026-11-03, as called by the Associated Press or a majority of major US television networks (ABC, CBS, NBC, CNN, Fox). | TRUE if, by the deadline, the Associated Press or a majority of the named networks have called Senate control for the Democratic Party (caucus, including independents caucusing with Democrats, holding 51 or more seats, or 50 seats with a Democratic Vice President tie-break) following the 2026-11-03 election; FALSE otherwise, including if control remains uncalled or is called for Republicans. |
| KKR-20260916-75 | 23% | 2026-12-17 | crime/security | The US Department of the Treasury Office of Foreign Assets Control will designate at least one additional Russian individual or entity, in a press release or Federal Register notice that explicitly references the assassination-plot allegation against Ukrainian-aligned individuals overseas reported around 2026-09-16, with the designation dated between 2026-09-23 and 2026-12-15. | TRUE if OFAC (via a Treasury press release or a Federal Register notice) designates at least one Russian individual or entity and the designation text explicitly references the assassination or targeted-killing plot against Ukraine-aligned individuals abroad first reported around 2026-09-16, with the designation dated between 2026-09-23 and 2026-12-15; FALSE otherwise, including if new Russia-related designations occur in this window without explicit reference to this specific allegation. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The CISA Known Exploited Vulnerabilities catalog will add at least one new CVE entry for a remote access, remote support, or remote monitori" → REJECTED: the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-58704 dateAdded 2026-09-16, before the claimed window 2026-09-23..2026-10-21; dateAdded is single-valued and a fresh in-window value would require removal-and-relisting, which has no documented precedent (removals exist: CVE-2022-28958, removed 2023-12-01)
- "A Houthi-launched missile, drone, or projectile will impact, be credibly reported as inbound toward, or be intercepted within 50 kilometers " → REJECTED: cited items name Djibouti, Iran, Islamic Republic of, Yemen; the claim is about Saudi Arabia — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else; resolution offers alternative VENUES joined by 'or' (… independent wire services (reuters, ap, afp) | or | two opposing-side channels report a houthi-at…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "The European Commission will publish a formal proposal document (a Commission Communication, draft Council Decision, or equivalent published" → REJECTED: measurable claim without a numeric threshold — a row about a quantity must state the number next to its comparator; identifier digits (H.15, S&P 500) do not count
- "GDACS (Global Disaster Alert and Coordination System) will issue a wildfire alert at Orange or Red level, above the Green level shown for Za" → REJECTED: measurable claim without a numeric threshold — a row about a quantity must state the number next to its comparator; identifier digits (H.15, S&P 500) do not count

## III. LEDGER STANDING

2301 issued all-time across 16 forecaster arms · 1899 open (61 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 773 issued · 720 open · 53 resolved · 25 hits / 28 misses · **Brier 0.267** against its own base rate 47.2% (climatological 0.249) · **skill -0.071**.

*21 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 773 | 720 | 53 | 25 | 28 | 0.267 | 47.2% | 0.249 | -0.071 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 13 | 7 | 1 | 6 | 0.155 | 14.3% | 0.122 | -0.269 |
| lmstudio/auto[post-window] | 280 | 130 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 73 | 68 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 30 | 8 | 5 | 3 | 0.066 | 62.5% | 0.234 | +0.717 |
| manual/fable-5.1/unattested | 113 | 111 | 2 | 0 | 2 | 0.156 | 0.0% | 0.000 | — |
| manual/fable-5/unattested | 249 | 242 | 7 | 7 | 0 | 0.178 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5/unattested | 263 | 256 | 7 | 5 | 2 | 0.137 | 71.4% | 0.204 | +0.329 |
| manual/sonnet-5 | 45 | 11 | 33 | 18 | 15 | 0.249 | 54.5% | 0.248 | -0.004 |
| manual/sonnet-5/unattested | 247 | 204 | 43 | 21 | 22 | 0.207 | 48.8% | 0.250 | +0.172 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*
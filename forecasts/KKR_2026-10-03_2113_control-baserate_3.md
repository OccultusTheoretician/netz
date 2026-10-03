**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 032113Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-03_1517.md · forecaster: control/baserate · 6 accepted / 4 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261003-47 | 64% | 2026-10-20 | military_conflict | Between 2026-10-05 and 2026-10-18, Russian drone or missile strikes hit or damage a Dnipro River bridge in Kyiv on at least three separate calendar dates. | Kyiv Mayor Klitschko or the Kyiv City Military Administration, or two of Reuters, AP and BBC, report strikes hitting a Kyiv Dnipro bridge on three or more separate dates between 2026-10-05 and 2026-10-18. |
| KKR-20261003-48 | 39% | 2026-10-12 | political | In the Brazilian presidential first round held on 2026-10-04, no candidate receives more than 50 percent of valid votes, so a runoff is required. | Brazil Superior Electoral Court (TSE) first-round results for 2026-10-04 show every presidential candidate at or below 50 percent of valid votes, triggering the runoff. |
| KKR-20261003-49 | 48% | 2026-11-02 | economic | ICE Brent December 2026 futures settle below 95.00 USD per barrel on 2026-10-29. Reference: 102.25 USD per barrel in the packet market snapshot dated 2026-10-03. | The ICE official settlement price for Brent December 2026 futures on 2026-10-29 is below 95.00 USD per barrel. |
| KKR-20261003-50 | 32% | 2026-11-10 | cyber | CISA adds a GitLab vulnerability to the Known Exploited Vulnerabilities catalog with a dateAdded between 2026-10-05 and 2026-11-06. | The CISA KEV catalog JSON carries at least one entry with vendorProject GitLab and a dateAdded value between 2026-10-05 and 2026-11-06 inclusive. |
| KKR-20261003-51 | 31% | 2026-11-04 | disaster_infrastructure | Between 2026-10-05 and 2026-11-01, the National Hurricane Center classifies at least one Atlantic tropical cyclone at hurricane intensity, meaning maximum sustained winds of at least 74 mph. | An NHC advisory issued between 2026-10-05 and 2026-11-01 lists an Atlantic tropical cyclone with maximum sustained winds of at least 74 mph. |
| KKR-20261003-52 | 39% | 2026-11-06 | political | Ken Paxton wins the most votes in the Texas U.S. Senate general election held on 2026-11-03. | The Texas Secretary of State results page, viewed on 2026-11-06, shows Ken Paxton with the highest vote total in the U.S. Senate race held on 2026-11-03, counting unofficial returns. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Likud wins strictly more Knesset seats than any other party list in the Israeli election held on 2026-10-27." → REJECTED: measurable claim without a numeric threshold — a row about a quantity must state the number next to its comparator; identifier digits (H.15, S&P 500) do not count
- "The FOMC raises the federal funds target range above 3.75 to 4.00 percent at its policy decision dated 2026-10-28. Reference: target range 3" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "Between 2026-10-05 and 2026-11-06, at least one person arrested in the counter-terrorism investigation into the 2026-09-27 incident near RAF" → REJECTED: resolution offers alternative VENUES joined by 'or' (… policing, the crown prosecution service, bbc | or | pa report that a person arrested over the 202…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "CISA adds at least one Microsoft vulnerability to the Known Exploited Vulnerabilities catalog with a dateAdded between 2026-10-06 and 2026-1" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim

## III. LEDGER STANDING

3322 issued all-time across 18 forecaster arms · 2780 open (497 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 1193 issued · 1076 open · 85 resolved · 50 hits / 35 misses · **Brier 0.327** against its own base rate 58.8% (climatological 0.242) · **skill -0.352**.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1193 | 1076 | 85 | 50 | 35 | 0.327 | 58.8% | 0.242 | -0.352 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 368 | 218 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 166 | 161 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 27 | 18 | 10 | 8 | 0.189 | 55.6% | 0.247 | +0.235 |
| manual/fable-5 | 38 | 27 | 11 | 6 | 5 | 0.101 | 54.5% | 0.248 | +0.591 |
| manual/fable-5.1/unattested | 250 | 233 | 9 | 6 | 3 | 0.176 | 66.7% | 0.222 | +0.209 |
| manual/fable-5/unattested | 258 | 237 | 12 | 11 | 1 | 0.214 | 91.7% | 0.076 | -1.797 |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5.5/unattested | 78 | 78 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 301 | 15 | 11 | 4 | 0.235 | 73.3% | 0.196 | -0.199 |
| manual/sonnet-5 | 45 | 9 | 35 | 18 | 17 | 0.247 | 51.4% | 0.250 | +0.009 |
| manual/sonnet-5.5/unattested | 38 | 38 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 278 | 59 | 31 | 28 | 0.238 | 52.5% | 0.249 | +0.047 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*
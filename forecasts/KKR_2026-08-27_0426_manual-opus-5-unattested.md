**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 270426Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-26_1538.md · forecaster: manual/opus-5/unattested · 7 accepted / 3 rejected by validation gate · 1 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260827-13 | 32% | 2026-11-06 | military_conflict | A temporary joint Iran-Oman maritime corridor through the Strait of Hormuz becomes operational, carrying at least one vessel transit between 2026-09-01 and 2026-10-31. | The Oman News Agency or the Omani foreign ministry, and the Iranian foreign ministry, both state the corridor is in operation with at least one transit completed before 2026-11-01. |
| KKR-20260827-14 | 35% | 2026-12-04 | military_conflict | United States and Iranian officials hold a direct negotiating session, in person or by video link, between 2026-09-01 and 2026-11-30. | The State Department or White House and the Iranian foreign ministry each confirm a direct session inside the window. Relay through Omani or Qatari mediators alone does not count. |
| KKR-20260827-15 | 82% | 2026-11-06 | political | OFAC designates at least one foreign-registered company or non-Iranian-flagged vessel for facilitating Iranian oil sales, in an action dated between 2026-09-01 and 2026-10-31. | The OFAC Recent Actions page or an SDN list update dated inside the window adds at least one foreign-registered entity or non-Iranian-flagged vessel under an Iran-related program tag. |
| KKR-20260827-16 | 45% | 2026-11-04 | cyber | CISA catalogues a Microsoft SharePoint vulnerability as actively exploited, with a KEV date-added value between 2026-08-27 and 2026-10-31. | The CISA KEV catalog JSON holds an entry with vendorProject Microsoft, a product string naming SharePoint, and a dateAdded value between 2026-08-27 and 2026-10-31. |
| KKR-20260827-17 | 40% | 2026-10-20 | cyber | A named extortion group publicly claims the Boston Scientific intrusion by listing the company on a leak site between 2026-08-27 and 2026-10-15. | At least two of BleepingComputer, Cybersecurity Dive, Reuters, and The Record report a named group listing Boston Scientific on an extortion leak site inside the window. |
| KKR-20260827-18 | 38% | 2026-12-04 | crime_security | The Bureau of Industry and Security adds a party to the Entity List over diversion of advanced computing items or AI servers to China, published in the Federal Register between 2026-09-01 and 2026-11-30. | A Federal Register rule published inside the window adds at least one party to the Entity List with a justification resting on diversion of advanced computing items or AI servers to China. |
| KKR-20260827-19 | 45% | 2026-10-15 | disaster | The confirmed death toll in Nepal from the 2026-08-26 Bhotekoshi and Trishuli flooding reaches 300 or more, stated by a Nepali government body between 2026-08-27 and 2026-10-12. | The National Disaster Risk Reduction and Management Authority, the Home Ministry, or the Office of the Prime Minister of Nepal states a confirmed dead count of 300 or more for this event inside the window. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The FOMC raises the federal funds target range at its scheduled meeting on 2026-09-16, moving it above the 3.50 to 3.75 percent range held s" → REJECTED: event window opens 2026-07-29, before this row is sealed (2026-08-26, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "Europe Brent spot crude prints at or below 75.00 US dollars per barrel on at least one business day between 2026-09-01 and 2026-10-30." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; the resolution names only a venue or register (FRED, dcoilbrenteu) and no subject - the register is where to look, not what is claimed; name the subject inside it
- "Donald Trump and Vladimir Putin meet face to face between 2026-09-07 and 2026-12-18." → REJECTED: the resolution names a different subject than the statement — the claim is about Donald, Putin, Trump, Vladimir and the resolution settles on House, Kremlin, Phone, White. A row whose resolution checks a different fact can be scored correct while being wrong

## III. LEDGER STANDING

942 issued all-time across 14 forecaster arms · 852 open (75 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/opus-5/unattested`:** 113 issued · 113 open · nothing resolved yet — this arm earns a score at its first resolution.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 186 | 178 | 8 | 1 | 7 | 0.125 | 12.5% | 0.109 | -0.143 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 20 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-window] | 152 | 140 | 10 | 2 | 8 | 0.240 | 20.0% | 0.160 | -0.502 |
| lmstudio/auto[pre-verbot] | 60 | 13 | 39 | 12 | 27 | 0.225 | 30.8% | 0.213 | -0.054 |
| manual/fable | 45 | 36 | 9 | 4 | 5 | 0.190 | 44.4% | 0.247 | +0.232 |
| manual/fable-5 | 38 | 38 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 90 | 90 | 0 | — | — | not computed | — | — | — |
| manual/opus-5 | 74 | 72 | 2 | 1 | 1 | 0.243 | 50.0% | 0.250 | +0.030 |
| manual/opus-5/unattested | 113 | 113 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 45 | 39 | 6 | 3 | 3 | 0.270 | 50.0% | 0.250 | -0.081 |
| manual/sonnet-5/unattested | 102 | 101 | 1 | 0 | 1 | 0.040 | 0.0% | 0.000 | — |
| operator/human | 6 | 2 | 1 | 1 | 0 | 0.122 | 100.0% | 0.000 | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*
**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 170209Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-16_1516.md · forecaster: manual/opus-5/unattested · 5 accepted / 5 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260817-11 | 30% | 2026-09-24 | military_conflict | Ukrainian long-range strikes halt loadings at a named Russian crude export terminal - Novorossiysk, Tuapse, Primorsk, or Ust-Luga - with the strike occurring between 2026-08-24 and 2026-09-21. | Reuters or Bloomberg reports suspended loadings at one of those four terminals attributed to a strike inside the window, and a Russian federal or regional official confirms the attack, by 2026-09-24. |
| KKR-20260817-12 | 30% | 2026-11-02 | economic | ICE Brent front-month futures settle at or above USD 100.00 per barrel on at least one trading session between 2026-08-24 and 2026-10-30. | The ICE Futures Europe published daily settlement for the front-month Brent contract reaches 100.00 or higher on any session in that range, checked 2026-11-02. |
| KKR-20260817-13 | 25% | 2026-08-24 | economic | Walmart reports Walmart US comparable sales excluding fuel of 4.5 percent or higher for fiscal Q2 2027 in its scheduled 2026-08-20 earnings release. | The Q2 FY27 earnings release furnished on Form 8-K to SEC EDGAR states Walmart US comparable sales excluding fuel at or above 4.5 percent, checked 2026-08-24. |
| KKR-20260817-14 | 30% | 2027-01-20 | political | FDA publishes a Federal Register document on the FSMA Section 204 food traceability rule - proposed rule, final rule, or request for information - between 2026-08-24 and 2027-01-15. | federalregister.gov lists an FDA document naming food traceability in its title or abstract with a publication date inside that range, checked 2027-01-20. |
| KKR-20260817-15 | 40% | 2026-10-08 | crime_security | A second person is charged over the 2026-08-15 Virginia State University shooting, with the charges filed between 2026-08-17 and 2026-10-05. | Chesterfield County Police, the Commonwealth Attorney, or Virginia online court records show charges against a second defendant filed inside that range, checked 2026-10-08. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "A commercial vessel sinks or is abandoned by its crew following an attack in the Strait of Hormuz, Gulf of Oman, or Persian Gulf between 202" → REJECTED: the resolution names a different subject than the statement — the claim is about Gulf, Hormuz, Oman, Persian and the resolution settles on List, Lloyds, Reuters, UKMTO. A row whose resolution checks a different fact can be scored correct while being wrong
- "The CISA Known Exploited Vulnerabilities catalog gains at least one entry naming Apple as the vendor, with a date added between 2026-08-24 a" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "The United States publishes a formal instrument asserting sovereignty, territorial claim, or protectorate status over the Strait of Hormuz b" → REJECTED: the resolution names a different subject than the statement — the claim is about Hormuz, States, Strait, United and the resolution settles on Federal, House, Register, White. A row whose resolution checks a different fact can be scored correct while being wrong
- "USGS catalogs at least one magnitude 6.0 or greater earthquake within 250 km of the 2026-08-15 Flores mainshock, event us6000tkt2, with orig" → REJECTED: the resolution names only a venue or register (USGS) and no subject - the register is where to look, not what is claimed; name the subject inside it
- "The Indonesian disaster agency BNPB puts the confirmed death toll from the 2026-08-15 Flores earthquake at 100 or more, in a figure issued o" → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-09-08 exactly. Price a day, not a window: widen the window or state why the date is fixed

## III. LEDGER STANDING

649 issued all-time across 14 forecaster arms · 559 open (5 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/opus-5/unattested`:** 60 issued · 60 open · nothing resolved yet — this arm earns a score at its first resolution.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 121 | 113 | 8 | 1 | 7 | 0.125 | 12.5% | 0.109 | -0.143 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 20 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-window] | 82 | 70 | 10 | 2 | 8 | 0.240 | 20.0% | 0.160 | -0.502 |
| lmstudio/auto[pre-verbot] | 60 | 13 | 39 | 12 | 27 | 0.225 | 30.8% | 0.213 | -0.054 |
| manual/fable | 45 | 36 | 9 | 4 | 5 | 0.190 | 44.4% | 0.247 | +0.232 |
| manual/fable-5 | 38 | 38 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 40 | 40 | 0 | — | — | not computed | — | — | — |
| manual/opus-5 | 74 | 72 | 2 | 1 | 1 | 0.243 | 50.0% | 0.250 | +0.030 |
| manual/opus-5/unattested | 60 | 60 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 45 | 39 | 6 | 3 | 3 | 0.270 | 50.0% | 0.250 | -0.081 |
| manual/sonnet-5/unattested | 47 | 46 | 1 | 0 | 1 | 0.040 | 0.0% | 0.000 | — |
| operator/human | 6 | 2 | 1 | 1 | 0 | 0.122 | 100.0% | 0.000 | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*
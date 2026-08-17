**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 170209Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-16_1516.md · forecaster: control/baserate · 5 accepted / 0 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260817-16 | 50% | 2026-09-24 | military_conflict | Ukrainian long-range strikes halt loadings at a named Russian crude export terminal - Novorossiysk, Tuapse, Primorsk, or Ust-Luga - with the strike occurring between 2026-08-24 and 2026-09-21. | Reuters or Bloomberg reports suspended loadings at one of those four terminals attributed to a strike inside the window, and a Russian federal or regional official confirms the attack, by 2026-09-24. |
| KKR-20260817-17 | 25% | 2026-11-02 | economic | ICE Brent front-month futures settle at or above USD 100.00 per barrel on at least one trading session between 2026-08-24 and 2026-10-30. | The ICE Futures Europe published daily settlement for the front-month Brent contract reaches 100.00 or higher on any session in that range, checked 2026-11-02. |
| KKR-20260817-18 | 25% | 2026-08-24 | economic | Walmart reports Walmart US comparable sales excluding fuel of 4.5 percent or higher for fiscal Q2 2027 in its scheduled 2026-08-20 earnings release. | The Q2 FY27 earnings release furnished on Form 8-K to SEC EDGAR states Walmart US comparable sales excluding fuel at or above 4.5 percent, checked 2026-08-24. |
| KKR-20260817-19 | 29% | 2027-01-20 | political | FDA publishes a Federal Register document on the FSMA Section 204 food traceability rule - proposed rule, final rule, or request for information - between 2026-08-24 and 2027-01-15. | federalregister.gov lists an FDA document naming food traceability in its title or abstract with a publication date inside that range, checked 2027-01-20. |
| KKR-20260817-20 | 31% | 2026-10-08 | crime_security | A second person is charged over the 2026-08-15 Virginia State University shooting, with the charges filed between 2026-08-17 and 2026-10-05. | Chesterfield County Police, the Commonwealth Attorney, or Virginia online court records show charges against a second defendant filed inside that range, checked 2026-10-08. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

Nothing rejected — every projection cleared the gate.

## III. LEDGER STANDING

654 issued all-time across 14 forecaster arms · 564 open (5 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 126 issued · 118 open · 8 resolved · 1 hits / 7 misses · **Brier 0.125** against its own base rate 12.5% (climatological 0.109) · **skill -0.143** · under 30 resolved, this is noise.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 126 | 118 | 8 | 1 | 7 | 0.125 | 12.5% | 0.109 | -0.143 |
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
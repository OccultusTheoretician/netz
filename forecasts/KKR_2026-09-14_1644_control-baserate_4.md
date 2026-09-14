**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 141644Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-14_1516.md · forecaster: control/baserate · 9 accepted / 1 rejected by validation gate · 5 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260914-62 | 56% | 2026-10-20 | military_conflict | Commercial traffic through the Strait of Hormuz is halted for more than 24 consecutive hours at some point between 2026-09-15 and 2026-10-15. | TRUE if Reuters or Lloyds List Intelligence and Iranian state media both report a halt of commercial Hormuz transits exceeding 24 consecutive hours occurring between 2026-09-15 and 2026-10-15. |
| KKR-20260914-63 | 56% | 2026-10-09 | military_conflict | A Ukrainian strike damages a named Russian oil refinery between 2026-09-15 and 2026-10-06, notwithstanding US pressure to stop refinery strikes. | TRUE if a Russian federal or regional official confirms a strike on a named refinery dated between 2026-09-15 and 2026-10-06, and Reuters or AFP reports the same strike. |
| KKR-20260914-64 | 26% | 2026-11-03 | economics | ICE front-month Brent settles at or above 120.00 USD per barrel on at least one trading day between 2026-09-15 and 2026-10-30. Reference: 108.29 on the packet date. | TRUE if the official ICE Brent front-month settlement price is 120.00 USD or higher on any trading day from 2026-09-15 through 2026-10-30. Reference level 108.29 at seal. |
| KKR-20260914-65 | 26% | 2027-01-05 | economics | The FRED series DGS10 records a value of 5.50 percent or higher on at least one business day between 2026-09-15 and 2026-12-31. Reference: 4.99 percent on the packet date. | TRUE if any FRED DGS10 observation dated 2026-09-15 through 2026-12-31 is 5.50 or greater. Reference level 4.99 percent at seal. |
| KKR-20260914-66 | 26% | 2027-01-06 | economics | Anthropic publicly files a Form S-1 registration statement with the SEC, visible on EDGAR, with a filing date between 2026-09-15 and 2026-12-31. | TRUE if EDGAR full-text search returns a Form S-1 or S-1/A filed by Anthropic with a filing date between 2026-09-15 and 2026-12-31. Confidential submissions not yet public do not count. |
| KKR-20260914-67 | 28% | 2026-10-20 | cyber | Microsoft resolves the September 2026 Windows Server RDS connection failure with a shipped update between 2026-09-15 and 2026-10-16. | TRUE if the Windows release health entry for the September 2026 RDS failure shows status Resolved by an out-of-band update, Known Issue Rollback, or cumulative update dated between 2026-09-15 and 2026-10-16. |
| KKR-20260914-68 | 35% | 2026-09-22 | political | A US Senate roll call on the CLARITY Act or a motion directly on it is held between 2026-09-15 and 2026-09-18 and records fewer than 60 yea votes. | TRUE if Senate.gov roll call records show a vote on the CLARITY Act or a related cloture or passage motion between 2026-09-15 and 2026-09-18 with fewer than 60 yeas. |
| KKR-20260914-69 | 35% | 2026-12-15 | political | The Riksdag elects Magdalena Andersson Prime Minister in a vote held between 2026-09-21 and 2026-12-11. | TRUE if the Riksdag voting record at riksdagen.se shows a prime minister vote held between 2026-09-21 and 2026-12-11 in which Magdalena Andersson is elected. |
| KKR-20260914-70 | 31% | 2026-09-29 | disaster | GDACS raises the alert level for tropical cyclone FIFTEEN-E-26 to orange or red at some point between 2026-09-15 and 2026-09-25. | TRUE if the GDACS event page for tropical cyclone FIFTEEN-E-26 shows an orange or red alert level assigned between 2026-09-15 and 2026-09-25. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The CISA KEV catalog carries at least one entry with vendorProject GitLab and a dateAdded value between 2026-09-08 and 2026-10-16." → REJECTED: event window opens 2026-09-08, before this row is sealed (2026-09-14, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later

## III. LEDGER STANDING

2139 issued all-time across 16 forecaster arms · 1803 open (79 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 706 issued · 668 open · 38 resolved · 18 hits / 20 misses · **Brier 0.280** against its own base rate 47.4% (climatological 0.249) · **skill -0.124**.

*21 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 706 | 668 | 38 | 18 | 20 | 0.280 | 47.4% | 0.249 | -0.124 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 265 | 136 | 120 | 26 | 94 | 0.195 | 21.7% | 0.170 | -0.151 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 60 | 60 | 0 | — | — | not computed | — | — | — |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 31 | 7 | 5 | 2 | 0.063 | 71.4% | 0.204 | +0.692 |
| manual/fable-5.1/unattested | 96 | 96 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 231 | 228 | 3 | 3 | 0 | 0.153 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 244 | 238 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 13 | 31 | 17 | 14 | 0.239 | 54.8% | 0.248 | +0.036 |
| manual/sonnet-5/unattested | 234 | 202 | 32 | 16 | 16 | 0.224 | 50.0% | 0.250 | +0.105 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*
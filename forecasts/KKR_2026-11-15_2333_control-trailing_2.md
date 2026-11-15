**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 152333Z NOV 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-11-15_1612.md · forecaster: control/trailing · 6 accepted / 0 rejected by validation gate · 0 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261115-35 | 68% | 2026-12-09 | military/conflict | Between 2026-11-16 and 2026-12-06 UTC, US forces carry out at least one kinetic strike on a target on Iranian territory, including Iranian islands. | True if CENTCOM, or US officials quoted by at least two of Reuters, AP, CNN, NBC News and ABC News, confirm a US strike on Iranian territory carried out between 2026-11-16 and 2026-12-06. |
| KKR-20261115-36 | 70% | 2026-12-08 | economics/markets | ICE Brent crude front-month futures settle at or above 100.00 USD per barrel on at least one trading day between 2026-11-16 and 2026-12-04. Reference: 95.84 on the packet date. | True if any daily ICE Brent front-month settlement price from 2026-11-16 through 2026-12-04 is 100.00 USD or higher. Reference: 95.84 on the packet date. |
| KKR-20261115-37 | 36% | 2026-11-23 | political | Donald Trump, Xi Jinping and Vladimir Putin hold an in-person three-way meeting in Shenzhen, China, between 2026-11-18 and 2026-11-20. | True if a White House, Kremlin or Chinese Foreign Ministry readout, or both Reuters and AP, record all three leaders meeting together in person in Shenzhen between 2026-11-18 and 2026-11-20 local time. |
| KKR-20261115-38 | 36% | 2026-11-23 | political | The International Court of Justice judgment in The Gambia v. Myanmar, scheduled for delivery on 2026-11-19, finds that Myanmar breached the Genocide Convention by committing genocide against the Rohingya. | True if the operative clause of the judgment delivered on 2026-11-19 and published on icj-cij.org declares that Myanmar violated the Genocide Convention by committing genocide. Any lesser finding, or none, is false. |
| KKR-20261115-39 | 36% | 2026-12-30 | political | The Knesset approves, in a confidence vote held between 2026-11-16 and 2026-12-28, a new Israeli government with Gadi Eisenkot as prime minister. | True if the Knesset record shows a confidence vote passed between 2026-11-16 and 2026-12-28 installing a government headed by Gadi Eisenkot as prime minister. |
| KKR-20261115-40 | 57% | 2027-01-05 | crime/security | Between 2026-11-16 and 2026-12-31, at least one named person is criminally charged, in state or federal court, over the explosive device found on 2026-11-13 at an ethanol plant in Peoria, Illinois. | True if a US Department of Justice or Peoria County prosecutor announcement, or a court docket, shows a charge filed between 2026-11-16 and 2026-12-31 against a named person over the Peoria device. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

Nothing rejected — every projection cleared the gate.

## III. LEDGER STANDING

5807 issued all-time across 23 forecaster arms · 4085 open (1723 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/trailing`:** 227 issued · 227 open · nothing resolved yet — this arm earns a score at its first resolution.

*96 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1788 | 1279 | 477 | 273 | 204 | 0.300 | 57.2% | 0.245 | -0.226 |
| control/trailing | 227 | 227 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 9 | 11 | 1 | 10 | 0.123 | 9.1% | 0.083 | -0.490 |
| lmstudio/auto[post-window] | 470 | 201 | 259 | 75 | 184 | 0.204 | 29.0% | 0.206 | +0.009 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 221 | 204 | 11 | 4 | 7 | 0.227 | 36.4% | 0.231 | +0.020 |
| lmstudio/qwen36-abliterated | 224 | 222 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
| lmstudio/qwen36-realist | 209 | 176 | 31 | 10 | 21 | 0.242 | 32.3% | 0.219 | -0.106 |
| lmstudio/realist | 249 | 128 | 119 | 66 | 53 | 0.317 | 55.5% | 0.247 | -0.285 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 14 | 24 | 14 | 10 | 0.164 | 58.3% | 0.243 | +0.325 |
| manual/fable-5.1/unattested | 535 | 420 | 107 | 61 | 46 | 0.211 | 57.0% | 0.245 | +0.140 |
| manual/fable-5.2/unattested | 29 | 29 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 258 | 147 | 102 | 65 | 37 | 0.203 | 63.7% | 0.231 | +0.121 |
| manual/opus-5 | 74 | 39 | 35 | 18 | 17 | 0.213 | 51.4% | 0.250 | +0.146 |
| manual/opus-5.5/unattested | 404 | 390 | 14 | 8 | 6 | 0.312 | 57.1% | 0.245 | -0.275 |
| manual/opus-5/unattested | 326 | 221 | 95 | 61 | 34 | 0.208 | 64.2% | 0.230 | +0.097 |
| manual/sonnet-5 | 45 | 3 | 41 | 22 | 19 | 0.250 | 53.7% | 0.249 | -0.007 |
| manual/sonnet-5.5/unattested | 222 | 207 | 15 | 10 | 5 | 0.122 | 66.7% | 0.222 | +0.451 |
| manual/sonnet-5/unattested | 342 | 141 | 196 | 98 | 98 | 0.245 | 50.0% | 0.250 | +0.019 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*
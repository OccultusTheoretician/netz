**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 271518Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-27_1516.md · forecaster: lmstudio/qwen36-realist · 4 accepted / 4 rejected by validation gate · 1 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261027-10 | 90% | 2026-11-05 | political | The Netherlands withdraws from the Eurovision 2027 contest. | The European Broadcasting Union confirms the Netherlands has withdrawn from the Eurovision 2027 contest. |
| KKR-20261027-11 | 30% | 2026-11-05 | disaster | A forest fire notification is issued by GDACS for a location in Papua New Guinea between 2026-10-27 and 2026-11-03. | The GDACS Alerts database carries a forest fire notification for a location in Papua New Guinea with a date between 2026-10-27 and 2026-11-03. |
| KKR-20261027-12 | 85% | 2026-11-05 | political | The CDC deputy director appointed by Trump resigns from office. | The CDC confirms the resignation of the Trump-appointed deputy director. |
| KKR-20261027-13 | 90% | 2026-11-05 | crime | A man is arrested for sending suspicious powder to the US Congress. | The FBI or US Capitol Police confirms an arrest for sending suspicious powder to the US Congress. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The CISA KEV catalog carries a date-added value for CVE-2026-109618 between 2026-10-27 and 2026-11-03." → REJECTED: the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-109618 dateAdded 2026-10-26, before the claimed window 2026-10-27..2026-11-03; dateAdded is single-valued and a fresh in-window value would require removal-and-relisting, which has no documented precedent (removals exist: CVE-2022-28958, removed 2023-12-01)
- "The S&P 500 index closes above 7,750 on any trading day between 2026-11-02 and 2026-11-06." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "Ebola cases in DR Congo surpass 10,000." → REJECTED: statement too thin to adjudicate (39 chars) — a third party reading the statement alone must be able to say what was claimed
- "JetBlue stock closes above $15 on any trading day between 2026-11-02 and 2026-11-06." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date

## III. LEDGER STANDING

5037 issued all-time across 21 forecaster arms · 3315 open (400 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36-realist`:** 126 issued · 93 open · 31 resolved · 10 hits / 21 misses · **Brier 0.242** against its own base rate 32.3% (climatological 0.219) · **skill -0.106**.

*96 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1770 | 1261 | 477 | 273 | 204 | 0.300 | 57.2% | 0.245 | -0.226 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 9 | 11 | 1 | 10 | 0.123 | 9.1% | 0.083 | -0.490 |
| lmstudio/auto[post-window] | 470 | 201 | 259 | 75 | 184 | 0.204 | 29.0% | 0.206 | +0.009 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 125 | 108 | 11 | 4 | 7 | 0.227 | 36.4% | 0.231 | +0.020 |
| lmstudio/qwen36-abliterated | 123 | 121 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
| lmstudio/qwen36-realist | 126 | 93 | 31 | 10 | 21 | 0.242 | 32.3% | 0.219 | -0.106 |
| lmstudio/realist | 249 | 128 | 119 | 66 | 53 | 0.317 | 55.5% | 0.247 | -0.285 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 14 | 24 | 14 | 10 | 0.164 | 58.3% | 0.243 | +0.325 |
| manual/fable-5.1/unattested | 447 | 332 | 107 | 61 | 46 | 0.211 | 57.0% | 0.245 | +0.140 |
| manual/fable-5/unattested | 258 | 147 | 102 | 65 | 37 | 0.203 | 63.7% | 0.231 | +0.121 |
| manual/opus-5 | 74 | 39 | 35 | 18 | 17 | 0.213 | 51.4% | 0.250 | +0.146 |
| manual/opus-5.5/unattested | 276 | 262 | 14 | 8 | 6 | 0.312 | 57.1% | 0.245 | -0.275 |
| manual/opus-5/unattested | 326 | 221 | 95 | 61 | 34 | 0.208 | 64.2% | 0.230 | +0.097 |
| manual/sonnet-5 | 45 | 3 | 41 | 22 | 19 | 0.250 | 53.7% | 0.249 | -0.007 |
| manual/sonnet-5.5/unattested | 222 | 207 | 15 | 10 | 5 | 0.122 | 66.7% | 0.222 | +0.451 |
| manual/sonnet-5/unattested | 342 | 141 | 196 | 98 | 98 | 0.245 | 50.0% | 0.250 | +0.019 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*
**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 220330Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-21_1524.md · forecaster: manual/fable-5/unattested · 2 accepted / 0 rejected by validation gate · 1 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260822-09 | 45% | 2026-09-22 | cyber | CISA adds CVE-2026-19478, the GitLab CE/EE GraphQL code-injection flaw (CVSS 9.4) reported exploited in the wild on 2026-08-19, to the Known Exploited Vulnerabilities catalog with a dateAdded value between 2026-08-21 and 2026-09-18. | The CISA KEV catalog JSON feed contains an entry with cveID CVE-2026-19478 whose dateAdded field is a date from 2026-08-21 through 2026-09-18 inclusive. |
| KKR-20260822-10 | 25% | 2026-09-22 | cyber | CISA adds CVE-2026-69836, the Microsoft Entra ID deserialization remote code execution flaw (CVSS 10.0) that Microsoft says was exploited and is already mitigated server-side, to the KEV catalog with a dateAdded value between 2026-08-21 and 2026-09-18. | The CISA KEV catalog JSON feed contains an entry with cveID CVE-2026-69836 whose dateAdded field is a date from 2026-08-21 through 2026-09-18 inclusive. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

Nothing rejected — every projection cleared the gate.

## III. LEDGER STANDING

841 issued all-time across 14 forecaster arms · 751 open (32 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/fable-5/unattested`:** 72 issued · 72 open · nothing resolved yet — this arm earns a score at its first resolution.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 186 | 178 | 8 | 1 | 7 | 0.125 | 12.5% | 0.109 | -0.143 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 20 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-window] | 117 | 105 | 10 | 2 | 8 | 0.240 | 20.0% | 0.160 | -0.502 |
| lmstudio/auto[pre-verbot] | 60 | 13 | 39 | 12 | 27 | 0.225 | 30.8% | 0.213 | -0.054 |
| manual/fable | 45 | 36 | 9 | 4 | 5 | 0.190 | 44.4% | 0.247 | +0.232 |
| manual/fable-5 | 38 | 38 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 72 | 72 | 0 | — | — | not computed | — | — | — |
| manual/opus-5 | 74 | 72 | 2 | 1 | 1 | 0.243 | 50.0% | 0.250 | +0.030 |
| manual/opus-5/unattested | 88 | 88 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 45 | 39 | 6 | 3 | 3 | 0.270 | 50.0% | 0.250 | -0.081 |
| manual/sonnet-5/unattested | 79 | 78 | 1 | 0 | 1 | 0.040 | 0.0% | 0.000 | — |
| operator/human | 6 | 2 | 1 | 1 | 0 | 0.122 | 100.0% | 0.000 | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*
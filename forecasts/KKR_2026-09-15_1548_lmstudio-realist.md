**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 151548Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-15_1544.md · forecaster: lmstudio/realist · 9 accepted / 1 rejected by validation gate · 5 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260915-09 | 30% | 2026-10-01 | cyber | Between 2026-09-15 and 2026-09-22, at least one major cyberattack exploiting CVE-2026-76461 will be confirmed by two independent sources. | At least one confirmed cyberattack exploiting CVE-2026-76461 is reported by two or more independent sources (e.g., BleepingComputer, The Hacker News, CISA Advisories) with distinct reporting channels. |
| KKR-20260915-10 | 85% | 2026-09-24 | economics/markets | Between 2026-09-15 and 2026-09-22, the 10-year U.S. Treasury yield will exceed 5.00 percent at any point during the window. | The 10-year U.S. Treasury yield, as reported by FRED or the U.S. Department of the Treasury, reaches or exceeds 5.00 percent at any point between 2026-09-15 and 2026-09-22. |
| KKR-20260915-11 | 25% | 2026-09-24 | military/conflict | Between 2026-09-15 and 2026-09-22, a drone strike will be reported in Kyiv with at least one casualty confirmed by two independent sources. | A drone strike in Kyiv is confirmed by two or more independent sources (e.g., Al Jazeera, BBC World, Deutsche Welle) with at least one casualty reported in corroborating reports. |
| KKR-20260915-12 | 35% | 2026-09-24 | disaster | Between 2026-09-15 and 2026-09-22, a major oil pipeline disruption in the Panama Canal region will be confirmed by two independent sources due to drought. | A major disruption to oil pipeline traffic in the Panama Canal region is confirmed by two independent sources (e.g., Guardian World, BBC World) due to drought conditions linked to El Niño. |
| KKR-20260915-13 | 40% | 2026-09-24 | military/conflict | Between 2026-09-15 and 2026-09-22, a U.S. military statement will confirm the deployment of weapons in space, verified by two independent sources. | A U.S. military statement confirming the deployment of weapons in space is reported by two or more independent sources (e.g., BBC World, Al Jazeera, Guardian World) with no contradictory denial. |
| KKR-20260915-14 | 20% | 2026-09-24 | cyber | Between 2026-09-15 and 2026-09-22, a cyberattack targeting a U.S. federal agency will be attributed to a China-linked group by CISA. | CISA issues a public advisory attributing a cyberattack on a U.S. federal agency to a China-linked threat actor during the event window. |
| KKR-20260915-15 | 30% | 2026-09-24 | military/conflict | Between 2026-09-15 and 2026-09-22, the Strait of Hormuz will see a confirmed tanker attack with at least one casualty, verified by two independent sources. | A confirmed tanker attack in the Strait of Hormuz with at least one casualty is reported by two or more independent sources (e.g., BBC World, Al Jazeera). |
| KKR-20260915-16 | 45% | 2026-09-24 | political | Between 2026-09-15 and 2026-09-22, a political statement by Zelenskyy will be confirmed by two independent sources stating Ukraine will pause attacks if Russia spares infrastructure. | A statement by Zelenskyy confirming Ukraine will pause attacks if Russia spares infrastructure is reported by two or more independent sources (e.g., Al Jazeera, BBC World). |
| KKR-20260915-17 | 25% | 2026-09-24 | disaster | Between 2026-09-15 and 2026-09-22, a major forest fire in Australia will be reported by GDACS Alerts with a green alert level. | GDACS Alerts issues a green forest fire notification for Australia during the event window. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-09-15 and 2026-09-22, the CISA KEV catalog will include CVE-2026-76461 with a date-added value of 2026-09-14." → REJECTED: the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-76461 dateAdded 2026-09-14, before the claimed window 2026-09-15..2026-09-22; dateAdded is single-valued and a fresh in-window value would require removal-and-relisting, which has no documented precedent (removals exist: CVE-2022-28958, removed 2023-12-01)

## III. LEDGER STANDING

2156 issued all-time across 16 forecaster arms · 1820 open (101 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/realist`:** 69 issued · 69 open · nothing resolved yet — this arm earns a score at its first resolution.

*21 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 706 | 668 | 38 | 18 | 20 | 0.280 | 47.4% | 0.249 | -0.124 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 273 | 144 | 120 | 26 | 94 | 0.195 | 21.7% | 0.170 | -0.151 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 69 | 69 | 0 | — | — | not computed | — | — | — |
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
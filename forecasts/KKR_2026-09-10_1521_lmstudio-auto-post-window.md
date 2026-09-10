**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 101521Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-10_1519.md · forecaster: lmstudio/auto · 9 accepted / 1 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260910-01 | 85% | 2026-10-01 | economics/markets | Between 2026-09-21 and 2026-09-24, the European Central Bank will raise interest rates to 2.5%. | The European Central Bank announces a rate hike to 2.5% during the event window. |
| KKR-20260910-02 | 25% | 2026-10-03 | military/conflict | Between 2026-09-21 and 2026-09-24, a drone strike will be reported in Jabalia, Gaza, with at least one casualty claimed by a hostile side. | At least one report from a hostile side confirms a drone strike in Jabalia, Gaza, with a claimed casualty count of one or more during the event window. |
| KKR-20260910-03 | 35% | 2026-10-05 | cyber | Between 2026-09-21 and 2026-09-24, a ransomware attack exploiting CVE-2026-20079 will be confirmed by CISA. | CISA issues a public advisory confirming a ransomware attack exploiting CVE-2026-20079 between 2026-09-21 and 2026-09-24. |
| KKR-20260910-04 | 65% | 2026-10-06 | economics/markets | Between 2026-09-21 and 2026-09-24, the 10-year U.S. Treasury yield will exceed 4.92% at market close. | The 10-year U.S. Treasury yield exceeds 4.92% on the close of any trading day between 2026-09-21 and 2026-09-24. |
| KKR-20260910-05 | 40% | 2026-10-07 | military/conflict | Between 2026-09-21 and 2026-09-24, the Houthis will seize control of the port city of Mocha in Yemen. | At least two independent, hostile-side reports confirm the Houthis have seized control of Mocha port between 2026-09-21 and 2026-09-24. |
| KKR-20260910-06 | 20% | 2026-10-08 | disaster | Between 2026-09-21 and 2026-09-24, a tropical cyclone named NORBERT-26 will cause a green alert in GDACS with population affected exceeding 100,000. | GDACS issues a green alert for tropical cyclone NORBERT-26 between 2026-09-21 and 2026-09-24 with a population affected estimate exceeding 100,000. |
| KKR-20260910-07 | 55% | 2026-10-09 | political | Between 2026-09-21 and 2026-09-24, Trump will publicly promise a $5,000 dividend to all U.S. adults if the GOP wins the 2026 midterm elections. | A public statement by Donald Trump between 2026-09-21 and 2026-09-24 confirms a $5,000 dividend for all U.S. adults contingent on a GOP midterm victory. |
| KKR-20260910-08 | 15% | 2026-10-10 | cyber | Between 2026-09-21 and 2026-09-24, a cyberattack on a U.S. federal agency will be confirmed by CISA involving the exploitation of a zero-day vulnerability in Google Chromium V8. | CISA issues a public advisory confirming a cyberattack on a U.S. federal agency between 2026-09-21 and 2026-09-24 involving the exploitation of a zero-day vulnerability in Google Chromium V8. |
| KKR-20260910-09 | 30% | 2026-10-11 | disaster | Between 2026-09-21 and 2026-09-24, a cargo ship fire in China will result in at least 25 fatalities as confirmed by Al Jazeera, BBC World, and Deutsche Welle. | Al Jazeera, BBC World, and Deutsche Welle each publish a report confirming at least 25 fatalities from a cargo ship fire in China between 2026-09-21 and 2026-09-24. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-09-21 and 2026-09-24, the CISA KEV catalog will include CVE-2026-20079 with a date-added value of 2026-09-09." → REJECTED: the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-20079 dateAdded 2026-09-09, before the claimed window 2026-09-21..2026-09-24; dateAdded is single-valued and a fresh in-window value would require removal-and-relisting, which has no documented precedent (removals exist: CVE-2022-28958, removed 2023-12-01)

## III. LEDGER STANDING

1817 issued all-time across 16 forecaster arms · 1481 open (54 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/auto[post-window]`:** 249 issued · 120 open · 120 resolved · 26 hits / 94 misses · **Brier 0.195** against its own base rate 21.7% (climatological 0.170) · **skill -0.151**.

*21 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 567 | 529 | 38 | 18 | 20 | 0.280 | 47.4% | 0.249 | -0.124 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 249 | 120 | 120 | 26 | 94 | 0.195 | 21.7% | 0.170 | -0.151 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 32 | 32 | 0 | — | — | not computed | — | — | — |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 31 | 7 | 5 | 2 | 0.063 | 71.4% | 0.204 | +0.692 |
| manual/fable-5.1/unattested | 58 | 58 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 196 | 193 | 3 | 3 | 0 | 0.153 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 213 | 207 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 13 | 31 | 17 | 14 | 0.239 | 54.8% | 0.248 | +0.036 |
| manual/sonnet-5/unattested | 199 | 167 | 32 | 16 | 16 | 0.224 | 50.0% | 0.250 | +0.105 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*
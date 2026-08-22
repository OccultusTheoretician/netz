**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 221518Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-22_1516.md · forecaster: lmstudio/auto · 5 accepted / 5 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260822-21 | 25% | 2026-09-02 | economics/markets | U.S. and Canadian officials announce a new bilateral tariff agreement between 2026-08-22 and 2026-08-28 | A joint statement from U.S. and Canadian officials, published in at least two independent outlets (e.g., BBC, CNBC), confirms a new bilateral tariff agreement between 2026-08-22 and 2026-08-28. |
| KKR-20260822-22 | 20% | 2026-09-02 | disaster | A major earthquake of magnitude 6.5 or higher occurs in the Scotia Sea between 2026-08-22 and 2026-08-28 | The USGS Significant Quakes catalog records a magnitude 6.5 or higher earthquake in the Scotia Sea between 2026-08-22 and 2026-08-28, with a depth of 10 km or less. |
| KKR-20260822-23 | 35% | 2026-09-02 | political | Iran announces the resumption of uranium enrichment at 60% purity between 2026-08-22 and 2026-08-28 | Iran's foreign ministry or state media announces, via a public statement, the resumption of uranium enrichment at 60% purity between 2026-08-22 and 2026-08-28, confirmed by at least two independent outlets (AXIS, WEST). |
| KKR-20260822-24 | 18% | 2026-09-02 | cyber | A cyberattack using a proxy botnet malware infects at least 10,000 vehicles with Android-based head units between 2026-08-22 and 2026-08-28 | At least 10,000 vehicles with Android-based head units are confirmed infected by proxy botnet malware, as reported by BleepingComputer or The Hacker News between 2026-08-22 and 2026-08-28. |
| KKR-20260822-25 | 32% | 2026-09-02 | political | A new political scandal involving a U.S. federal official is confirmed by two independent outlets between 2026-08-22 and 2026-08-28 | Two independent outlets (e.g., BBC, Guardian, Politico) publish a confirmed report of a political scandal involving a U.S. federal official between 2026-08-22 and 2026-08-28, with corroboration from a third source. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "A Russian drone strike kills at least 5 people in Kyiv between 2026-08-22 and 2026-08-28" → REJECTED: the packet already decides this claim; a forecast must be open at seal -- the row's own citation [70], dated 2026-08-22 inside the claimed window 2026-08-22..2026-08-28, already reports 6 killed against the row's threshold of 5
- "The CISA KEV catalog includes CVE-2026-73570 in a public exploit update between 2026-08-22 and 2026-08-28" → REJECTED: the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-73570 dateAdded 2026-08-21, before the claimed window 2026-08-22..2026-08-28; dateAdded is single-valued and a fresh in-window value would require removal-and-relisting, which has no documented precedent (removals exist: CVE-2022-28958, removed 2023-12-01)
- "A cyberattack exploiting CVE-2026-73570 results in a public data breach of a U.S. federal agency between 2026-08-22 and 2026-08-28" → REJECTED: the named venue is introduced by 'e.g.', which makes it an example rather than the source of record — the adjudicator still chooses. Strike the softener or name the class exhaustively
- "A new U.S. sanctions package targeting Iranian financial institutions is enacted between 2026-08-22 and 2026-08-28" → REJECTED: resolution offers alternative VENUES joined by 'or' (…federal register | or | a…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "A wildfire in the Kootenai National Forest in Montana spreads to exceed 10,000 acres between 2026-08-22 and 2026-08-28" → REJECTED: resolution offers alternative VENUES joined by 'or' (…the gdacs alerts system | or | the national interagency fire center (nifc) r…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

856 issued all-time across 14 forecaster arms · 766 open (32 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/auto[post-window]`:** 122 issued · 110 open · 10 resolved · 2 hits / 8 misses · **Brier 0.240** against its own base rate 20.0% (climatological 0.160) · **skill -0.502** · under 30 resolved, this is noise.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 186 | 178 | 8 | 1 | 7 | 0.125 | 12.5% | 0.109 | -0.143 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 20 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-window] | 122 | 110 | 10 | 2 | 8 | 0.240 | 20.0% | 0.160 | -0.502 |
| lmstudio/auto[pre-verbot] | 60 | 13 | 39 | 12 | 27 | 0.225 | 30.8% | 0.213 | -0.054 |
| manual/fable | 45 | 36 | 9 | 4 | 5 | 0.190 | 44.4% | 0.247 | +0.232 |
| manual/fable-5 | 38 | 38 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 72 | 72 | 0 | — | — | not computed | — | — | — |
| manual/opus-5 | 74 | 72 | 2 | 1 | 1 | 0.243 | 50.0% | 0.250 | +0.030 |
| manual/opus-5/unattested | 92 | 92 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 45 | 39 | 6 | 3 | 3 | 0.270 | 50.0% | 0.250 | -0.081 |
| manual/sonnet-5/unattested | 85 | 84 | 1 | 0 | 1 | 0.040 | 0.0% | 0.000 | — |
| operator/human | 6 | 2 | 1 | 1 | 0 | 0.122 | 100.0% | 0.000 | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*
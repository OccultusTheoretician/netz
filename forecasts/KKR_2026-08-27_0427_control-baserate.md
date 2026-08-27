**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 270427Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-26_1538.md · forecaster: control/baserate · 6 accepted / 0 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260827-23 | 23% | 2026-10-02 | cyber | CISA adds CVE-2026-63520, the Microsoft SharePoint Business Connectivity Services remote code execution flaw that completes the chain with CVE-2026-55040, to the Known Exploited Vulnerabilities catalog between 2026-08-27 and 2026-09-30. | The CISA KEV JSON feed contains an entry for CVE-2026-63520 whose dateAdded value falls between 2026-08-27 and 2026-09-30 inclusive; otherwise false. |
| KKR-20260827-24 | 23% | 2026-11-03 | cyber | Boston Scientific files a Form 8-K or 8-K/A with the SEC that includes Item 1.05, Material Cybersecurity Incidents, for the August 2026 cyberattack between 2026-08-27 and 2026-10-30, following its initial Item 8.01 disclosure. | EDGAR filings for CIK 885725 show a Form 8-K or 8-K/A with filing date 2026-08-27 through 2026-10-30 whose listed items include 1.05; otherwise false. |
| KKR-20260827-25 | 29% | 2026-09-08 | political | Xi Jinping holds an in-person meeting with Egyptian President Abdel Fattah El-Sisi on Egyptian territory between 2026-08-30 and 2026-09-04, as part of the state visit announced by the Chinese Foreign Ministry. | Both Xinhua or the Chinese Foreign Ministry and the Egyptian Presidency report an in-person Xi-Sisi meeting held on Egyptian territory between 2026-08-30 and 2026-09-04; otherwise false. |
| KKR-20260827-26 | 50% | 2026-10-02 | military/conflict | United States and Iranian officials at the level of secretary of state, foreign minister, or presidential special envoy meet face to face for a negotiating session between 2026-08-27 and 2026-09-30, and both governments acknowledge the meeting. | Both the US State Department or White House and the Iranian Foreign Ministry publicly confirm a face to face US-Iran session at that level held between 2026-08-27 and 2026-09-30; mediated exchanges through third parties do not count. |
| KKR-20260827-27 | 50% | 2026-09-29 | military/conflict | UKMTO publishes at least one incident advisory reporting a merchant vessel struck or damaged by a projectile, mine, or uncrewed system within 100 nautical miles of the Strait of Hormuz, anchor 26.5N 56.3E, between 2026-08-27 and 2026-09-25. | A UKMTO advisory at ukmto.org dated 2026-08-27 through 2026-09-25 reports a vessel struck or damaged by a projectile, mine, or uncrewed system at a position within 100 nm of 26.5N 56.3E; otherwise false. |
| KKR-20260827-28 | 33% | 2026-09-18 | disaster | The confirmed death toll in Nepal from the 26 August 2026 Bhotekoshi-Trishuli avalanche flash flood reaches at least 250 by 2026-09-16, as published by Nepal Police, the Office of the Prime Minister of Nepal, or the NDRRMA. | By 2026-09-16 a figure of at least 250 confirmed dead in Nepal, excluding missing persons and excluding deaths in China, is published by Nepal Police, the Office of the Prime Minister, or the NDRRMA BIPAD portal. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

Nothing rejected — every projection cleared the gate.

## III. LEDGER STANDING

951 issued all-time across 14 forecaster arms · 861 open (75 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 192 issued · 184 open · 8 resolved · 1 hits / 7 misses · **Brier 0.125** against its own base rate 12.5% (climatological 0.109) · **skill -0.143** · under 30 resolved, this is noise.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 192 | 184 | 8 | 1 | 7 | 0.125 | 12.5% | 0.109 | -0.143 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 20 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-window] | 152 | 140 | 10 | 2 | 8 | 0.240 | 20.0% | 0.160 | -0.502 |
| lmstudio/auto[pre-verbot] | 60 | 13 | 39 | 12 | 27 | 0.225 | 30.8% | 0.213 | -0.054 |
| manual/fable | 45 | 36 | 9 | 4 | 5 | 0.190 | 44.4% | 0.247 | +0.232 |
| manual/fable-5 | 38 | 38 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 92 | 92 | 0 | — | — | not computed | — | — | — |
| manual/opus-5 | 74 | 72 | 2 | 1 | 1 | 0.243 | 50.0% | 0.250 | +0.030 |
| manual/opus-5/unattested | 114 | 114 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 45 | 39 | 6 | 3 | 3 | 0.270 | 50.0% | 0.250 | -0.081 |
| manual/sonnet-5/unattested | 102 | 101 | 1 | 0 | 1 | 0.040 | 0.0% | 0.000 | — |
| operator/human | 6 | 2 | 1 | 1 | 0 | 0.122 | 100.0% | 0.000 | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*
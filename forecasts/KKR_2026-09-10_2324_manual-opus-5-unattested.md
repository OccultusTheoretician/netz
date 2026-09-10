**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 102324Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-10_1519.md · forecaster: manual/opus-5/unattested · 6 accepted / 4 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260910-61 | 75% | 2026-10-22 | cyber | CISA adds at least one Microsoft vulnerability to the Known Exploited Vulnerabilities catalog between 2026-10-13, October Patch Tuesday, and 2026-10-20. | TRUE if the CISA KEV JSON feed lists at least one entry with vendorProject Microsoft and a dateAdded value between 2026-10-13 and 2026-10-20 inclusive. FALSE otherwise. |
| KKR-20260910-62 | 25% | 2026-11-02 | cyber | CISA adds CVE-2026-85102 or CVE-2026-85103, the Check Point VPN certificate flaws disclosed 2026-09-09, to the Known Exploited Vulnerabilities catalog between 2026-09-11 and 2026-10-30. | TRUE if the CISA KEV JSON feed lists CVE-2026-85102 or CVE-2026-85103 with a dateAdded value between 2026-09-11 and 2026-10-30 inclusive. FALSE otherwise. |
| KKR-20260910-63 | 20% | 2026-11-03 | military/conflict | US or Israeli forces strike the Pickaxe Mountain (Kuh-e Kolang Gaz La) tunnel complex near Natanz, Iran, between 2026-09-11 and 2026-10-31. | TRUE if a strike on the site between 2026-09-11 and 2026-10-31 is confirmed by Pentagon, CENTCOM, White House or IDF, or by two of Reuters, AP, AFP citing US or Israeli officials. Iranian claims alone do not count. |
| KKR-20260910-64 | 20% | 2026-12-02 | military/conflict | A ceasefire, truce, or cessation of hostilities between the United States and Iran is announced by the US government and publicly accepted by the Iranian government between 2026-09-11 and 2026-11-30. | TRUE if between 2026-09-11 and 2026-11-30 the US government announces a US-Iran ceasefire or truce and the Iranian government publicly confirms it, as reported by at least two of Reuters, AP, AFP, BBC. |
| KKR-20260910-65 | 30% | 2026-11-02 | military/conflict | Houthi forces take control of the town of Dhubab, Taiz governorate, on the southern Red Sea coast approach to the Bab al-Mandab strait, between 2026-09-11 and 2026-10-30. | TRUE if Houthi forces take control of Dhubab town between 2026-09-11 and 2026-10-30, as reported by at least two of Reuters, AP, AFP citing Yemeni government or government-aligned military sources. Houthi claims alone do not count. |
| KKR-20260910-66 | 70% | 2026-09-22 | political | The Liberals win at least 4.00 percent of valid national votes in the Swedish Riksdag election held 2026-09-13, clearing the parliamentary threshold. | TRUE if the Valmyndigheten final result (slutligt valresultat) for the 2026-09-13 Riksdag election shows the Liberals at 4.00 percent or more of valid national votes. FALSE if below 4.00 percent. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The FOMC raises the federal funds target range above 3.50-3.75 percent at its meeting concluding 2026-09-16. Reference: 3.50-3.75 percent ta" → REJECTED: deadline leaves no settling margin — resolution requires third-party confirmation and the deadline (2026-09-18) is 1 day(s) after the window closes (2026-09-17). Cross-bias confirmation does not exist yet on the morning the resolver walks the row; allow >= 2 days
- "The ECB Governing Council raises the deposit facility rate above 2.50 percent at its monetary policy meeting concluding 2026-10-29. Referenc" → REJECTED: resolution offers alternative VENUES joined by 'or' (… percent, per the ecb key interest rates page | or | ecb data portal…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "UK authorities charge at least one of the two people, a 42-year-old woman and a 60-year-old man, arrested in London on 2026-09-09 on suspici" → REJECTED: the resolution names a different subject than the statement — the claim is about Iranian, London, UK and the resolution settles on Act, CPS, Metropolitan, National. A row whose resolution checks a different fact can be scored correct while being wrong
- "September 2026, between 2026-09-01 and 2026-09-30, is the warmest September in the Copernicus ERA5 global surface air temperature record, ex" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; event window opens 2026-09-01, before this row is sealed (2026-09-10, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later

## III. LEDGER STANDING

1874 issued all-time across 16 forecaster arms · 1538 open (54 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/opus-5/unattested`:** 219 issued · 213 open · 6 resolved · 4 hits / 2 misses · **Brier 0.157** against its own base rate 66.7% (climatological 0.222) · **skill +0.293** · under 30 resolved, this is noise.

*21 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 590 | 552 | 38 | 18 | 20 | 0.280 | 47.4% | 0.249 | -0.124 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 249 | 120 | 120 | 26 | 94 | 0.195 | 21.7% | 0.170 | -0.151 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 37 | 37 | 0 | — | — | not computed | — | — | — |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 31 | 7 | 5 | 2 | 0.063 | 71.4% | 0.204 | +0.692 |
| manual/fable-5.1/unattested | 68 | 68 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 203 | 200 | 3 | 3 | 0 | 0.153 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 219 | 213 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 13 | 31 | 17 | 14 | 0.239 | 54.8% | 0.248 | +0.036 |
| manual/sonnet-5/unattested | 205 | 173 | 32 | 16 | 16 | 0.224 | 50.0% | 0.250 | +0.105 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*
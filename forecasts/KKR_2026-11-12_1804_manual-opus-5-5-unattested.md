**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 121804Z NOV 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-11-12_1613.md · forecaster: manual/opus-5.5/unattested · 7 accepted / 3 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261112-34 | 8% | 2027-02-19 | military/conflict | A general ceasefire covering the entire Russia-Ukraine line of contact takes effect between 2026-11-13 and 2027-02-15, confirmed by both the Russian and Ukrainian governments. | TRUE if Reuters and AP both report a ceasefire covering the whole front line took effect between 2026-11-13 and 2027-02-15, confirmed by both governments; energy-only, humanitarian, holiday or localized truces do not count. |
| KKR-20261112-35 | 40% | 2027-02-01 | economics/markets | The 10-year Treasury constant-maturity yield, FRED series DGS10, closes at or above 5.25 percent on at least one trading day between 2026-11-13 and 2027-01-29. Reference: 5.07 percent on the packet date. | TRUE if the highest FRED DGS10 daily value dated 2026-11-13 through 2027-01-29 is 5.25 or higher; FALSE otherwise. Reference: 5.07 percent on the packet date. |
| KKR-20261112-36 | 45% | 2027-02-02 | cyber | CISA adds at least one CVE from Citrix bulletins CTX697305 or CTX697320, the NetScaler ADC, Gateway and Console flaws patched on 2026-11-12, to the KEV catalog between 2026-11-13 and 2027-01-29. | TRUE if the CISA KEV JSON feed shows a dateAdded between 2026-11-13 and 2027-01-29 for any CVE listed in Citrix bulletin CTX697305 or CTX697320; FALSE otherwise. |
| KKR-20261112-37 | 55% | 2026-11-24 | political | Donald Trump, Xi Jinping and Vladimir Putin hold a dedicated in-person three-way meeting between 2026-11-13 and 2026-11-22, the window around the APEC leaders meeting in Shenzhen. | TRUE if at least two of Reuters, AP and AFP report a dedicated in-person meeting of all three leaders held between 2026-11-13 and 2026-11-22; plenaries, gala dinners and group photos do not count. |
| KKR-20261112-38 | 20% | 2027-03-02 | political | The Commerce Department adds Megaspeed, the company at the center of the Nvidia scandal, to the Entity List in a rule published between 2026-11-13 and 2027-02-26. | TRUE if a BIS rule published in the Federal Register between 2026-11-13 and 2027-02-26 adds an entry naming Megaspeed, under any corporate or address variant, to the Entity List; FALSE otherwise. |
| KKR-20261112-39 | 40% | 2027-03-02 | crime/security | At least one of the two Iranian nationals convicted on 2026-11-12 of assisting Iranian intelligence, Sepahvand or Manesh, receives a custodial term of 10 years or more, imposed between 2026-12-14 and 2027-02-26. | TRUE if judiciary.uk sentencing remarks, a CPS statement or PA reporting show Sepahvand or Manesh given a custodial term of 10 years or more, excluding extended licence, imposed between 2026-12-14 and 2027-02-26; FALSE otherwise. |
| KKR-20261112-40 | 55% | 2027-04-05 | disaster | The New Zealand government classifies drought conditions in at least one region as a medium-scale or larger adverse event, announced between 2026-11-13 and 2027-03-31. | TRUE if an MPI or Beehive.govt.nz release dated between 2026-11-13 and 2027-03-31 announces a new or expanded drought classification at medium-scale or larger for any New Zealand region; FALSE otherwise. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The PLA Eastern Theater Command announces a named large-scale joint exercise around Taiwan, comparable to the Joint Sword and Strait Thunder" → REJECTED: resolution offers alternative VENUES joined by 'or' (…-11-13 and 2027-01-31, as reported by reuters | or | ap…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "Nvidia announces a permanent, non-interim chief executive, whether Colette Kress or another person, with the announcement dated between 2026" → REJECTED: resolution offers alternative VENUES joined by 'or' (…an nvidia press release | or | sec form 8-k on edgar dated…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "CISA adds the Windows privilege-escalation flaw released as the SignDrop zero-day on 2026-11-12 to the KEV catalog between 2026-11-13 and 20" → REJECTED: resolution offers alternative VENUES joined by 'or' (…signdrop, as mapped by the microsoft advisory | or | bleepingcomputer…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

5688 issued all-time across 23 forecaster arms · 3966 open (1628 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/opus-5.5/unattested`:** 388 issued · 374 open · 14 resolved · 8 hits / 6 misses · **Brier 0.312** against its own base rate 57.1% (climatological 0.245) · **skill -0.275** · under 30 resolved, this is noise.

*96 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1788 | 1279 | 477 | 273 | 204 | 0.300 | 57.2% | 0.245 | -0.226 |
| control/trailing | 187 | 187 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 9 | 11 | 1 | 10 | 0.123 | 9.1% | 0.083 | -0.490 |
| lmstudio/auto[post-window] | 470 | 201 | 259 | 75 | 184 | 0.204 | 29.0% | 0.206 | +0.009 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 207 | 190 | 11 | 4 | 7 | 0.227 | 36.4% | 0.231 | +0.020 |
| lmstudio/qwen36-abliterated | 212 | 210 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
| lmstudio/qwen36-realist | 189 | 156 | 31 | 10 | 21 | 0.242 | 32.3% | 0.219 | -0.106 |
| lmstudio/realist | 249 | 128 | 119 | 66 | 53 | 0.317 | 55.5% | 0.247 | -0.285 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 14 | 24 | 14 | 10 | 0.164 | 58.3% | 0.243 | +0.325 |
| manual/fable-5.1/unattested | 535 | 420 | 107 | 61 | 46 | 0.211 | 57.0% | 0.245 | +0.140 |
| manual/fable-5.2/unattested | 12 | 12 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 258 | 147 | 102 | 65 | 37 | 0.203 | 63.7% | 0.231 | +0.121 |
| manual/opus-5 | 74 | 39 | 35 | 18 | 17 | 0.213 | 51.4% | 0.250 | +0.146 |
| manual/opus-5.5/unattested | 388 | 374 | 14 | 8 | 6 | 0.312 | 57.1% | 0.245 | -0.275 |
| manual/opus-5/unattested | 326 | 221 | 95 | 61 | 34 | 0.208 | 64.2% | 0.230 | +0.097 |
| manual/sonnet-5 | 45 | 3 | 41 | 22 | 19 | 0.250 | 53.7% | 0.249 | -0.007 |
| manual/sonnet-5.5/unattested | 222 | 207 | 15 | 10 | 5 | 0.122 | 66.7% | 0.222 | +0.451 |
| manual/sonnet-5/unattested | 342 | 141 | 196 | 98 | 98 | 0.245 | 50.0% | 0.250 | +0.019 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*
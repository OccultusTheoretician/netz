**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 071817Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-07_1518.md · forecaster: control/baserate · 7 accepted / 3 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260907-41 | 35% | 2026-12-04 | political | Following the AfD first-place finish in the 6 September 2026 Saxony-Anhalt Landtag election reported in the packet, the Saxony-Anhalt Landtag will elect an AfD-nominated Minister-President in a floor vote between 2026-09-14 and 2026-12-01. | TRUE if the Saxony-Anhalt Landtag confirms an AfD-nominated Minister-President by floor vote in the window, per official Landtag records and at least one of dpa, Reuters, or AP; else FALSE. |
| KKR-20260907-42 | 35% | 2026-11-16 | political | Following the resignation of the senior AI policy adviser to the UK government over an Anthropic conflict of interest, reported 2026-09-07, the UK government will publicly name a permanent successor to that role between 2026-09-14 and 2026-11-13. | TRUE if the UK government publicly names, via a GOV.UK release or a wire service report, PA Media or Reuters, a permanent successor to the role within the window; else FALSE. |
| KKR-20260907-43 | 21% | 2026-10-13 | economics/markets | Reference: the 10-year Treasury yield was 4.78 percent per the market snapshot in the packet dated 2026-09-07. The FRED DGS10 series will show a daily 10-year Treasury yield at or above 4.95 percent on at least one day between 2026-09-14 and 2026-10-09. | TRUE if the FRED DGS10 daily series records a value at or above 4.95 percent on any date in the window; else FALSE. |
| KKR-20260907-44 | 30% | 2026-10-22 | cyber | Following the report of a Telerik UI padding-oracle bug chained to unauthenticated remote code execution, the CISA Known Exploited Vulnerabilities catalog will add a Telerik UI entry between 2026-09-14 and 2026-10-19. | TRUE if the CISA KEV catalog carries a dateAdded value for a Telerik UI CVE falling within the window; else FALSE. |
| KKR-20260907-45 | 49% | 2026-10-15 | military/conflict | Amid reports questioning whether Iran can enforce a restricted zone in the Strait of Hormuz, the government of Iran or the IRGC Navy will formally declare a named restricted or exclusion zone in the Strait of Hormuz between 2026-09-14 and 2026-10-12. | TRUE if Iranian state media, meaning IRNA, Tasnim, or Mehr, and at least one of Reuters, AP, or AFP both report a formally declared, named Hormuz restricted zone within the window; else FALSE. |
| KKR-20260907-46 | 49% | 2026-11-16 | military/conflict | Following reports of Israel-Hezbollah clashes killing 11 and Israeli strikes on a southern Lebanese village killing 12, a formally announced ceasefire or truce covering Israel-Hezbollah hostilities in southern Lebanon will take effect between 2026-09-14 and 2026-11-13. | TRUE if the government of Israel, the government of Lebanon, or Hezbollah announces a ceasefire or truce that takes effect in the window, corroborated by a Western wire service and a regional outlet; else FALSE. |
| KKR-20260907-47 | 36% | 2026-10-15 | disaster | Reference: the packet dated 2026-09-07 reports more than 1,300 confirmed dead in the Nepal flooding. The cumulative confirmed death toll reported by disaster authorities in Nepal will reach or exceed 1,500 between 2026-09-14 and 2026-10-12. | TRUE if the NDRRMA of Nepal, a Nepal government source, or a wire service, AP, Reuters, or AFP, reports a cumulative confirmed death toll at or above 1,500 within the window; else FALSE. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Reference: Brent crude settled at 96.28 USD per barrel per the market snapshot in the packet dated 2026-09-07. Brent front-month futures wil" → REJECTED: resolution offers alternative VENUES joined by 'or' (…ice brent 1st-month futures settlement price, | or | the eia brent spot price series if unavailabl…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "Following reports that N-able patched a maximum-severity N-central flaw amid ongoing attacks and issued a fourth N-central hotfix in five we" → REJECTED: the resolution names only a venue or register (CISA, KEV, cve) and no subject - the register is where to look, not what is claimed; name the subject inside it
- "Following the opening of the Paris trial over the killing of former Argentina rugby international Federico Aramburu, reported 2026-09-07, a " → REJECTED: resolution offers alternative VENUES joined by 'or' (…court docket | or | a…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact; the resolution names only a venue or register (AFP, Reuters) and no subject - the register is where to look, not what is claimed; name the subject inside it

## III. LEDGER STANDING

1657 issued all-time across 16 forecaster arms · 1392 open (90 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 491 issued · 463 open · 28 resolved · 14 hits / 14 misses · **Brier 0.297** against its own base rate 50.0% (climatological 0.250) · **skill -0.187** · under 30 resolved, this is noise.

*16 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 491 | 463 | 28 | 14 | 14 | 0.297 | 50.0% | 0.250 | -0.187 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 227 | 139 | 83 | 15 | 68 | 0.183 | 18.1% | 0.148 | -0.234 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 25 | 25 | 0 | — | — | not computed | — | — | — |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 32 | 6 | 4 | 2 | 0.070 | 66.7% | 0.222 | +0.687 |
| manual/fable-5.1/unattested | 45 | 45 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 180 | 178 | 2 | 2 | 0 | 0.225 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 199 | 193 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 20 | 25 | 14 | 11 | 0.231 | 56.0% | 0.246 | +0.064 |
| manual/sonnet-5/unattested | 187 | 166 | 21 | 10 | 11 | 0.214 | 47.6% | 0.249 | +0.141 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*
**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 181515Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-18_1512.md · forecaster: lmstudio/realist · 3 accepted / 7 rejected by validation gate · 1 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261018-08 | 25% | 2026-10-29 | cyber | Between 2026-10-21 and 2026-10-27, a cyberattack exploiting the SiteGuard WAF vulnerability (CVE-2026-XXXX) will be confirmed by CISA KEV catalog with a date-added value between 2026-10-20 and 2026-10-26. | The CISA KEV catalog carries a date-added value between 2026-10-20 and 2026-10-26 for a vulnerability with a name matching 'SiteGuard WAF' or a CVE identifier linked to the exploit described in item 9. |
| KKR-20261018-09 | 45% | 2026-10-28 | economics/markets | On 2026-10-25, the 10-year U.S. Treasury yield will exceed 5.15 percent, based on the prior-session close of 5.10 percent on 2026-10-18. | The 10-year U.S. Treasury yield exceeds 5.15 percent on 2026-10-25, as reported by the U.S. Department of the Treasury or FRED. |
| KKR-20261018-10 | 35% | 2026-11-04 | political | Between 2026-10-27 and 2026-11-02, a new diplomatic crisis will emerge between Iran and the U.S. over the Strait of Hormuz, confirmed by a public statement from both sides and corroborated by at least two independent news outlets. | A public statement from Iran and the U.S. regarding a crisis over the Strait of Hormuz is issued between 2026-10-27 and 2026-11-02, and the event is independently corroborated by at least two independent news outlets (e.g., BBC, Al Jazeera). |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "On 2026-10-20, a drone strike originating from the Russia-Ukraine theatre will result in at least one confirmed casualty in Zaporizhzhia, as" → REJECTED: cited items name France, Palestine, State of; the claim is about zone:russia_ukraine — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else; resolution offers alternative VENUES joined by 'or' (…borated by a third-party source such as gdacs | or | usgs…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "On 2026-10-23, the S&P 500 will close below 7,600, based on the prior-session close of 7,659.44 on 2026-10-18." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "Between 2026-10-22 and 2026-10-28, a major wildfire will be confirmed in Alberta, Canada, with a GDACS alert issued and at least 500 hectare" → REJECTED: the named venue is introduced by 'e.g.', which makes it an example rather than the source of record — the adjudicator still chooses. Strike the softener or name the class exhaustively
- "Between 2026-10-24 and 2026-10-30, a coordinated cyberattack on a U.S. federal agency will be confirmed by CISA KEV catalog with a date-adde" → REJECTED: cited items name Palestine, State of; the claim is about United States — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else
- "On 2026-10-26, a French government official will be indicted for corruption related to the Manchester City housing loan scandal, as confirme" → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-10-26 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "Between 2026-10-28 and 2026-11-03, a new offensive operation in the Russia-Ukraine theatre will be confirmed by at least two Grade A reports" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "On 2026-10-29, a major earthquake of magnitude 6.0 or higher will be recorded by USGS in the Pacific Northwest, with a confirmed epicenter w" → REJECTED: cited items name Pakistan; the claim is about Idaho, Oregon, Washington — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else; single-day resolution window for an unscheduled event — the row requires this to occur on 2026-10-29 exactly. Price a day, not a window: widen the window or state why the date is fixed

## III. LEDGER STANDING

4416 issued all-time across 21 forecaster arms · 3305 open (547 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/realist`:** 230 issued · 171 open · 58 resolved · 31 hits / 27 misses · **Brier 0.296** against its own base rate 53.4% (climatological 0.249) · **skill -0.191**.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1556 | 1260 | 264 | 161 | 103 | 0.313 | 61.0% | 0.238 | -0.317 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 11 | 9 | 1 | 8 | 0.146 | 11.1% | 0.099 | -0.474 |
| lmstudio/auto[post-window] | 444 | 221 | 214 | 63 | 151 | 0.209 | 29.4% | 0.208 | -0.007 |
| lmstudio/auto[pre-verbot] | 60 | 4 | 48 | 13 | 35 | 0.214 | 27.1% | 0.197 | -0.085 |
| lmstudio/qwen36 | 75 | 75 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 72 | 72 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 79 | 79 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 230 | 171 | 58 | 31 | 27 | 0.296 | 53.4% | 0.249 | -0.191 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 20 | 18 | 10 | 8 | 0.164 | 55.6% | 0.247 | +0.334 |
| manual/fable-5.1/unattested | 372 | 314 | 50 | 34 | 16 | 0.248 | 68.0% | 0.218 | -0.140 |
| manual/fable-5/unattested | 258 | 179 | 70 | 47 | 23 | 0.190 | 67.1% | 0.221 | +0.138 |
| manual/opus-5 | 74 | 44 | 30 | 14 | 16 | 0.210 | 46.7% | 0.249 | +0.156 |
| manual/opus-5.5/unattested | 203 | 198 | 5 | 3 | 2 | 0.440 | 60.0% | 0.240 | -0.835 |
| manual/opus-5/unattested | 326 | 265 | 51 | 34 | 17 | 0.182 | 66.7% | 0.222 | +0.182 |
| manual/sonnet-5 | 45 | 5 | 39 | 21 | 18 | 0.262 | 53.8% | 0.249 | -0.055 |
| manual/sonnet-5.5/unattested | 156 | 156 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 206 | 131 | 69 | 62 | 0.249 | 52.7% | 0.249 | +0.000 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*
**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 161514Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-16_1513.md · forecaster: lmstudio/auto · 3 accepted / 7 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261016-01 | 20% | 2026-11-02 | political | The European Parliament passes a resolution calling for the suspension of all EU military aid to Israel between 2026-10-25 and 2026-10-31. | The European Parliament's official website (europarl.europa.eu) publishes a resolution titled 'Suspension of EU military aid to Israel' with a vote date between 2026-10-25 and 2026-10-31. |
| KKR-20261016-02 | 40% | 2026-11-02 | cyber | A U.S. federal agency issues a public advisory warning of a coordinated cyberattack on critical infrastructure by a China-linked threat group between 2026-10-24 and 2026-10-31. | The CISA Advisories page (cisa.gov) publishes a new advisory titled 'China-Linked Threat Group Targets Critical Infrastructure' with a publication date between 2026-10-24 and 2026-10-31. |
| KKR-20261016-03 | 20% | 2026-11-05 | military/conflict | A drone strike on a civilian facility in Gaza City, Palestine, results in at least five confirmed casualties between 2026-10-27 and 2026-11-03. | Two independent wire services (e.g., Al Jazeera, BBC World) report at least five confirmed casualties from a drone strike on a civilian facility in Gaza City between 2026-10-27 and 2026-11-03. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "A drone strike targeting a military installation in Kyiv, Ukraine, occurs between 2026-10-21 and 2026-10-24, resulting in at least one confi" → REJECTED: cited items name Israel; the claim is about Ukraine, zone:russia_ukraine — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else; the named venue is introduced by 'e.g.', which makes it an example rather than the source of record — the adjudicator still chooses. Strike the softener or name the class exhaustively
- "The S&P 500 closes below 7,600.00 on or before 2026-11-06." → REJECTED: market-price resolution with weekend deadline — no settlement exists that day; resolution offers alternative VENUES joined by 'or' (…d by the federal reserve economic data (fred) | or | a major financial exchange…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "A zero-day exploit targeting Atlassian products is actively used in a cyberattack on a U.S. federal agency between 2026-10-22 and 2026-10-28" → REJECTED: cited items name Russian Federation; the claim is about United States — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else; the resolution names a different subject than the statement — the claim is about Atlassian and the resolution settles on CISA, CVE, KEV, cve-2026-21589. A row whose resolution checks a different fact can be scored correct while being wrong; the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-21589 dateAdded 2026-10-15, before the claimed window 2026-10-22..2026-10-28; dateAdded is single-valued and a fresh in-window value would require removal-and-relisting, which has no documented precedent (removals exist: CVE-2022-28958, removed 2023-12-01)
- "A magnitude 6.5 or greater earthquake with a depth less than 100 km occurs in the Pacific Northwest region of the United States between 2026" → REJECTED: cited items name Congo, Russian Federation; the claim is about California, Idaho, Oregon, United States, Washington — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else
- "A cyberattack exploiting a vulnerability in FortiOS software results in a data breach at a major U.S. financial institution between 2026-10-" → REJECTED: resolution offers alternative VENUES joined by 'or' (…public report from cisa | or | a major financial…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "A wildfire in Southern California spreads beyond 500 acres and causes at least one fatality between 2026-11-05 and 2026-11-12." → REJECTED: the resolution narrows the claim with a qualifier the statement never makes — green. The forecaster is graded on the statement; a severity or status qualifier living only in the resolution is invisible to anyone reading the claim
- "A major political protest in Kyiv, Ukraine, results in the resignation of a senior government official between 2026-10-26 and 2026-11-02." → REJECTED: the named venue is introduced by 'e.g.', which makes it an example rather than the source of record — the adjudicator still chooses. Strike the softener or name the class exhaustively

## III. LEDGER STANDING

4246 issued all-time across 21 forecaster arms · 3135 open (525 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/auto[post-window]`:** 432 issued · 209 open · 214 resolved · 63 hits / 151 misses · **Brier 0.209** against its own base rate 29.4% (climatological 0.208) · **skill -0.007**.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1501 | 1205 | 264 | 161 | 103 | 0.313 | 61.0% | 0.238 | -0.317 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 11 | 9 | 1 | 8 | 0.146 | 11.1% | 0.099 | -0.474 |
| lmstudio/auto[post-window] | 432 | 209 | 214 | 63 | 151 | 0.209 | 29.4% | 0.208 | -0.007 |
| lmstudio/auto[pre-verbot] | 60 | 4 | 48 | 13 | 35 | 0.214 | 27.1% | 0.197 | -0.085 |
| lmstudio/qwen36 | 65 | 65 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 60 | 60 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 63 | 63 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 220 | 161 | 58 | 31 | 27 | 0.296 | 53.4% | 0.249 | -0.191 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 20 | 18 | 10 | 8 | 0.164 | 55.6% | 0.247 | +0.334 |
| manual/fable-5.1/unattested | 354 | 296 | 50 | 34 | 16 | 0.248 | 68.0% | 0.218 | -0.140 |
| manual/fable-5/unattested | 258 | 179 | 70 | 47 | 23 | 0.190 | 67.1% | 0.221 | +0.138 |
| manual/opus-5 | 74 | 44 | 30 | 14 | 16 | 0.210 | 46.7% | 0.249 | +0.156 |
| manual/opus-5.5/unattested | 184 | 179 | 5 | 3 | 2 | 0.440 | 60.0% | 0.240 | -0.835 |
| manual/opus-5/unattested | 326 | 265 | 51 | 34 | 17 | 0.182 | 66.7% | 0.222 | +0.182 |
| manual/sonnet-5 | 45 | 5 | 39 | 21 | 18 | 0.262 | 53.8% | 0.249 | -0.055 |
| manual/sonnet-5.5/unattested | 138 | 138 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 206 | 131 | 69 | 62 | 0.249 | 52.7% | 0.249 | +0.000 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*
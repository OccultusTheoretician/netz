**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 092054Z NOV 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-11-09_1611.md · forecaster: manual/opus-5.5/unattested · 8 accepted / 2 rejected by validation gate · 5 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261109-27 | 60% | 2026-12-03 | military/conflict | Between 2026-11-10 and 2026-11-30, the IRGC or Iranian forces strike or seize at least one additional commercial tanker in or near the Strait of Hormuz. | True if Reuters, AP, or UKMTO reports at least one new tanker strike or seizure by Iranian forces near Hormuz dated between 2026-11-10 and 2026-11-30. |
| KKR-20261109-28 | 30% | 2027-01-04 | economics/markets | Brent crude front-month settles above 100 USD per barrel on at least one trading day between 2026-11-10 and 2026-12-31. Reference: 94.80 on the packet date. | True if ICE Brent front-month daily settlement exceeds 100.00 USD on any trading day from 2026-11-10 to 2026-12-31. Reference: 94.80 on the packet date. |
| KKR-20261109-29 | 8% | 2027-02-03 | military/conflict | A formal ceasefire or comprehensive peace agreement between Russia and Ukraine is signed by both governments between 2026-11-10 and 2027-01-31. | True if Russia and Ukraine both sign a ceasefire or peace agreement between 2026-11-10 and 2027-01-31, as reported by Reuters and AP. |
| KKR-20261109-30 | 22% | 2027-02-03 | political | Jensen Huang ceases to be CEO of Nvidia, via resignation, removal, or announced leave, between 2026-11-10 and 2027-01-31. | True if Nvidia files an SEC 8-K or issues a press release between 2026-11-10 and 2027-01-31 stating Huang has resigned, been removed, or taken leave as CEO. |
| KKR-20261109-31 | 55% | 2026-12-17 | cyber | The CISA KEV catalog adds an OpenSSH vulnerability with a date-added value between 2026-11-10 and 2026-12-15. | True if the CISA KEV catalog lists an OpenSSH CVE with dateAdded between 2026-11-10 and 2026-12-15. |
| KKR-20261109-32 | 55% | 2027-01-04 | political | The EU formally nominates or agrees on a new ECB President candidate between 2026-11-10 and 2026-12-31. | True if the Eurogroup or European Council publicly names its chosen candidate for ECB President between 2026-11-10 and 2026-12-31, per official EU press release. |
| KKR-20261109-33 | 25% | 2027-02-03 | political | A US federal government funding lapse (shutdown) begins between 2026-11-10 and 2027-01-31. | True if federal appropriations lapse and OMB directs a shutdown of agencies on any date between 2026-11-10 and 2027-01-31, per Congress.gov and wire reporting. |
| KKR-20261109-34 | 10% | 2027-01-05 | disaster | USGS records an earthquake of magnitude 7.0 or greater within 300 km of the Solomon Islands between 2026-11-10 and 2026-12-31. | True if the USGS earthquake catalog lists an M7.0+ event within 300 km of Lata or Honiara with an origin time between 2026-11-10 and 2026-12-31. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The US 10-year Treasury yield closes above 5.00 percent on at least one day between 2026-11-10 and 2026-12-31. Reference: 4.88 percent on th" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "Polish prosecutors publicly announce a motive or ideological link for the Krakow shooting between 2026-11-10 and 2026-12-10." → REJECTED: resolution offers alternative VENUES joined by 'or' (…2026-11-10 and 2026-12-10, as reported by bbc | or | reuters…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

5508 issued all-time across 22 forecaster arms · 3786 open (1345 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/opus-5.5/unattested`:** 364 issued · 350 open · 14 resolved · 8 hits / 6 misses · **Brier 0.312** against its own base rate 57.1% (climatological 0.245) · **skill -0.275** · under 30 resolved, this is noise.

*96 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1788 | 1279 | 477 | 273 | 204 | 0.300 | 57.2% | 0.245 | -0.226 |
| control/trailing | 115 | 115 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 9 | 11 | 1 | 10 | 0.123 | 9.1% | 0.083 | -0.490 |
| lmstudio/auto[post-window] | 470 | 201 | 259 | 75 | 184 | 0.204 | 29.0% | 0.206 | +0.009 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 195 | 178 | 11 | 4 | 7 | 0.227 | 36.4% | 0.231 | +0.020 |
| lmstudio/qwen36-abliterated | 196 | 194 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
| lmstudio/qwen36-realist | 171 | 138 | 31 | 10 | 21 | 0.242 | 32.3% | 0.219 | -0.106 |
| lmstudio/realist | 249 | 128 | 119 | 66 | 53 | 0.317 | 55.5% | 0.247 | -0.285 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 14 | 24 | 14 | 10 | 0.164 | 58.3% | 0.243 | +0.325 |
| manual/fable-5.1/unattested | 509 | 394 | 107 | 61 | 46 | 0.211 | 57.0% | 0.245 | +0.140 |
| manual/fable-5/unattested | 258 | 147 | 102 | 65 | 37 | 0.203 | 63.7% | 0.231 | +0.121 |
| manual/opus-5 | 74 | 39 | 35 | 18 | 17 | 0.213 | 51.4% | 0.250 | +0.146 |
| manual/opus-5.5/unattested | 364 | 350 | 14 | 8 | 6 | 0.312 | 57.1% | 0.245 | -0.275 |
| manual/opus-5/unattested | 326 | 221 | 95 | 61 | 34 | 0.208 | 64.2% | 0.230 | +0.097 |
| manual/sonnet-5 | 45 | 3 | 41 | 22 | 19 | 0.250 | 53.7% | 0.249 | -0.007 |
| manual/sonnet-5.5/unattested | 222 | 207 | 15 | 10 | 5 | 0.122 | 66.7% | 0.222 | +0.451 |
| manual/sonnet-5/unattested | 342 | 141 | 196 | 98 | 98 | 0.245 | 50.0% | 0.250 | +0.019 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*
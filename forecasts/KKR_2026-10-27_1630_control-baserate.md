**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 271630Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-27_1516.md · forecaster: control/baserate · 8 accepted / 2 rejected by validation gate · 0 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261027-29 | 45% | 2026-12-02 | cyber | The CISA KEV catalog adds at least one PHP Group PHP CVE other than CVE-2026-109618 and CVE-2026-109619 with a date-added value between 2026-10-28 and 2026-11-30. | True if the CISA KEV catalog JSON shows a PHP Group PHP entry, excluding CVE-2026-109618 and CVE-2026-109619, with dateAdded between 2026-10-28 and 2026-11-30 inclusive. |
| KKR-20261027-30 | 45% | 2027-01-05 | cyber | The CISA KEV catalog adds a CVE for the Brotli compression flaw called HTTP2Shell, affecting .NET or the Brotli library, with a date-added value between 2026-10-28 and 2026-12-31. | True if the CISA KEV catalog JSON contains an entry whose vendor or product is Google Brotli or Microsoft .NET describing the Brotli flaw, with dateAdded between 2026-10-28 and 2026-12-31 inclusive. |
| KKR-20261027-31 | 44% | 2027-04-20 | crime/security | The third federal case against James Comey produces a conviction, meaning a jury guilty verdict or an accepted guilty plea, between 2026-10-28 and 2027-04-15. | True if a federal court docket on PACER or CourtListener records a guilty verdict or accepted guilty plea for Comey in that case between 2026-10-28 and 2027-04-15 inclusive. |
| KKR-20261027-32 | 59% | 2026-12-01 | economics/markets | WTI crude front-month futures settle below 90.00 dollars per barrel on at least one trading day between 2026-10-28 and 2026-11-27. Reference: 100.01 on the packet date. | True if the CME NYMEX official daily settlement for the front-month WTI contract is below 90.00 on any trading day from 2026-10-28 through 2026-11-27 inclusive. |
| KKR-20261027-33 | 63% | 2026-12-02 | military/conflict | The Ukrainian government officially declares the localised Oleshky ceasefire ended, suspended, or collapsed between 2026-10-28 and 2026-11-30. | True if at least two of Reuters, AP, AFP report an official statement from the Ukrainian presidency, foreign ministry, or general staff that the Oleshky ceasefire has ended, been suspended, or collapsed, dated within the window. |
| KKR-20261027-34 | 38% | 2027-01-05 | disaster | WHO reports cumulative confirmed and probable Ebola cases in the DR Congo outbreak of at least 15,000 in a Disease Outbreak News or situation report published between 2026-10-28 and 2026-12-31. | True if a WHO Disease Outbreak News item or WHO situation report published in the window states a cumulative case count of 15,000 or more for this DRC Ebola outbreak. |
| KKR-20261027-35 | 44% | 2026-11-12 | crime/security | The man serving a life sentence who escaped a Tennessee prison on or about 2026-10-27 is taken back into custody between 2026-10-28 and 2026-11-10. | True if the Tennessee Department of Correction, TBI, or a county sheriff announces the escapee is in custody, confirmed by at least one of AP, Reuters, or the Tennessean, dated within the window. |
| KKR-20261027-36 | 63% | 2027-01-05 | military/conflict | Israeli or US strikes hit targets on Iranian territory between 2026-11-04 and 2026-12-31. | True if at least two of Reuters, AP, AFP report strikes on Iranian territory attributed to Israel or the US, and Iranian state media or an Iranian government body acknowledges strikes occurred, within the window. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Benjamin Netanyahu is sworn in by the Knesset as prime minister of a new Israeli government following the 2026-10-27 election, between 2026-" → REJECTED: resolution offers alternative VENUES joined by 'or' (…the knesset website | or | at least two of reuters, ap, afp record a kne…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "The FOMC statement issued 2026-10-28 announces no change to the federal funds target range." → REJECTED: measurable claim without a numeric threshold — a row about a quantity must state the number next to its comparator; identifier digits (H.15, S&P 500) do not count

## III. LEDGER STANDING

5060 issued all-time across 21 forecaster arms · 3338 open (400 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 1778 issued · 1269 open · 477 resolved · 273 hits / 204 misses · **Brier 0.300** against its own base rate 57.2% (climatological 0.245) · **skill -0.226**.

*96 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1778 | 1269 | 477 | 273 | 204 | 0.300 | 57.2% | 0.245 | -0.226 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 9 | 11 | 1 | 10 | 0.123 | 9.1% | 0.083 | -0.490 |
| lmstudio/auto[post-window] | 470 | 201 | 259 | 75 | 184 | 0.204 | 29.0% | 0.206 | +0.009 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 125 | 108 | 11 | 4 | 7 | 0.227 | 36.4% | 0.231 | +0.020 |
| lmstudio/qwen36-abliterated | 130 | 128 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
| lmstudio/qwen36-realist | 126 | 93 | 31 | 10 | 21 | 0.242 | 32.3% | 0.219 | -0.106 |
| lmstudio/realist | 249 | 128 | 119 | 66 | 53 | 0.317 | 55.5% | 0.247 | -0.285 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 14 | 24 | 14 | 10 | 0.164 | 58.3% | 0.243 | +0.325 |
| manual/fable-5.1/unattested | 455 | 340 | 107 | 61 | 46 | 0.211 | 57.0% | 0.245 | +0.140 |
| manual/fable-5/unattested | 258 | 147 | 102 | 65 | 37 | 0.203 | 63.7% | 0.231 | +0.121 |
| manual/opus-5 | 74 | 39 | 35 | 18 | 17 | 0.213 | 51.4% | 0.250 | +0.146 |
| manual/opus-5.5/unattested | 276 | 262 | 14 | 8 | 6 | 0.312 | 57.1% | 0.245 | -0.275 |
| manual/opus-5/unattested | 326 | 221 | 95 | 61 | 34 | 0.208 | 64.2% | 0.230 | +0.097 |
| manual/sonnet-5 | 45 | 3 | 41 | 22 | 19 | 0.250 | 53.7% | 0.249 | -0.007 |
| manual/sonnet-5.5/unattested | 222 | 207 | 15 | 10 | 5 | 0.122 | 66.7% | 0.222 | +0.451 |
| manual/sonnet-5/unattested | 342 | 141 | 196 | 98 | 98 | 0.245 | 50.0% | 0.250 | +0.019 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*
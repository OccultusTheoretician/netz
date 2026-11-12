**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 121804Z NOV 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-11-12_1613.md · forecaster: control/trailing · 9 accepted / 0 rejected by validation gate · 0 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261112-25 | 69% | 2026-12-22 | economics/markets | The FRED DGS10 10-year Treasury constant maturity yield for 2026-12-18 is at or above 5.00 percent. Reference: 5.07 percent on the packet date. | The FRED DGS10 observation dated 2026-12-18 is 5.00 or higher. If that date has no observation, the next published observation governs. |
| KKR-20261112-26 | 69% | 2027-03-02 | economics/markets | Nvidia files a Form 8-K on SEC EDGAR between 2026-11-13 and 2027-02-26 announcing appointment of a chief executive officer with no interim or acting designation. | SEC EDGAR shows an Nvidia 8-K, filed between 2026-11-13 and 2027-02-26, under Item 5.02 naming a CEO appointment without the words interim or acting. |
| KKR-20261112-27 | 55% | 2027-01-19 | cyber | The CISA KEV catalog adds CVE-2026-118383, the pre-auth MongoDB flaw, with a dateAdded between 2026-11-12 and 2027-01-15. | The CISA KEV JSON feed contains an entry with cveID CVE-2026-118383 and dateAdded between 2026-11-12 and 2027-01-15 inclusive. |
| KKR-20261112-28 | 55% | 2027-01-19 | cyber | The CISA KEV catalog adds an entry with vendorProject Apache and product HTTP Server with a dateAdded between 2026-11-12 and 2027-01-15. | The CISA KEV JSON feed contains at least one entry whose vendorProject is Apache, whose product is HTTP Server, and whose dateAdded falls between 2026-11-12 and 2027-01-15 inclusive. |
| KKR-20261112-29 | 42% | 2027-01-12 | political | Scott Colom is seated as United States Senator from Mississippi with service beginning on or before 2027-01-06. | The Congress.gov or Senate.gov member record for Scott Colom shows Senate service for Mississippi with a start date on or before 2027-01-06. |
| KKR-20261112-30 | 42% | 2027-01-19 | political | Indonesia's People's Consultative Assembly elects or swears in a replacement Vice President between 2026-11-12 and 2027-01-16. | Reuters and Antara both report an MPR plenary session that elected or inaugurated a new Vice President of Indonesia on a date between 2026-11-12 and 2027-01-16. |
| KKR-20261112-31 | 65% | 2027-01-05 | military/conflict | The Russian and Ukrainian governments both announce a general ceasefire covering the full front line, with a stated effective date, between 2026-11-12 and 2026-12-31. | Reuters and AP both report official announcements from both governments, made between 2026-11-12 and 2026-12-31, of a general ceasefire across the front with an effective date. |
| KKR-20261112-32 | 65% | 2027-02-03 | military/conflict | The PLA Eastern Theater Command announces a named joint exercise around Taiwan, confirmed by Taiwan's Ministry of National Defense, starting between 2026-11-13 and 2027-01-31. | Taiwan MND public statements and Reuters both identify a PLA joint exercise around Taiwan carrying a PLA-assigned name, with a start date between 2026-11-13 and 2027-01-31. |
| KKR-20261112-33 | 65% | 2026-12-16 | military/conflict | Iranian state forces board, seize, or detain a commercial tanker in the Strait of Hormuz, Persian Gulf, or Gulf of Oman between 2026-11-13 and 2026-12-13. | UKMTO advisories and Reuters both report Iranian boarding, seizure, or detention of a commercial tanker in those waters on a date between 2026-11-13 and 2026-12-13. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

Nothing rejected — every projection cleared the gate.

## III. LEDGER STANDING

5681 issued all-time across 23 forecaster arms · 3959 open (1628 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/trailing`:** 187 issued · 187 open · nothing resolved yet — this arm earns a score at its first resolution.

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
| manual/opus-5.5/unattested | 381 | 367 | 14 | 8 | 6 | 0.312 | 57.1% | 0.245 | -0.275 |
| manual/opus-5/unattested | 326 | 221 | 95 | 61 | 34 | 0.208 | 64.2% | 0.230 | +0.097 |
| manual/sonnet-5 | 45 | 3 | 41 | 22 | 19 | 0.250 | 53.7% | 0.249 | -0.007 |
| manual/sonnet-5.5/unattested | 222 | 207 | 15 | 10 | 5 | 0.122 | 66.7% | 0.222 | +0.451 |
| manual/sonnet-5/unattested | 342 | 141 | 196 | 98 | 98 | 0.245 | 50.0% | 0.250 | +0.019 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*
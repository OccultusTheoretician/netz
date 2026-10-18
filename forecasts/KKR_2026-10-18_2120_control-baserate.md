**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 182120Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-18_1512.md · forecaster: control/baserate · 6 accepted / 4 rejected by validation gate · 0 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261018-34 | 41% | 2026-11-24 | cyber | CISA adds a SiteGuard WAF vulnerability to the Known Exploited Vulnerabilities catalog with a dateAdded between 2026-10-19 and 2026-11-20. | The CISA KEV JSON feed contains an entry whose vendorProject or product field includes SiteGuard, with dateAdded between 2026-10-19 and 2026-11-20 inclusive. |
| KKR-20261018-35 | 41% | 2026-12-02 | cyber | ConnectWise publicly announces that its Cloud Backup service, suspended after the Microsoft 365 tenant compromises, is restored to general customer availability on a date between 2026-10-19 and 2026-11-30. | An official ConnectWise channel (trust center, status page, bulletin, or blog) dated between 2026-10-19 and 2026-11-30 inclusive states Cloud Backup is restored or re-enabled for customers generally. |
| KKR-20261018-36 | 42% | 2026-11-20 | disaster | An earthquake of magnitude 5.0 or greater occurs within 100 km of the epicenter of the M5.7 Khuzdar, Pakistan event (USGS id us6000u2y1) between 2026-10-19 and 2026-11-18. | The USGS ComCat catalog lists an event with magnitude at least 5.0, epicenter within 100 km of us6000u2y1, and origin time between 2026-10-19 00:00 UTC and 2026-11-18 23:59 UTC. |
| KKR-20261018-37 | 39% | 2026-11-04 | crime/security | French authorities announce a cumulative arrest total of at least 3,000 for the student-led protest wave that began in October 2026, for a period ending on or before 2026-11-01. Reference: 1,800 arrests announced as of 2026-10-18. | An official statement or post by the French Interior Ministry or the Paris Prefecture de Police gives a cumulative arrest figure of 3,000 or more for the protest wave, covering a period ending on or before 2026-11-01. |
| KKR-20261018-38 | 64% | 2026-11-04 | military/conflict | A Ukrainian drone strike hits an oil refinery, oil terminal, or fuel depot in St Petersburg or Leningrad Oblast between 2026-10-19 and 2026-11-01, acknowledged by Russian officials and claimed by Ukrainian officials. | Russian officials (regional governor or MoD) and Ukrainian officials (General Staff, SBU, or Unmanned Systems Forces) both acknowledge the same strike on an oil or fuel facility in St Petersburg or Leningrad Oblast dated 2026-10-19 to 2026-11-01. |
| KKR-20261018-39 | 64% | 2026-11-04 | military/conflict | A merchant vessel is attacked, hit by an explosion, boarded, or seized in the Strait of Hormuz, Persian Gulf, or Gulf of Oman between 2026-10-19 and 2026-11-01, as recorded by UKMTO. | UKMTO records an attack, explosion, boarding, or seizure of a merchant vessel in the Strait of Hormuz, Persian Gulf, or Gulf of Oman dated 2026-10-19 to 2026-11-01; suspicious approaches or hailing alone do not count. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Hurricane Trudy, Category 2 on 2026-10-17 while heading toward Mexico, reaches Category 3 or higher (maximum sustained winds at least 111 mp" → REJECTED: resolution offers alternative VENUES joined by 'or' (…advisory | or | tropical cyclone…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "The EIA daily Cushing WTI spot price (FRED series DCOILWTICO) is at or above 110.00 dollars per barrel on at least one trading day between 2" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "The FOMC statement released on 2026-10-28 leaves the target range for the federal funds rate unchanged from the range announced in the 2026-" → REJECTED: measurable claim without a numeric threshold — a row about a quantity must state the number next to its comparator; identifier digits (H.15, S&P 500) do not count
- "The French Government falls between 2026-10-18 and 2026-11-30: a presidential decree ending the functions of the Prime Minister, whether aft" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim

## III. LEDGER STANDING

4445 issued all-time across 21 forecaster arms · 3334 open (547 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 1562 issued · 1266 open · 264 resolved · 161 hits / 103 misses · **Brier 0.313** against its own base rate 61.0% (climatological 0.238) · **skill -0.317**.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1562 | 1266 | 264 | 161 | 103 | 0.313 | 61.0% | 0.238 | -0.317 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 11 | 9 | 1 | 8 | 0.146 | 11.1% | 0.099 | -0.474 |
| lmstudio/auto[post-window] | 444 | 221 | 214 | 63 | 151 | 0.209 | 29.4% | 0.208 | -0.007 |
| lmstudio/auto[pre-verbot] | 60 | 4 | 48 | 13 | 35 | 0.214 | 27.1% | 0.197 | -0.085 |
| lmstudio/qwen36 | 81 | 81 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 76 | 76 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 86 | 86 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 230 | 171 | 58 | 31 | 27 | 0.296 | 53.4% | 0.249 | -0.191 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 20 | 18 | 10 | 8 | 0.164 | 55.6% | 0.247 | +0.334 |
| manual/fable-5.1/unattested | 378 | 320 | 50 | 34 | 16 | 0.248 | 68.0% | 0.218 | -0.140 |
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
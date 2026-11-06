**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 061709Z NOV 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-11-06_1614.md · forecaster: manual/opus-5.5/unattested · 6 accepted / 4 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261106-34 | 33% | 2027-01-05 | economics/markets | The S&P 500 closes below 7,000.00 on at least one trading day between 2026-11-09 and 2026-12-31. Reference: 7,405.12 on the packet date. | True if FRED series SP500 records any daily close below 7000.00 dated from 2026-11-09 through 2026-12-31. Reference: 7405.12 on the packet date. |
| KKR-20261106-35 | 50% | 2027-01-05 | cyber | CISA adds CVE-2026-123158, the OpenSSH password-authentication bypass affecting musl-based Linux systems without PAM, to its Known Exploited Vulnerabilities catalog between 2026-11-06 and 2026-12-31. | True if the CISA KEV catalog carries CVE-2026-123158, the bypass fixed in OpenSSH 10.6p2, with a dateAdded value from 2026-11-06 through 2026-12-31. |
| KKR-20261106-36 | 9% | 2027-02-02 | cyber | CISA adds a vulnerability in D-Link DGS-3130 Series switches to its Known Exploited Vulnerabilities catalog between 2026-11-06 and 2027-01-29. | True if the CISA KEV catalog carries an entry with vendorProject D-Link naming DGS-3130 in its product or vulnerabilityName field, with a dateAdded value from 2026-11-06 through 2027-01-29. |
| KKR-20261106-37 | 27% | 2027-03-02 | political | Pete Hegseth leaves the post of US Secretary of Defense, also styled Secretary of War, by resignation, dismissal or removal between 2026-11-09 and 2027-02-26. | True if, between 2026-11-09 and 2027-02-26, Hegseth resigns, is fired or is removed from office, as announced by the White House or reported by both Reuters and AP. |
| KKR-20261106-38 | 45% | 2026-12-22 | political | At the Victorian state election held on 2026-11-28, the Liberal-National Coalition wins at least 45 of the 88 Legislative Assembly seats. | True if Victorian Electoral Commission declared results for the 2026-11-28 election show Liberal and National candidates winning a combined 45 or more of the 88 Legislative Assembly seats. |
| KKR-20261106-39 | 73% | 2026-11-25 | disaster | Delhi records an official daily AQI of 401 or higher, the Severe band, on at least one day between 2026-11-09 and 2026-11-22. | True if the CPCB 4 PM National AQI Bulletin lists Delhi at 401 or higher for any date from 2026-11-09 through 2026-11-22. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "US forces strike at least one target on Iranian soil, mainland or islands, between 2026-11-09 and 2026-12-31." → REJECTED: resolution offers alternative VENUES joined by 'or' (…a centcom statement, | or | reporting by both reuters and ap, confirms a …) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "The UN Human Rights Monitoring Mission in Ukraine (HRMMU) reports at least 300 civilians killed in Ukraine during the event window 2026-11-0" → REJECTED: event window opens 2026-11-01, before this row is sealed (2026-11-06, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "At its scheduled meeting concluding 2026-12-09, the FOMC raises the federal funds target range by at least 25 basis points, lifting the uppe" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "Between 2026-11-09 and 2027-01-08, a government of an EU member state or the UK publicly attributes the November 2026 hoax bomb threats agai" → REJECTED: resolution offers alternative VENUES joined by 'or' (…ntelligence agency, says russian state actors | or | proxies were behind the hoax threats, per reu…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

5415 issued all-time across 22 forecaster arms · 3693 open (1268 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/opus-5.5/unattested`:** 349 issued · 335 open · 14 resolved · 8 hits / 6 misses · **Brier 0.312** against its own base rate 57.1% (climatological 0.245) · **skill -0.275** · under 30 resolved, this is noise.

*96 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1788 | 1279 | 477 | 273 | 204 | 0.300 | 57.2% | 0.245 | -0.226 |
| control/trailing | 96 | 96 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 9 | 11 | 1 | 10 | 0.123 | 9.1% | 0.083 | -0.490 |
| lmstudio/auto[post-window] | 470 | 201 | 259 | 75 | 184 | 0.204 | 29.0% | 0.206 | +0.009 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 179 | 162 | 11 | 4 | 7 | 0.227 | 36.4% | 0.231 | +0.020 |
| lmstudio/qwen36-abliterated | 179 | 177 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
| lmstudio/qwen36-realist | 160 | 127 | 31 | 10 | 21 | 0.242 | 32.3% | 0.219 | -0.106 |
| lmstudio/realist | 249 | 128 | 119 | 66 | 53 | 0.317 | 55.5% | 0.247 | -0.285 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 14 | 24 | 14 | 10 | 0.164 | 58.3% | 0.243 | +0.325 |
| manual/fable-5.1/unattested | 494 | 379 | 107 | 61 | 46 | 0.211 | 57.0% | 0.245 | +0.140 |
| manual/fable-5/unattested | 258 | 147 | 102 | 65 | 37 | 0.203 | 63.7% | 0.231 | +0.121 |
| manual/opus-5 | 74 | 39 | 35 | 18 | 17 | 0.213 | 51.4% | 0.250 | +0.146 |
| manual/opus-5.5/unattested | 349 | 335 | 14 | 8 | 6 | 0.312 | 57.1% | 0.245 | -0.275 |
| manual/opus-5/unattested | 326 | 221 | 95 | 61 | 34 | 0.208 | 64.2% | 0.230 | +0.097 |
| manual/sonnet-5 | 45 | 3 | 41 | 22 | 19 | 0.250 | 53.7% | 0.249 | -0.007 |
| manual/sonnet-5.5/unattested | 222 | 207 | 15 | 10 | 5 | 0.122 | 66.7% | 0.222 | +0.451 |
| manual/sonnet-5/unattested | 342 | 141 | 196 | 98 | 98 | 0.245 | 50.0% | 0.250 | +0.019 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*
**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 141516Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-14_1513.md · forecaster: lmstudio/realist · 3 accepted / 7 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261014-04 | 20% | 2026-10-27 | cyber | Between 2026-10-19 and 2026-10-25, Iran issues a public statement via a state-aligned outlet claiming it has launched a cyberattack on a U.S. defense contractor, with no independent corroboration from a Western outlet. | At least one state-aligned Iranian outlet publishes a claim of a cyberattack on a U.S. defense contractor between 2026-10-19 and 2026-10-25, with no confirmation from a Western outlet. |
| KKR-20261014-05 | 40% | 2026-10-22 | economics/markets | On 2026-10-20, the 10-year U.S. Treasury yield exceeds 5.3% at the close of trading, as reported by FRED. | The 10-year U.S. Treasury yield exceeds 5.3% at the close of trading on 2026-10-20, as reported by FRED. |
| KKR-20261014-06 | 30% | 2026-10-29 | disaster | Between 2026-10-21 and 2026-10-27, a wildfire of at least 500 hectares burns in California, confirmed by both the GDACS Alerts and the California Department of Forestry and Fire Protection (CAL FIRE). | The GDACS Alerts feed and CAL FIRE both confirm a wildfire of at least 500 hectares in California between 2026-10-21 and 2026-10-27. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "On 2026-10-15, a drone strike targeting a Russian military installation in Kyiv is confirmed by at least two independently biased sources, i" → REJECTED: cited items name Australia, Saudi Arabia, United States; the claim is about Russian Federation, zone:russia_ukraine — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else; negated-observation clause — 'with no X reported' is a claim about the source record, not about the event. The war desk prints it to describe its own reports; it cannot be adjudicated as a property of the world; event window opens 2026-10-13, before this row is sealed (2026-10-14, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later; the resolution names only a venue or register (CISA, KEV) and no subject - the register is where to look, not what is claimed; name the subject inside it
- "Between 2026-10-16 and 2026-10-22, the S&P 500 closes below 7,700 on at least three separate trading days." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "Between 2026-10-17 and 2026-10-23, a cyberattack exploiting CVE-2026-104935 is confirmed by at least two independent sources, including one " → REJECTED: the resolution names only a venue or register (CISA, KEV) and no subject - the register is where to look, not what is claimed; name the subject inside it; the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-104935 dateAdded 2026-10-13, before the claimed window 2026-10-17..2026-10-23; dateAdded is single-valued and a fresh in-window value would require removal-and-relisting, which has no documented precedent (removals exist: CVE-2022-28958, removed 2023-12-01)
- "On 2026-10-18, a major earthquake of magnitude 6.5 or higher occurs in the Pacific Northwest, with a depth of less than 50 km, as recorded b" → REJECTED: cited items name Guinea, Panama, Papua New Guinea; the claim is about Idaho, Oregon, Washington — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else; single-day resolution window for an unscheduled event — the row requires this to occur on 2026-10-18 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "On 2026-10-22, a political scandal involving a U.S. senator is confirmed by two major U.S. news outlets, with the senator facing formal char" → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-10-22 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "Between 2026-10-23 and 2026-10-29, a major cyberattack on a financial institution in the EU results in a temporary suspension of online bank" → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "On 2026-10-24, a new U.S. executive order is issued restricting the export of AI-related technologies to Iran, as published in the Federal R" → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-10-24 exactly. Price a day, not a window: widen the window or state why the date is fixed

## III. LEDGER STANDING

4101 issued all-time across 21 forecaster arms · 2990 open (438 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/realist`:** 220 issued · 161 open · 58 resolved · 31 hits / 27 misses · **Brier 0.296** against its own base rate 53.4% (climatological 0.249) · **skill -0.191**.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1452 | 1156 | 264 | 161 | 103 | 0.313 | 61.0% | 0.238 | -0.317 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 11 | 9 | 1 | 8 | 0.146 | 11.1% | 0.099 | -0.474 |
| lmstudio/auto[post-window] | 422 | 199 | 214 | 63 | 151 | 0.209 | 29.4% | 0.208 | -0.007 |
| lmstudio/auto[pre-verbot] | 60 | 4 | 48 | 13 | 35 | 0.214 | 27.1% | 0.197 | -0.085 |
| lmstudio/qwen36 | 49 | 49 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 48 | 48 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 54 | 54 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 220 | 161 | 58 | 31 | 27 | 0.296 | 53.4% | 0.249 | -0.191 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 20 | 18 | 10 | 8 | 0.164 | 55.6% | 0.247 | +0.334 |
| manual/fable-5.1/unattested | 337 | 279 | 50 | 34 | 16 | 0.248 | 68.0% | 0.218 | -0.140 |
| manual/fable-5/unattested | 258 | 179 | 70 | 47 | 23 | 0.190 | 67.1% | 0.221 | +0.138 |
| manual/opus-5 | 74 | 44 | 30 | 14 | 16 | 0.210 | 46.7% | 0.249 | +0.156 |
| manual/opus-5.5/unattested | 168 | 163 | 5 | 3 | 2 | 0.440 | 60.0% | 0.240 | -0.835 |
| manual/opus-5/unattested | 326 | 265 | 51 | 34 | 17 | 0.182 | 66.7% | 0.222 | +0.182 |
| manual/sonnet-5 | 45 | 5 | 39 | 21 | 18 | 0.262 | 53.8% | 0.249 | -0.055 |
| manual/sonnet-5.5/unattested | 122 | 122 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 206 | 131 | 69 | 62 | 0.249 | 52.7% | 0.249 | +0.000 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*
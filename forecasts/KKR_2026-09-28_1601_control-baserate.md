**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 281601Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-28_1516.md · forecaster: control/baserate · 6 accepted / 4 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260928-21 | 32% | 2026-11-17 | cyber | The FBI, the US Department of Justice, or the US Treasury Department publicly attributes the September 2026 theft of roughly 387 million dollars in crypto assets from Bitget to North Korean state actors, in a publication dated between 2026-09-28 and 2026-11-13. | TRUE if a publication on fbi.gov, ic3.gov, justice.gov, or home.treasury.gov dated between 2026-09-28 and 2026-11-13 names Bitget and attributes the theft to North Korean, DPRK, Lazarus, or TraderTraitor actors. |
| KKR-20260928-22 | 64% | 2026-11-17 | military/conflict | The United States and Iran publicly announce an agreed bilateral ceasefire, memorandum of understanding, or framework agreement, confirmed by both governments, between 2026-09-29 and 2026-11-13. | TRUE if, between 2026-09-29 and 2026-11-13, the White House or State Department and the Iranian Foreign Ministry each publicly confirm a bilateral ceasefire, MoU, or framework agreement has been agreed, and Reuters and AP report both confirmations. |
| KKR-20260928-23 | 64% | 2026-12-22 | military/conflict | United States forces strike at least one target located in Tehran province, Iran, between 2026-11-04 and 2026-12-18, with the strike publicly confirmed by the US Department of Defense or CENTCOM. | TRUE if the US Department of Defense or CENTCOM publicly confirms a US strike on a target in Tehran province conducted between 2026-11-04 and 2026-12-18 inclusive, and Reuters and AP both report the strike. |
| KKR-20260928-24 | 39% | 2026-11-24 | political | Democrats win a majority of the US House of Representatives in the 2026-11-03 midterm election, with Associated Press race calls assigning Democratic candidates at least 218 seats as of 2026-11-24. | TRUE if, as of 2026-11-24, Associated Press race calls for the 2026-11-03 US House general elections assign at least 218 of 435 seats to Democratic candidates. |
| KKR-20260928-25 | 48% | 2026-11-04 | economics/markets | The official NYMEX WTI crude oil front-month futures settlement price on 2026-10-30 is above 100.00 dollars per barrel. Reference: 95.60 dollars per barrel on the packet date. | TRUE if the CME Group official settlement for the front-month NYMEX WTI crude oil futures contract on 2026-10-30, as also recorded in the EIA daily futures price series, is strictly greater than 100.00 dollars per barrel. |
| KKR-20260928-26 | 31% | 2026-10-06 | disaster | Hurricane Polo makes landfall on the Baja California Peninsula between 2026-09-28 and 2026-10-04 with National Hurricane Center operational products stating maximum sustained winds of at least 111 mph at landfall. | TRUE if an NHC Tropical Cyclone Update or Public Advisory issued between 2026-09-28 and 2026-10-04 reports the center of Polo crossing the Baja California Peninsula coast with maximum sustained winds of 111 mph or greater. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "At least one of the five men arrested near RAF Fairford on 2026-09-27 is charged with a criminal offence, with the charge publicly announced" → REJECTED: event window opens 2026-09-27, before this row is sealed (2026-09-28, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "The CISA Known Exploited Vulnerabilities catalog adds at least one Citrix NetScaler ADC or NetScaler Gateway CVE other than CVE-2026-88771 a" → REJECTED: the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-88772 dateAdded 2026-09-27, before the claimed window 2026-09-29..2026-12-31; dateAdded is single-valued and a fresh in-window value would require removal-and-relisting, which has no documented precedent (removals exist: CVE-2022-28958, removed 2023-12-01)
- "A Presidential proclamation, executive order, or federal agency rule imposing a mandatory prohibition, quota, or license requirement on expo" → REJECTED: cited items name Iran, Islamic Republic of; the claim is about United States — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else
- "The FOMC statement released on 2026-10-28 announces an increase in the federal funds target range above the 3.75 to 4.00 percent range held " → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim

## III. LEDGER STANDING

3014 issued all-time across 17 forecaster arms · 2472 open (232 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 1070 issued · 953 open · 85 resolved · 50 hits / 35 misses · **Brier 0.327** against its own base rate 58.8% (climatological 0.242) · **skill -0.352**.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1070 | 953 | 85 | 50 | 35 | 0.327 | 58.8% | 0.242 | -0.352 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 336 | 186 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 136 | 131 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 27 | 18 | 10 | 8 | 0.189 | 55.6% | 0.247 | +0.235 |
| manual/fable-5 | 38 | 27 | 11 | 6 | 5 | 0.101 | 54.5% | 0.248 | +0.591 |
| manual/fable-5.1/unattested | 216 | 199 | 9 | 6 | 3 | 0.176 | 66.7% | 0.222 | +0.209 |
| manual/fable-5/unattested | 258 | 237 | 12 | 11 | 1 | 0.214 | 91.7% | 0.076 | -1.797 |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5.5/unattested | 34 | 34 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 301 | 15 | 11 | 4 | 0.235 | 73.3% | 0.196 | -0.199 |
| manual/sonnet-5 | 45 | 9 | 35 | 18 | 17 | 0.247 | 51.4% | 0.250 | +0.009 |
| manual/sonnet-5/unattested | 335 | 271 | 59 | 31 | 28 | 0.238 | 52.5% | 0.249 | +0.047 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*
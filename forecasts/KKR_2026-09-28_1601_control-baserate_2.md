**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 281601Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-28_1516.md · forecaster: control/baserate · 6 accepted / 4 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260928-33 | 48% | 2027-01-05 | economics/markets | The 10-year Treasury constant-maturity yield for 2026-12-31 is above the packet-date level. Reference: 5.27 percent on the packet date. | FRED series DGS10 value for 2026-12-31 is strictly greater than 5.27. Reference: 5.27 percent on the packet date. |
| KKR-20260928-34 | 39% | 2026-12-03 | political | A Federal Register document modifying US tariffs on products of China is published between 2026-09-29 and 2026-11-30. | The Federal Register publishes an executive order, proclamation, or USTR notice dated 2026-09-29 through 2026-11-30 that changes duty rates on goods of Chinese origin. |
| KKR-20260928-35 | 64% | 2026-11-18 | military/conflict | US and Iranian officials hold direct talks, confirmed by both governments, between 2026-09-29 and 2026-11-15. | Reuters or AP reports that a direct US-Iran meeting occurred between 2026-09-29 and 2026-11-15, and both the US government and the Iranian government publicly acknowledge that meeting. |
| KKR-20260928-36 | 64% | 2026-12-03 | military/conflict | The Ethiopian federal government and Tigrayan forces announce a ceasefire or cessation of hostilities between 2026-09-29 and 2026-11-30. | Reuters and AP each report that the Ethiopian government and Tigrayan armed forces agreed or declared a ceasefire or cessation of hostilities dated within 2026-09-29 to 2026-11-30. |
| KKR-20260928-37 | 29% | 2026-10-14 | crime/security | At least one of the five men arrested near RAF Fairford is charged with a terrorism or explosives offence between 2026-09-28 and 2026-10-12. | The CPS or Counter Terrorism Policing announces, dated 2026-09-28 through 2026-10-12, a terrorism or explosives charge against at least one person arrested in the RAF Fairford investigation. |
| KKR-20260928-38 | 31% | 2026-10-08 | disaster | Hurricane Polo makes landfall on the Baja California peninsula at hurricane intensity between 2026-09-28 and 2026-10-06. | NHC public advisories or tropical cyclone updates for Polo state a landfall on the Baja California peninsula with maximum sustained winds of 64 knots or higher, dated within the window. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "CISA adds at least one Citrix vulnerability other than CVE-2026-88771 and CVE-2026-88772 to the KEV catalog between 2026-09-29 and 2026-12-3" → REJECTED: the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-88772 dateAdded 2026-09-27, before the claimed window 2026-09-29..2026-12-31; dateAdded is single-valued and a fresh in-window value would require removal-and-relisting, which has no documented precedent (removals exist: CVE-2022-28958, removed 2023-12-01)
- "The FBI publicly attributes the 387.5 million dollar Bitget theft to North Korean actors between 2026-09-29 and 2026-11-30." → REJECTED: resolution offers alternative VENUES joined by 'or' (…fbi press release | or | ic3 public…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "WTI crude spot prints at or above 110.00 dollars on at least one day between 2026-09-29 and 2026-11-30. Reference: 95.60 on the packet date." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "The US government formally restricts diesel or distillate fuel exports via a Federal Register document published between 2026-09-29 and 2026" → REJECTED: resolution offers alternative VENUES joined by 'or' (…al register publishes a presidential document | or | agency rule, dated 2026-09-29 through 2026-12…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

3026 issued all-time across 17 forecaster arms · 2484 open (232 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 1076 issued · 959 open · 85 resolved · 50 hits / 35 misses · **Brier 0.327** against its own base rate 58.8% (climatological 0.242) · **skill -0.352**.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1076 | 959 | 85 | 50 | 35 | 0.327 | 58.8% | 0.242 | -0.352 |
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
| manual/opus-5.5/unattested | 40 | 40 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 301 | 15 | 11 | 4 | 0.235 | 73.3% | 0.196 | -0.199 |
| manual/sonnet-5 | 45 | 9 | 35 | 18 | 17 | 0.247 | 51.4% | 0.250 | +0.009 |
| manual/sonnet-5/unattested | 335 | 271 | 59 | 31 | 28 | 0.238 | 52.5% | 0.249 | +0.047 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*
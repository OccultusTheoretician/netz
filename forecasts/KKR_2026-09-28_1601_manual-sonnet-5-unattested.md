**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 281601Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-28_1516.md · forecaster: manual/sonnet-5/unattested · 7 accepted / 3 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260928-39 | 80% | 2026-10-14 | crime/security | Between 2026-09-28 and 2026-10-11, at least one of the five men arrested on 2026-09-27 near RAF Fairford on suspicion of Explosives Act offences and preparing a terrorist act is formally charged with a criminal offence arising from those arrests. | Counter Terrorism Policing, the CPS, or a court record confirms a charge against at least one of the five men, dated between 2026-09-28 and 2026-10-11, arising from the 2026-09-27 RAF Fairford arrests. |
| KKR-20260928-40 | 17% | 2026-10-22 | cyber | Between 2026-09-29 and 2026-10-20, the CISA Known Exploited Vulnerabilities catalog adds at least one further Citrix NetScaler vulnerability, beyond the two Citrix NetScaler entries added on 2026-09-27. | CISA KEV JSON contains an entry with vendorProject Citrix, product referencing NetScaler, dateAdded between 2026-09-29 and 2026-10-20 inclusive, and a cveID different from the two Citrix entries dated 2026-09-27. |
| KKR-20260928-41 | 30% | 2026-11-04 | economics/markets | Between 2026-10-01 and 2026-10-30, the FRED series DGS10 (10-year Treasury constant maturity yield) records a value at or above 5.50 percent on at least one business day. Reference: 5.27 percent per the packet market snapshot; FRED DGS10 was 5.18 percent on 2026-09-24. | At least one FRED DGS10 observation dated between 2026-10-01 and 2026-10-30 is 5.50 or higher. Reference: 5.27 percent per the packet market snapshot on 2026-09-28. |
| KKR-20260928-42 | 22% | 2026-11-06 | political | Between 2026-09-29 and 2026-10-30, the US President or a federal agency signs or issues an order, proclamation, or rule that prohibits, restricts, or caps exports of diesel fuel from the United States. Voluntary industry export restraint does not count. | whitehouse.gov, the Federal Register, or a BIS or Commerce notice shows a mandatory diesel export ban, licensing requirement, or quota signed or issued between 2026-09-29 and 2026-10-30; voluntary export restraint does not count. |
| KKR-20260928-43 | 40% | 2026-11-04 | political | Between 2026-10-01 and 2026-10-31, OFAC designates at least one entity located outside Iran for supporting Iranian airlines or the Iranian aviation sector. | A US Treasury press release or OFAC Recent Actions SDN list update dated between 2026-10-01 and 2026-10-31 designates an entity located outside Iran and cites support to Iranian airlines or the Iranian aviation sector. |
| KKR-20260928-44 | 22% | 2026-12-08 | military/conflict | Between 2026-11-04 and 2026-12-04, US forces conduct at least one acknowledged air or missile strike on a land target or island inside Iran. | A US government statement, or Reuters and AP reporting, confirms a US air or missile strike on a land target or island inside Iranian territory carried out between 2026-11-04 and 2026-12-04. |
| KKR-20260928-45 | 90% | 2026-10-20 | political | Between 2026-09-29 and 2026-10-16, the Australian Greens party room elects a new federal parliamentary leader to replace Larissa Waters, who announced on 2026-09-28 that she is stepping down. | The Greens or two of ABC, Guardian Australia, and AAP report a party room vote choosing a new federal leader between 2026-09-29 and 2026-10-16; acting or interim appointments do not count. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-09-29 and 2026-10-20, the FBI publicly attributes the roughly 387.5 million dollar theft from the Bitget exchange on 2026-09-24" → REJECTED: resolution offers alternative VENUES joined by 'or' (…an fbi public service announcement | or | press release on ic3…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "On 2026-09-29 the Reserve Bank of Australia board announces an increase in the cash rate target. Reference: cash rate target of 4.35 percent" → REJECTED: the resolution names a different subject than the statement — the claim is about Australia, Bank, Reference, Reserve and the resolution settles on RBA. A row whose resolution checks a different fact can be scored correct while being wrong
- "Between 2026-09-28 and 2026-10-05, Hurricane Polo makes landfall on mainland Mexico after crossing the Baja California peninsula, with Natio" → REJECTED: resolution offers alternative VENUES joined by 'or' (…the first nhc advisory | or | bulletin reporting that polo has made landfal…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

3033 issued all-time across 17 forecaster arms · 2491 open (232 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/sonnet-5/unattested`:** 342 issued · 278 open · 59 resolved · 31 hits / 28 misses · **Brier 0.238** against its own base rate 52.5% (climatological 0.249) · **skill +0.047**.

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
| manual/sonnet-5/unattested | 342 | 278 | 59 | 31 | 28 | 0.238 | 52.5% | 0.249 | +0.047 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*
**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 251947Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-25_1520.md · forecaster: manual/sonnet-5/unattested · 6 accepted / 4 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260925-41 | 20% | 2026-11-10 | cyber | OFAC will add a wallet address or entity to its Specially Designated Nationals list with designation remarks naming the Bitget hack (reported theft of approximately 351.6 million dollars, suspected North Korea attribution), between 2026-10-02 and 2026-11-06. | OFAC's SDN list (sanctionssearch.ofac.treas.gov) or a Federal Register notice contains an entry whose designation remarks name the Bitget hack, with a listing date between 2026-10-02 and 2026-11-06 inclusive. |
| KKR-20260925-42 | 62% | 2026-10-20 | military_conflict | At least two independent outlets will report a specific clash, casualty event, or territorial change involving Ethiopian federal forces and Tigrayan (TPLF-aligned) forces occurring between 2026-10-02 and 2026-10-16. | Two independent outlets (e.g. Reuters, AP, BBC, Al Jazeera, Addis Standard) report a specific clash, casualty event, or territorial change involving Ethiopian federal and Tigrayan forces, dated within 2026-10-02 to 2026-10-16. |
| KKR-20260925-43 | 15% | 2026-11-24 | military_conflict | Pakistan and/or Turkiye will formally announce, through an official government statement, military participation in Saudi-led coalition operations against Houthi forces in Yemen, between 2026-10-02 and 2026-11-20. | An official Pakistani or Turkish government statement, or a joint Saudi-coalition communique, reported by at least two independent outlets, confirms Pakistani or Turkish military participation in coalition operations against the Houthis, dated between 2026-10-02 and 2026-11-20. |
| KKR-20260925-44 | 75% | 2026-10-06 | political | Pakistani authorities will arrest or detain at least one PTI member or supporter in connection with the Islamabad march, between 2026-09-26 and 2026-10-04. | Two independent outlets (e.g. Dawn, Reuters, Al Jazeera, AP) report the arrest or detention of at least one PTI member, supporter, or organizer tied to the Islamabad march, with an arrest date between 2026-09-26 and 2026-10-04. |
| KKR-20260925-45 | 32% | 2026-11-16 | economic | The 10-year US Treasury yield (reference: 5.21 percent on 2026-09-25, per the Treasury daily par yield curve) will reach 5.50 percent or higher on at least one business day between 2026-10-02 and 2026-11-13. | The US Treasury Daily Par Yield Curve Rates (home.treasury.gov) show a 10-year rate of 5.50 percent or higher on at least one business day within 2026-10-02 to 2026-11-13 inclusive. |
| KKR-20260925-46 | 50% | 2026-11-09 | political | USTR will publish a press release, fact sheet, or Federal Register notice describing specific terms of a US-China trade agreement or framework, following USTR Greer's 2026-09-25 statement that details were coming, between 2026-10-02 and 2026-11-06. | USTR (ustr.gov) or the Federal Register carries a press release, fact sheet, or notice describing specific US-China trade terms, dated between 2026-10-02 and 2026-11-06. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "CISA will add at least one new CVE to the Known Exploited Vulnerabilities catalog, other than CVE-2026-5430 (WSO2) or CVE-2026-71362 (Adobe " → REJECTED: the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-5430 dateAdded 2026-09-24, before the claimed window 2026-10-02..2026-10-09; dateAdded is single-valued and a fresh in-window value would require removal-and-relisting, which has no documented precedent (removals exist: CVE-2022-28958, removed 2023-12-01)
- "A named Atlantic or Eastern Pacific tropical cyclone, other than Hurricane Nolo or Hurricane Polo (both active as of 2026-09-25), will reach" → REJECTED: resolution offers alternative VENUES joined by 'or' (… national hurricane center's advisory archive | or | best-track database lists a tropical cyclone,…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "The federal case referenced in item 9 (a Virginia tech firm executive and a Russian national charged with concealing the firm's Russian ties" → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "A lawsuit, DOJ Office of Inspector General investigation announcement, or congressional oversight letter concerning the theft of FBI special" → REJECTED: resolution offers alternative VENUES joined by 'or' (…docket, the doj oig's published reports page, | or | a congressional committee's official site sho…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

2870 issued all-time across 17 forecaster arms · 2328 open (189 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/sonnet-5/unattested`:** 320 issued · 256 open · 59 resolved · 31 hits / 28 misses · **Brier 0.238** against its own base rate 52.5% (climatological 0.249) · **skill +0.047**.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1007 | 890 | 85 | 50 | 35 | 0.327 | 58.8% | 0.242 | -0.352 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 329 | 179 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 119 | 114 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 27 | 18 | 10 | 8 | 0.189 | 55.6% | 0.247 | +0.235 |
| manual/fable-5 | 38 | 27 | 11 | 6 | 5 | 0.101 | 54.5% | 0.248 | +0.591 |
| manual/fable-5.1/unattested | 190 | 173 | 9 | 6 | 3 | 0.176 | 66.7% | 0.222 | +0.209 |
| manual/fable-5/unattested | 258 | 237 | 12 | 11 | 1 | 0.214 | 91.7% | 0.076 | -1.797 |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5.5/unattested | 18 | 18 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 301 | 15 | 11 | 4 | 0.235 | 73.3% | 0.196 | -0.199 |
| manual/sonnet-5 | 45 | 9 | 35 | 18 | 17 | 0.247 | 51.4% | 0.250 | +0.009 |
| manual/sonnet-5/unattested | 320 | 256 | 59 | 31 | 28 | 0.238 | 52.5% | 0.249 | +0.047 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*
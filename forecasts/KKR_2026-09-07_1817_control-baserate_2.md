**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 071817Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-07_1518.md · forecaster: control/baserate · 7 accepted / 3 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260907-48 | 21% | 2026-10-05 | economics/markets | NYMEX WTI front-month crude settles at or above 100.00 USD per barrel on 2026-10-02. Reference: 91.48 on the packet date 2026-09-07. | CME Group official settlement price of the front-month NYMEX WTI (CL) contract for trade date 2026-10-02 is at or above 100.00 USD. Reference: 91.48 on the packet date 2026-09-07. Any settlement below 100.00 resolves false. |
| KKR-20260907-49 | 21% | 2026-11-04 | economics/markets | The US 10-year Treasury constant maturity yield closes at or above 5.00 percent on at least one business day between 2026-09-08 and 2026-10-30. Reference: 4.78 percent on the packet date 2026-09-07. | FRED series DGS10 (Treasury 10-year constant maturity) shows a daily value of 5.00 or higher for at least one date from 2026-09-08 through 2026-10-30 inclusive. Reference: 4.78 on 2026-09-07. No such value resolves false. |
| KKR-20260907-50 | 30% | 2026-09-29 | cyber | The CISA KEV catalog adds at least one N-able N-central vulnerability (CVE-2026-86218, CVE-2026-86207, or CVE-2026-86206) with a dateAdded between 2026-09-08 and 2026-09-25. | The CISA Known Exploited Vulnerabilities JSON feed lists CVE-2026-86218, CVE-2026-86207, or CVE-2026-86206 with a dateAdded value from 2026-09-08 through 2026-09-25 inclusive. No entry, or entries dated outside that range only, resolves false. |
| KKR-20260907-51 | 35% | 2027-01-15 | political | Ulrich Siegmund (AfD) is elected Ministerpraesident of Saxony-Anhalt by the Landtag in a ballot held between 2026-09-08 and 2027-01-13. | The Landtag of Saxony-Anhalt official plenary record or press release shows Ulrich Siegmund elected Ministerpraesident in any ballot round dated 2026-09-08 through 2027-01-13. Election of anyone else, or no completed election in that window, resolves false. |
| KKR-20260907-52 | 49% | 2026-10-02 | military/conflict | The Israeli military conducts at least one airstrike inside Beirut municipality or its southern suburbs (Dahiyeh) between 2026-09-08 and 2026-09-30. | An IDF statement claims a strike inside Beirut municipality or Dahiyeh (Haret Hreik, Burj al-Barajneh, Ghobeiry, Chiyah, Laylaki) and the Lebanese National News Agency reports the same strike, both dated 2026-09-08 to 2026-09-30. Strikes elsewhere do not count. |
| KKR-20260907-53 | 49% | 2026-11-04 | military/conflict | Official Russian and Ukrainian government delegations hold a direct in-person negotiating session, bilateral or with third-party mediation, between 2026-09-08 and 2026-10-30. | Both the Kremlin or Russian MFA and the Ukrainian Presidential Office or MFA confirm the same in-person delegation session held 2026-09-08 through 2026-10-30. Video calls, prisoner-exchange contacts, and meetings with US officials only do not count. |
| KKR-20260907-54 | 35% | 2026-10-06 | political | The Iraqi government or the US Department of Defense announces, between 2026-09-08 and 2026-10-02, that US military forces will remain stationed at bases in Iraq, including the Kurdistan Region, beyond 2026-09-30. | An official statement from the Iraqi PM office, Iraqi Armed Forces spokesperson, CENTCOM, CJTF-OIR, or US DoD, dated 2026-09-08 to 2026-10-02, announces US forces remaining at Iraqi bases past 2026-09-30. Embassy security and security-cooperation staff excluded. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The Japanese Ministry of Finance reports non-zero yen-buying intervention for its monthly reporting period covering approximately 2026-08-27" → REJECTED: measurable claim without a numeric threshold — a row about a quantity must state the number next to its comparator; identifier digits (H.15, S&P 500) do not count; event window opens 2026-08-27, before this row is sealed (2026-09-07, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later; the resolution names a different subject than the statement — the claim is about Finance, Japanese, Ministry and the resolution settles on Exchange, Foreign, Intervention, MOF. A row whose resolution checks a different fact can be scored correct while being wrong
- "The Paris assize court convicts Loik Le Priol of assassinat (premeditated murder) of Federico Martin Aramburu, with the verdict delivered be" → REJECTED: measurable claim without a numeric threshold — a row about a quantity must state the number next to its comparator; identifier digits (H.15, S&P 500) do not count
- "The NTSB publishes a preliminary report for the 2026-09-06 Amazon cargo aircraft accident at Miami International Airport between 2026-09-08 " → REJECTED: resolution offers alternative VENUES joined by 'or' (…ntsb investigation page | or | carol…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

1664 issued all-time across 16 forecaster arms · 1399 open (90 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 498 issued · 470 open · 28 resolved · 14 hits / 14 misses · **Brier 0.297** against its own base rate 50.0% (climatological 0.250) · **skill -0.187** · under 30 resolved, this is noise.

*16 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 498 | 470 | 28 | 14 | 14 | 0.297 | 50.0% | 0.250 | -0.187 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 227 | 139 | 83 | 15 | 68 | 0.183 | 18.1% | 0.148 | -0.234 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 25 | 25 | 0 | — | — | not computed | — | — | — |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 32 | 6 | 4 | 2 | 0.070 | 66.7% | 0.222 | +0.687 |
| manual/fable-5.1/unattested | 45 | 45 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 180 | 178 | 2 | 2 | 0 | 0.225 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 199 | 193 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 20 | 25 | 14 | 11 | 0.231 | 56.0% | 0.246 | +0.064 |
| manual/sonnet-5/unattested | 187 | 166 | 21 | 10 | 11 | 0.214 | 47.6% | 0.249 | +0.141 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*
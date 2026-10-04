**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 041918Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-04_1517.md · forecaster: manual/sonnet-5.5/unattested · 8 accepted / 2 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261004-52 | 55% | 2026-10-21 | military/conflict | Between 2026-10-05 and 2026-10-18, at least one bridge within the city limits of Kyiv is struck by a Russian drone or missile, following the Kyiv bridge strikes reported on 2026-10-04. | Ukrainian authorities (Kyiv city military administration, mayor, or Infrastructure Ministry) report a Russian drone or missile strike on a Kyiv bridge dated between 2026-10-05 and 2026-10-18, carried by Reuters or AP. |
| KKR-20261004-53 | 90% | 2026-10-12 | political | In the Brazilian presidential election first round held on 2026-10-04, no candidate receives more than 50 percent of valid votes, so a runoff between the top two candidates is scheduled for 2026-10-25. | The Brazilian Superior Electoral Court (TSE) results portal for the first round held on 2026-10-04 shows no presidential candidate above 50 percent of valid votes and a second round dated 2026-10-25. |
| KKR-20261004-54 | 6% | 2026-12-03 | political | Between 2026-10-05 and 2026-11-30, the Spanish prime minister dissolves the Cortes Generales and calls a snap general election by Royal Decree. | The Boletin Oficial del Estado publishes a Real Decreto dissolving the Congress of Deputies and the Senate and convening general elections, dated between 2026-10-05 and 2026-11-30. |
| KKR-20261004-55 | 60% | 2026-11-10 | crime/security | Between 2026-10-05 and 2026-11-06, Japanese prosecutors formally indict, on a murder charge, the US Marine arrested in Okinawa on suspicion of killing a woman, as reported on 2026-10-04. | Japanese prosecutors file a murder indictment against the arrested US Marine on a date between 2026-10-05 and 2026-11-06, reported by at least two of Kyodo, NHK, Reuters, or AP. |
| KKR-20261004-56 | 25% | 2026-11-17 | economics/markets | Between 2026-10-05 and 2026-11-13, the US 10-year Treasury constant maturity yield closes at or above 5.60 percent on at least one business day. Reference: 5.28 percent on the packet date 2026-10-04. | FRED series DGS10 shows a value of 5.60 or higher for at least one date between 2026-10-05 and 2026-11-13. Reference: 5.28 percent on the packet date. |
| KKR-20261004-57 | 30% | 2026-11-20 | economics/markets | Between 2026-10-05 and 2026-11-13, the WTI crude oil spot price is at or above 100.00 USD per barrel on at least one trading day. Reference: 91.11 USD on the packet date 2026-10-04, the prior-session close. | FRED series DCOILWTICO shows a value of 100.00 or higher for at least one date between 2026-10-05 and 2026-11-13. Reference: 91.11 USD on the packet date. |
| KKR-20261004-58 | 10% | 2026-11-02 | economics/markets | At the FOMC meeting held 2026-10-27 and 2026-10-28, the committee raises the federal funds target range above the range in effect on the packet date 2026-10-04. | The Federal Reserve statement released on 2026-10-28 sets a federal funds target range above the range in effect on 2026-10-04, as shown by FRED series DFEDTARU. Reference: range in effect on the packet date. |
| KKR-20261004-59 | 58% | 2026-11-10 | disaster | Between 2026-10-05 and 2026-11-06, the NTSB publishes a preliminary report on the air ambulance that went missing off the Massachusetts coast with 6 people aboard, as reported on 2026-10-03. | An NTSB preliminary report for the Massachusetts air ambulance accident appears on ntsb.gov or in the NTSB CAROL database with a publication date between 2026-10-05 and 2026-11-06. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-10-05 and 2026-11-08, the Iranian government announces that the closure of the Strait of Hormuz is lifted and commercial shippi" → REJECTED: measurable claim without a numeric threshold — a row about a quantity must state the number next to its comparator; identifier digits (H.15, S&P 500) do not count
- "Between 2026-10-05 and 2026-11-01, US federal prosecutors announce criminal charges, or a US court unseals an indictment or complaint, again" → REJECTED: resolution offers alternative VENUES joined by 'or' (…a us department of justice press release | or | a federal court docket entry dated…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

3381 issued all-time across 18 forecaster arms · 2839 open (502 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/sonnet-5.5/unattested`:** 46 issued · 46 open · nothing resolved yet — this arm earns a score at its first resolution.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1210 | 1093 | 85 | 50 | 35 | 0.327 | 58.8% | 0.242 | -0.352 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 376 | 226 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 175 | 170 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 27 | 18 | 10 | 8 | 0.189 | 55.6% | 0.247 | +0.235 |
| manual/fable-5 | 38 | 27 | 11 | 6 | 5 | 0.101 | 54.5% | 0.248 | +0.591 |
| manual/fable-5.1/unattested | 258 | 241 | 9 | 6 | 3 | 0.176 | 66.7% | 0.222 | +0.209 |
| manual/fable-5/unattested | 258 | 237 | 12 | 11 | 1 | 0.214 | 91.7% | 0.076 | -1.797 |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5.5/unattested | 87 | 87 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 301 | 15 | 11 | 4 | 0.235 | 73.3% | 0.196 | -0.199 |
| manual/sonnet-5 | 45 | 9 | 35 | 18 | 17 | 0.247 | 51.4% | 0.250 | +0.009 |
| manual/sonnet-5.5/unattested | 46 | 46 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 278 | 59 | 31 | 28 | 0.238 | 52.5% | 0.249 | +0.047 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*
**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 291712Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-29_1517.md · forecaster: control/baserate · 8 accepted / 2 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260929-36 | 29% | 2026-10-06 | crime/security | Tennessee carries out the execution of Christa Gail Pike on her scheduled execution date, 2026-09-30. | True if the Tennessee Department of Correction or AP reports Christa Gail Pike was executed on 2026-09-30, Central Time. False if a stay, reprieve, commutation or halted procedure prevents execution that day. |
| KKR-20260929-37 | 48% | 2026-12-02 | economics/markets | The US 10-year Treasury constant-maturity yield is at or above 5.50 percent on at least one daily reading between 2026-10-01 and 2026-11-30. Reference: 5.26 percent at seal on the packet date, 2026-09-29. | True if FRED series DGS10 shows a daily value of 5.50 or higher for any date from 2026-10-01 through 2026-11-30. Reference: 5.26 percent on 2026-09-29 per the packet market snapshot. |
| KKR-20260929-38 | 48% | 2027-01-05 | economics/markets | Oura Inc., which postponed its IPO on 2026-09-29, prices the offering and its common stock begins trading on a US exchange (planned Nasdaq ticker OURA) between 2026-09-30 and 2026-12-31. | True if Oura common stock begins regular trading on a US national exchange between 2026-09-30 and 2026-12-31, evidenced by a final 424B4 prospectus on SEC EDGAR and exchange listing records. |
| KKR-20260929-39 | 32% | 2027-01-05 | cyber | CISA adds at least one Apple vulnerability to the Known Exploited Vulnerabilities catalog with a dateAdded between 2026-09-30 and 2026-12-31. | True if the CISA KEV JSON feed contains at least one entry with vendorProject Apple and a dateAdded from 2026-09-30 through 2026-12-31 inclusive. |
| KKR-20260929-40 | 39% | 2026-12-15 | political | Democrat James Talarico defeats Republican Ken Paxton in the scheduled 2026-11-03 US Senate general election in Texas. | True if the AP calls the 2026-11-03 Texas US Senate race for James Talarico, or the certified Texas state canvass shows him with the most votes. False if Ken Paxton or another candidate prevails. |
| KKR-20260929-41 | 39% | 2027-01-05 | political | Between 2026-09-30 and 2026-12-31, the US terminates or fully suspends the Section 338 import ban on Canadian alcoholic beverages that took effect on 2026-09-29. | True if the Federal Register publishes a presidential proclamation or executive order, dated between 2026-09-30 and 2026-12-31, that terminates or fully suspends the Section 338 exclusion of Canadian alcoholic beverages. |
| KKR-20260929-42 | 64% | 2026-11-06 | military/conflict | US forces strike at least one target located on Iranian land territory, including ports and Iranian-held islands, between 2026-09-30 and 2026-11-03, before the US midterm elections. | True if CENTCOM or the Pentagon confirms, or AP and Reuters both report, a US strike on a target on Iranian land territory, ports or Iranian-held islands occurring between 2026-09-30 and 2026-11-03. |
| KKR-20260929-43 | 29% | 2027-01-05 | crime/security | At least one of the five men arrested near RAF Fairford on 2026-09-27 is charged with a criminal offence arising from that investigation between 2026-09-30 and 2026-12-31. | True if Counter Terrorism Policing, the CPS or a UK court listing states that any of the five men arrested near RAF Fairford on 2026-09-27 was charged between 2026-09-30 and 2026-12-31. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The FOMC raises the federal funds target range by at least 25 basis points at its scheduled meeting concluding 2026-10-28, lifting the upper" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "An eastern North Pacific tropical cyclone other than Polo makes landfall in Mexico, mainland or Baja California, at hurricane strength betwe" → REJECTED: resolution offers alternative VENUES joined by 'or' (…nhc public advisory | or | tropical cyclone…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

3083 issued all-time across 17 forecaster arms · 2541 open (260 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 1099 issued · 982 open · 85 resolved · 50 hits / 35 misses · **Brier 0.327** against its own base rate 58.8% (climatological 0.242) · **skill -0.352**.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1099 | 982 | 85 | 50 | 35 | 0.327 | 58.8% | 0.242 | -0.352 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 340 | 190 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 143 | 138 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 27 | 18 | 10 | 8 | 0.189 | 55.6% | 0.247 | +0.235 |
| manual/fable-5 | 38 | 27 | 11 | 6 | 5 | 0.101 | 54.5% | 0.248 | +0.591 |
| manual/fable-5.1/unattested | 224 | 207 | 9 | 6 | 3 | 0.176 | 66.7% | 0.222 | +0.209 |
| manual/fable-5/unattested | 258 | 237 | 12 | 11 | 1 | 0.214 | 91.7% | 0.076 | -1.797 |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5.5/unattested | 48 | 48 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 301 | 15 | 11 | 4 | 0.235 | 73.3% | 0.196 | -0.199 |
| manual/sonnet-5 | 45 | 9 | 35 | 18 | 17 | 0.247 | 51.4% | 0.250 | +0.009 |
| manual/sonnet-5/unattested | 342 | 278 | 59 | 31 | 28 | 0.238 | 52.5% | 0.249 | +0.047 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*
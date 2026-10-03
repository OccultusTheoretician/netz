**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 032113Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-03_1517.md · forecaster: manual/fable-5.1/unattested · 7 accepted / 3 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261003-13 | 95% | 2026-10-12 | political | No candidate exceeds 50 percent of valid votes in the first round of the Brazilian presidential election on 2026-10-04, sending the race to the scheduled runoff on 2026-10-25. | True if TSE official first-round totals for 2026-10-04 show every presidential candidate at or below 50 percent of valid votes. |
| KKR-20261003-14 | 43% | 2026-10-28 | political | Luiz Inacio Lula da Silva wins the 2026 Brazilian presidential election, either outright in the first round on 2026-10-04 or in the runoff on 2026-10-25. | True if TSE official results show Lula with the winning majority of valid votes in the 2026-10-04 first round or in the 2026-10-25 runoff. |
| KKR-20261003-15 | 25% | 2026-10-26 | economics/markets | ICE Brent crude futures for December 2026 delivery settle at or below 95.00 dollars per barrel on 2026-10-23. Reference: 102.25 on the packet date. | True if the ICE settlement price of the December 2026 Brent contract on 2026-10-23 is 95.00 dollars or lower. Reference: 102.25 on the packet date. |
| KKR-20261003-16 | 5% | 2026-11-09 | cyber | CISA adds the GitLab AI Gateway vulnerability CVE-2026-90970 to its Known Exploited Vulnerabilities catalog between 2026-10-04 and 2026-11-06. | True if the CISA KEV catalog lists CVE-2026-90970 with a date-added value between 2026-10-04 and 2026-11-06. |
| KKR-20261003-17 | 18% | 2026-11-09 | disaster | At least one Atlantic basin tropical cyclone reaches hurricane strength between 2026-10-05 and 2026-11-06. | True if National Hurricane Center advisories or best-track data show any Atlantic basin system with sustained winds of 64 knots or more on a date between 2026-10-05 and 2026-11-06. |
| KKR-20261003-18 | 40% | 2026-10-20 | military/conflict | A Russian strike hits a Kyiv bridge over the Dnipro other than the Pivdennyi (Southern) and Pivnichnyi (Northern) bridges between 2026-10-04 and 2026-10-17. | True if at least two of BBC, Reuters, AP and Kyiv Independent report a Russian drone or missile strike damaging a third Kyiv Dnipro bridge on a date between 2026-10-04 and 2026-10-17. |
| KKR-20261003-19 | 12% | 2026-11-16 | crime/security | At least one person is criminally charged in connection with the September 2026 security incident at RAF Fairford between 2026-10-05 and 2026-11-13. | True if Counter Terrorism Policing or the Crown Prosecution Service announces a charge tied to the RAF Fairford incident dated between 2026-10-05 and 2026-11-13, as reported by BBC or the Guardian. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "A royal decree dissolving the Cortes Generales and calling an early Spanish general election is published in the Boletin Oficial del Estado " → REJECTED: the resolution names a different subject than the statement — the claim is about Boletin, Cortes, Estado, Generales and the resolution settles on BOE, Congreso, Senado. A row whose resolution checks a different fact can be scored correct while being wrong
- "Likud, Shas, United Torah Judaism, Religious Zionism-Zehut, Otzma Yehudit and Amcha Yisrael (Ofer Winter) win a combined 61 or more of the 1" → REJECTED: the resolution names a different subject than the statement — the claim is about Amcha, Israeli, Judaism, Knesset and the resolution settles on Central, Committee, Elections. A row whose resolution checks a different fact can be scored correct while being wrong
- "The FOMC leaves the federal funds target range unchanged at 3.75 to 4.00 percent at its scheduled decision on 2026-10-28. Reference: 3.75 to" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim

## III. LEDGER STANDING

3289 issued all-time across 18 forecaster arms · 2747 open (497 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/fable-5.1/unattested`:** 250 issued · 233 open · 9 resolved · 6 hits / 3 misses · **Brier 0.176** against its own base rate 66.7% (climatological 0.222) · **skill +0.209** · under 30 resolved, this is noise.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1173 | 1056 | 85 | 50 | 35 | 0.327 | 58.8% | 0.242 | -0.352 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 368 | 218 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 166 | 161 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 27 | 18 | 10 | 8 | 0.189 | 55.6% | 0.247 | +0.235 |
| manual/fable-5 | 38 | 27 | 11 | 6 | 5 | 0.101 | 54.5% | 0.248 | +0.591 |
| manual/fable-5.1/unattested | 250 | 233 | 9 | 6 | 3 | 0.176 | 66.7% | 0.222 | +0.209 |
| manual/fable-5/unattested | 258 | 237 | 12 | 11 | 1 | 0.214 | 91.7% | 0.076 | -1.797 |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5.5/unattested | 71 | 71 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 301 | 15 | 11 | 4 | 0.235 | 73.3% | 0.196 | -0.199 |
| manual/sonnet-5 | 45 | 9 | 35 | 18 | 17 | 0.247 | 51.4% | 0.250 | +0.009 |
| manual/sonnet-5.5/unattested | 32 | 32 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 278 | 59 | 31 | 28 | 0.238 | 52.5% | 0.249 | +0.047 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*
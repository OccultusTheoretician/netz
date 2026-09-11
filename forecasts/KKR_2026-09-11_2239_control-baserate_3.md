**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 112239Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-11_1518.md · forecaster: control/baserate · 8 accepted / 2 rejected by validation gate · 6 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260911-50 | 56% | 2026-10-14 | military/conflict | Russian strikes damage fuel or electric power infrastructure in Kyiv city or Kyiv oblast on at least three separate calendar days between 2026-09-12 and 2026-10-11. | At least two of Reuters, AP, AFP, or the Guardian, citing Ukrainian officials, report such infrastructure damage in Kyiv city or oblast on three or more distinct dates between 2026-09-12 and 2026-10-11; otherwise MISS. |
| KKR-20260911-51 | 26% | 2026-10-20 | economics/markets | WTI crude front-month futures record at least one daily settlement price at or above 110.00 USD per barrel on NYMEX between 2026-09-14 and 2026-10-16. Reference: 99.63 USD on the packet date. | CME Group official daily settlement data for front-month WTI crude shows any settlement at or above 110.00 USD between 2026-09-14 and 2026-10-16 inclusive; otherwise MISS. |
| KKR-20260911-52 | 26% | 2026-11-17 | economics/markets | The 10-year US Treasury constant maturity yield prints at or above 5.25 percent on at least one business day between 2026-09-14 and 2026-11-13. Reference: 4.94 percent on the packet date. | FRED series DGS10 shows any daily value at or above 5.25 between 2026-09-14 and 2026-11-13 inclusive; otherwise MISS. |
| KKR-20260911-53 | 26% | 2027-03-09 | economics/markets | Anthropic shares begin public trading on the NYSE or Nasdaq between 2026-09-14 and 2027-03-05. | Official records of the listing exchange show a first day of public trading for Anthropic common stock between 2026-09-14 and 2027-03-05 inclusive; otherwise MISS. |
| KKR-20260911-54 | 28% | 2026-10-13 | cyber | The CISA Known Exploited Vulnerabilities catalog adds at least one CVE whose vendor or product field contains PaperCut with a dateAdded value between 2026-09-12 and 2026-10-09. | The public CISA KEV JSON feed contains an entry matching PaperCut in vendorProject or product with dateAdded between 2026-09-12 and 2026-10-09 inclusive; otherwise MISS. |
| KKR-20260911-55 | 28% | 2026-11-03 | cyber | The CISA Known Exploited Vulnerabilities catalog adds at least one CVE whose vendor or product field contains GitLab with a dateAdded value between 2026-09-12 and 2026-10-30. | The public CISA KEV JSON feed contains an entry matching GitLab in vendorProject or product with dateAdded between 2026-09-12 and 2026-10-30 inclusive; otherwise MISS. |
| KKR-20260911-56 | 35% | 2027-02-02 | political | Zack Polanski is elected Member of Parliament for Holborn and St Pancras at a byelection held between 2026-09-12 and 2027-01-29. | The official declaration recorded by parliament.uk, or reported by BBC or the Guardian, names Polanski winner of a Holborn and St Pancras byelection held between 2026-09-12 and 2027-01-29; otherwise MISS. |
| KKR-20260911-57 | 31% | 2026-11-13 | disaster | The DRC Ebola outbreak reported in a seventh province on 2026-09-11 records at least one laboratory-confirmed case in an eighth DRC province between 2026-09-12 and 2026-11-11. | A WHO Disease Outbreak News item, WHO AFRO bulletin, or DRC health ministry statement carried by Reuters or AP confirms a case in an eighth province between 2026-09-12 and 2026-11-11; otherwise MISS. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "At least one commercial merchant vessel is struck by a missile, drone, or uncrewed surface vessel in the Red Sea, Bab al-Mandab, or Gulf of " → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; the resolution names a different subject than the statement — the claim is about Aden, Bab, Gulf, Mandab and the resolution settles on AP, MISS, Reuters, UKMTO. A row whose resolution checks a different fact can be scored correct while being wrong
- "At least one of the six Nigerian nationals in the romance-scam extradition case reported on 2026-09-11 is physically surrendered to the requ" → REJECTED: the resolution names a different subject than the statement — the claim is about Nigerian and the resolution settles on AP, BBC, MISS, Reuters. A row whose resolution checks a different fact can be scored correct while being wrong

## III. LEDGER STANDING

1937 issued all-time across 16 forecaster arms · 1601 open (63 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 618 issued · 580 open · 38 resolved · 18 hits / 20 misses · **Brier 0.280** against its own base rate 47.4% (climatological 0.249) · **skill -0.124**.

*21 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 618 | 580 | 38 | 18 | 20 | 0.280 | 47.4% | 0.249 | -0.124 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 254 | 125 | 120 | 26 | 94 | 0.195 | 21.7% | 0.170 | -0.151 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 45 | 45 | 0 | — | — | not computed | — | — | — |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 31 | 7 | 5 | 2 | 0.063 | 71.4% | 0.204 | +0.692 |
| manual/fable-5.1/unattested | 75 | 75 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 211 | 208 | 3 | 3 | 0 | 0.153 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 219 | 213 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 13 | 31 | 17 | 14 | 0.239 | 54.8% | 0.248 | +0.036 |
| manual/sonnet-5/unattested | 212 | 180 | 32 | 16 | 16 | 0.224 | 50.0% | 0.250 | +0.105 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*
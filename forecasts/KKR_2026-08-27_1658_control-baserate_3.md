**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 271658Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-27_1517.md · forecaster: control/baserate · 6 accepted / 4 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260827-107 | 33% | 2026-10-05 | cyber | The CISA Known Exploited Vulnerabilities catalog will add at least 20 CVE entries carrying a dateAdded value between 2026-09-01 and 2026-09-30. | Fetch the CISA KEV JSON feed and count entries whose dateAdded field falls between 2026-09-01 and 2026-09-30 inclusive. A count of 20 or more resolves TRUE. |
| KKR-20260827-108 | 25% | 2026-11-04 | economics/markets | The Federal Register will publish at least one presidential proclamation or executive order imposing new or increased US tariff rates, dated between 2026-09-01 and 2026-10-31. | A Federal Register presidential document published between 2026-09-01 and 2026-10-31 newly imposes or raises US duty rates on imported goods. Pure extensions of existing rates resolve FALSE. |
| KKR-20260827-109 | 53% | 2026-11-04 | military/conflict | The United States and Iran will hold publicly acknowledged direct bilateral talks between 2026-09-01 and 2026-10-31. | A US executive branch spokesperson and the Iranian foreign ministry each acknowledge that officials of the two states met directly between 2026-09-01 and 2026-10-31. Mediated contact alone resolves FALSE. |
| KKR-20260827-110 | 53% | 2027-01-06 | military/conflict | The UK government will attribute to Russia an attack causing physical damage or casualties to UK territory, UK-flagged shipping, or UK armed forces, occurring between 2026-08-28 and 2026-12-31. | A UK minister or the Ministry of Defence states that Russia carried out such an attack occurring between 2026-08-28 and 2026-12-31 and names the damaged asset or casualties. Cyber intrusion alone resolves FALSE. |
| KKR-20260827-111 | 44% | 2026-11-04 | political | King Harald V of Norway will die between 2026-08-28 and 2026-10-31 and Crown Prince Haakon will succeed him as king. | The Royal House of Norway announces the death of King Harald V on a date between 2026-08-28 and 2026-10-31, and Haakon is proclaimed king or takes the oath before the Storting. |
| KKR-20260827-112 | 43% | 2026-12-04 | crime/security | Spanish authorities will detain at least one person in connection with the theft of the Treasure of Villena, with the detention occurring between 2026-08-27 and 2026-11-30. | The Guardia Civil, the Policia Nacional, or the Spanish Interior Ministry states that a person was detained in connection with this theft between 2026-08-27 and 2026-11-30, carried by two independent outlets. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The FOMC will raise the federal funds target range above 3.50-3.75 percent at its scheduled decision on 2026-09-16." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "ICE Brent front-month crude futures will settle at or above 100.00 USD per barrel on at least one trading day between 2026-09-01 and 2026-10" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "At least one commercial vessel will sustain weapon-caused damage in the Strait of Hormuz, Gulf of Oman, or Persian Gulf between 2026-09-01 a" → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date; the resolution names only a venue or register (UKMTO) and no subject - the register is where to look, not what is claimed; name the subject inside it
- "The official confirmed death toll from the late-August 2026 Nepal-Tibet flash floods will stand at 750 or more at some point between 2026-09" → REJECTED: measurable claim without a numeric threshold — a row about a quantity must state the number next to its comparator; identifier digits (H.15, S&P 500) do not count

## III. LEDGER STANDING

1035 issued all-time across 14 forecaster arms · 874 open (4 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 245 issued · 228 open · 17 resolved · 8 hits / 9 misses · **Brier 0.275** against its own base rate 47.1% (climatological 0.249) · **skill -0.105** · under 30 resolved, this is noise.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 245 | 228 | 17 | 8 | 9 | 0.275 | 47.1% | 0.249 | -0.105 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 17 | 3 | 1 | 2 | 0.214 | 33.3% | 0.222 | +0.036 |
| lmstudio/auto[post-window] | 160 | 129 | 29 | 10 | 19 | 0.250 | 34.5% | 0.226 | -0.109 |
| lmstudio/auto[pre-verbot] | 60 | 7 | 45 | 13 | 32 | 0.222 | 28.9% | 0.205 | -0.081 |
| manual/fable | 45 | 32 | 13 | 7 | 6 | 0.183 | 53.8% | 0.249 | +0.265 |
| manual/fable-5 | 38 | 34 | 4 | 3 | 1 | 0.086 | 75.0% | 0.188 | +0.540 |
| manual/fable-5/unattested | 101 | 100 | 1 | 1 | 0 | 0.090 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 71 | 3 | 1 | 2 | 0.386 | 33.3% | 0.222 | -0.736 |
| manual/opus-5/unattested | 120 | 117 | 3 | 1 | 2 | 0.141 | 33.3% | 0.222 | +0.366 |
| manual/sonnet-5 | 45 | 25 | 20 | 12 | 8 | 0.231 | 60.0% | 0.240 | +0.037 |
| manual/sonnet-5/unattested | 110 | 102 | 8 | 5 | 3 | 0.174 | 62.5% | 0.234 | +0.257 |
| operator/human | 6 | 2 | 1 | 1 | 0 | 0.122 | 100.0% | 0.000 | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*
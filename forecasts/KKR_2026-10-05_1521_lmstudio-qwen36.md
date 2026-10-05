**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 051521Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-05_1516.md · forecaster: lmstudio/qwen36 · 2 accepted / 8 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261005-11 | 25% | 2026-10-21 | disaster | GDACS issues a Yellow or Red alert for a tropical cyclone affecting a populated area between 2026-10-12 and 2026-10-19. | The GDACS alert database records a Yellow or Red alert for a tropical cyclone affecting a populated area between 2026-10-12 and 2026-10-19. |
| KKR-20261005-12 | 20% | 2026-10-21 | disaster | A confirmed case of pneumonic plague is reported in Russia between 2026-10-12 and 2026-10-19. | A public health authority (e.g., WHO, Russian Ministry of Health) or a major wire service confirms a case of pneumonic plague in Russia between 2026-10-12 and 2026-10-19. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The CISA KEV catalog carries a date-added value for CVE-2026-88779 between 2026-10-04 and 2026-10-11." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; event window opens 2026-10-04, before this row is sealed (2026-10-05, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later; the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-88779 dateAdded 2026-10-04, already inside the claimed window 2026-10-04..2026-10-11
- "Spain holds a snap general election between 2026-10-12 and 2026-10-19." → REJECTED: the resolution names only a venue or register (interior, ministry, spanish) and no subject - the register is where to look, not what is claimed; name the subject inside it
- "WTI Crude closes above 95.00 on at least one trading day between 2026-10-12 and 2026-10-19." → REJECTED: the named venue is introduced by 'e.g.', which makes it an example rather than the source of record — the adjudicator still chooses. Strike the softener or name the class exhaustively
- "A US federal court issues a formal indictment against the suspected developer of Ploutus ATM malware between 2026-10-12 and 2026-10-19." → REJECTED: the named venue is introduced by 'e.g.', which makes it an example rather than the source of record — the adjudicator still chooses. Strike the softener or name the class exhaustively
- "The US Supreme Court hears oral arguments in the case involving big oil's bid to block climate damage lawsuits between 2026-10-12 and 2026-1" → REJECTED: resolution offers alternative VENUES joined by 'or' (…the us supreme court official docket | or | a major wire service reports that oral argume…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "A new vulnerability with CVSS score 9.0 or higher is added to the CISA KEV catalog between 2026-10-12 and 2026-10-19." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "The Euro falls below 1.10 against the US Dollar on at least one trading day between 2026-10-12 and 2026-10-19." → REJECTED: the named venue is introduced by 'e.g.', which makes it an example rather than the source of record — the adjudicator still chooses. Strike the softener or name the class exhaustively
- "A major cyberattack disrupts critical infrastructure in South Korea between 2026-10-12 and 2026-10-19." → REJECTED: the named venue is introduced by 'e.g.', which makes it an example rather than the source of record — the adjudicator still chooses. Strike the softener or name the class exhaustively

## III. LEDGER STANDING

3403 issued all-time across 19 forecaster arms · 2589 open (238 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36`:** 2 issued · 2 open · nothing resolved yet — this arm earns a score at its first resolution.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1218 | 1017 | 169 | 106 | 63 | 0.324 | 62.7% | 0.234 | -0.386 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 383 | 204 | 170 | 45 | 125 | 0.205 | 26.5% | 0.195 | -0.056 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/qwen36 | 2 | 2 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 180 | 145 | 34 | 26 | 8 | 0.383 | 76.5% | 0.180 | -1.128 |
| manual/fable | 45 | 20 | 25 | 13 | 12 | 0.190 | 52.0% | 0.250 | +0.241 |
| manual/fable-5 | 38 | 23 | 15 | 8 | 7 | 0.130 | 53.3% | 0.249 | +0.479 |
| manual/fable-5.1/unattested | 258 | 225 | 25 | 20 | 5 | 0.207 | 80.0% | 0.160 | -0.296 |
| manual/fable-5/unattested | 258 | 202 | 47 | 36 | 11 | 0.210 | 76.6% | 0.179 | -0.169 |
| manual/opus-5 | 74 | 55 | 19 | 11 | 8 | 0.188 | 57.9% | 0.244 | +0.228 |
| manual/opus-5.5/unattested | 87 | 87 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 286 | 30 | 20 | 10 | 0.217 | 66.7% | 0.222 | +0.025 |
| manual/sonnet-5 | 45 | 7 | 37 | 19 | 18 | 0.250 | 51.4% | 0.250 | +0.000 |
| manual/sonnet-5.5/unattested | 46 | 46 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 237 | 100 | 56 | 44 | 0.263 | 56.0% | 0.246 | -0.069 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*
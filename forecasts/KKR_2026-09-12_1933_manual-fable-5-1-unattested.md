**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 121933Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-12_1654.md · forecaster: manual/fable-5.1/unattested · 7 accepted / 3 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260912-26 | 80% | 2026-09-21 | economics/markets | At the FOMC meeting concluding 2026-09-16, the Federal Reserve raises the federal funds target range above the 3.50 to 3.75 percent range held at seal, so that FRED series DFEDTARU (target range upper limit) prints 4.00 or higher for 2026-09-17. | FRED series DFEDTARU (federal funds target range upper limit) shows a value of 4.00 or higher for 2026-09-17. Reference at seal: 3.75 percent upper limit on the packet date. |
| KKR-20260912-27 | 60% | 2026-10-02 | economics/markets | Between 2026-09-12 and 2026-09-30, Saudi Arabia publicly announces through its Energy Ministry, Saudi Aramco, or SPA that crude oil is again flowing through the East-West pipeline from Abqaiq to Yanbu, which was shut on 2026-09-11 after drone attacks launched from Iraq. | A Saudi Energy Ministry, Saudi Aramco, or SPA statement dated 2026-09-12 to 2026-09-30 says East-West pipeline crude flows have resumed, or Reuters and Bloomberg both report resumption within that window citing Saudi officials or Aramco. |
| KKR-20260912-28 | 45% | 2026-10-13 | cyber | The CISA Known Exploited Vulnerabilities catalog adds CVE-2026-85102 or CVE-2026-85103, the Check Point Security Gateway VPN remote code execution flaws patched on 2026-09-09, with a dateAdded value between 2026-09-12 and 2026-10-09 inclusive. | The CISA KEV JSON feed contains an entry for CVE-2026-85102 or CVE-2026-85103 whose dateAdded field falls between 2026-09-12 and 2026-10-09 inclusive. |
| KKR-20260912-29 | 40% | 2026-10-14 | cyber | Between 2026-09-12 and 2026-10-10, records taken from the Florida FLHSMV DAVID driver database in the September 2026 breach claimed by ShinyHunters are posted for public download or public viewing on a leak site, forum, or Telegram channel, not merely offered for private sale. | At least two of BleepingComputer, The Record, DataBreaches.net, TechCrunch, or a wire service publish, between 2026-09-12 and 2026-10-12, reports that DAVID breach records were publicly posted on a date within 2026-09-12 to 2026-10-10. |
| KKR-20260912-30 | 25% | 2026-10-13 | military/conflict | Between 2026-09-13 and 2026-10-10, United States forces conduct strikes on Houthi targets inside Yemen that US Central Command publicly acknowledges in a press release or official post. | A CENTCOM press release or official social media post dated 2026-09-13 to 2026-10-12 states that US forces struck Houthi targets in Yemen on a date within 2026-09-13 to 2026-10-10. |
| KKR-20260912-31 | 20% | 2026-11-17 | military/conflict | Between 2026-09-13 and 2026-11-13, the United States and Iran both publicly announce a ceasefire, pause, or cessation of hostilities in the war that resumed on 2026-07-08: the US via the White House or the President, Iran via its President, Foreign Minister, or Supreme National Security Council. | Statements from the White House or the President and from the Iranian President, Foreign Minister, or SNSC, each dated 2026-09-13 to 2026-11-13, announce or confirm the same ceasefire or pause in US-Iran hostilities. |
| KKR-20260912-32 | 45% | 2026-12-16 | political | Between 2026-09-12 and 2026-12-14, the federal respondents (Department of Energy or United States) seek further review of the D.C. Circuit judgment in Michigan v. Department of Energy, No. 25-1159, decided 2026-09-11, by petition for panel rehearing, rehearing en banc, or certiorari. | The D.C. Circuit docket in No. 25-1159 shows a federal petition for panel or en banc rehearing, or the Supreme Court docket shows a certiorari petition from that judgment, filed between 2026-09-12 and 2026-12-14. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "FRED series DCOILWTICO (WTI Cushing spot) prints 110.00 USD per barrel or higher on at least one business day between 2026-09-14 and 2026-09" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "The 10-year Treasury constant maturity yield, FRED series DGS10, closes at 5.25 percent or higher on at least one business day between 2026-" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "The DRC Bundibugyo Ebola outbreak reaches 10,000 or more cumulative confirmed cases in an official count with data through 2026-10-16 or ear" → REJECTED: resolution offers alternative VENUES joined by 'or' (…drc ministry of health | or | insp…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact; single-day resolution window for an unscheduled event — the row requires this to occur on 2026-09-12 exactly. Price a day, not a window: widen the window or state why the date is fixed

## III. LEDGER STANDING

1983 issued all-time across 16 forecaster arms · 1647 open (77 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/fable-5.1/unattested`:** 82 issued · 82 open · nothing resolved yet — this arm earns a score at its first resolution.

*21 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 631 | 593 | 38 | 18 | 20 | 0.280 | 47.4% | 0.249 | -0.124 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 259 | 130 | 120 | 26 | 94 | 0.195 | 21.7% | 0.170 | -0.151 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 53 | 53 | 0 | — | — | not computed | — | — | — |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 31 | 7 | 5 | 2 | 0.063 | 71.4% | 0.204 | +0.692 |
| manual/fable-5.1/unattested | 82 | 82 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 211 | 208 | 3 | 3 | 0 | 0.153 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 226 | 220 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 13 | 31 | 17 | 14 | 0.239 | 54.8% | 0.248 | +0.036 |
| manual/sonnet-5/unattested | 218 | 186 | 32 | 16 | 16 | 0.224 | 50.0% | 0.250 | +0.105 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*
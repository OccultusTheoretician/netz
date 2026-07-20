**UNCLASSIFIED // OPEN SOURCES**

# NETZ / KKR — open-source collation engine + scored forecast ledger

A daily intelligence product built from public feeds, and a predictive ledger
that keeps its own misses. Everything here is machine-collated open-source
material; every synthesized claim must cite the record beneath it; every
forecast carries a falsifiable resolution criterion, a deadline, and a
probability — and is scored against outcomes, permanently, in public.

**Live dashboards:** daily report (`/docs/index.html` via Pages) · ledger
(`/docs/ledger.html`) · latest forecasts (`/docs/kkr.html`)

## What this is

- **NETZ** (`netz.py`) — fetches 500+ items/day across curated RSS + keyless
  APIs (CISA KEV, NWS, ReliefWeb, market data), dedupes, clusters, scores
  corroboration (Admiralty A-F × 1-6, computed mechanically from feed tier ×
  independent-source count), tracks day-over-day deltas, matches standing
  Priority Intelligence Requirements, detects cross-category convergence, and
  optionally synthesizes through a local model under ICD 203 estimative
  discipline — with a citation auditor that machine-flags any synthesized
  sentence that does not cite the record.
- **KKR** (`kkr.py`) — elicits falsifiable projections from a model (local or
  API), passes them through a deterministic validation gate (rejections are
  published with reasons), and maintains the ledger: dated, misfire-inclusive,
  Brier-scored, calibration-tabled. Forecasts are tagged by which model made
  them. Resolutions are adjudicated by the operator against public reporting.

## Provenance

The collation, grading, and gate logic are deterministic code — inspect it.
The synthesis and forecasts are model-generated, tagged per model lane in the
ledger. The operator directs the system, adjudicates resolutions, and reviews
every published run. The commit history is the timestamp authority: nothing
here can be backdated, and the misses stay.

## The scoreboard

`LEDGER.md` — every projection ever issued, open and resolved, hits and
misses, with the standing Brier score (0 = oracle, 0.25 = coin-flipping on
50% calls) and the calibration table: stated probability vs. realized
frequency. That table is the only thing in this repository that constitutes
evidence of forecasting skill. Until it says otherwise, this is an
instrument being tested in public, not a validated one.

## Run it yourself

Python 3.10+, `pip install feedparser requests`, a local model via LM Studio
(optional — the collated report ships without one). `python netz.py` then
`python kkr.py`. Config in `report_config.json`: feeds, reliability tiers,
PIRs. No API keys required for any data source.

**UNCLASSIFIED // OPEN SOURCES**

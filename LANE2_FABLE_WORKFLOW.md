# LANE 2 — THE FABLE WORKFLOW (manual forecasting through Claude)

The lane where Claude does the analysis and red-team, not just a model filling a
template. No API key. The ledger tags these `manual/fable` so this lane is scored
separately from Qwen's daily runs.

## THE LOOP — 5 STEPS

**1. Generate the packet.**
Double-click `C:\netz\fable_packet.bat`.
It runs a fresh NETZ collation, then writes the packet WITHOUT running Qwen's
forecaster (so no throwaway projections stack in the ledger). It opens the
`forecasts\` folder for you. The file is `kkr_packet_[today].md`.

**2. Bring it here.**
Upload that `kkr_packet_[today].md` into the Claude project. Say:
    "run the projections"
Claude works the forecasts WITH the full corpus behind it — red-teams
calibration against live data, catches contradictions, applies base-rate
discipline — then returns ONE clean JSON array (the same format the gate expects).

**3. Save the JSON.**
Copy the JSON block Claude returns. Save it as exactly:
    C:\netz\fable_projections.json
(plain text; the whole `[ ... ]` array, nothing else).

**4. Ingest.**
Double-click `C:\netz\fable_ingest.bat`.
It runs the validation gate on the Fable projections, writes the survivors to
the ledger tagged `manual/fable`, publishes rejections with reasons, opens
`KKR_latest.html`.

**5. Publish (optional, when ready).**
`publish.bat` — review, push, dashboards update.

## WHY THE SEPARATE PACKET STEP

`fable_packet.bat` uses `--packet-only`, which is the difference from the daily
`kkr.bat`: it does NOT invoke Qwen, so running Lane 2 doesn't add a batch of
local-model projections you'd then have to void. The packet is just the report +
the projection prompt, ready for a stronger forecaster.

## SCORING

Every Fable projection carries `model: manual/fable` in `ledger.json`. When you
run `kkr.py --score` after resolutions, the calibration reflects all lanes
together — but because the tag is stored, the lanes can be separated later to
show which forecaster (Qwen / API / Fable-via-Claude) actually earns its Brier.

## WHEN TO USE THIS LANE

Not every day — Qwen's automated 06:00 run is the daily floor. Reach for Lane 2
on the days that matter: an active crisis, a big convergence, a batch you want
pressure-tested before it goes on the permanent record. The value is the
interrogation, not the generation.

## ONE-LINE VERSIONS (if you skip the bats)

    python C:\netz\netz.py & python C:\netz\kkr.py --packet-only
    [upload packet, get JSON, save as fable_projections.json]
    python C:\netz\kkr.py --ingest C:\netz\fable_projections.json

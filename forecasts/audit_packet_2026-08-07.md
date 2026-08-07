# KKR RESOLUTION AUDIT PACKET
Generated 072038Z AUG 26 · 2 projections past deadline, awaiting adjudication.

## YOUR TASK (independent auditor)

For EACH projection below, search public reporting and determine whether its
resolution criterion was met. You are auditing forecasts you did not make.

RULES:
1. Work the RESOLUTION CRITERION as written, not the statement's spirit. If the
   criterion demands two independent sources, one is not enough.
2. Search for DISCONFIRMING evidence as hard as confirming evidence. Note both.
3. If the evidence is genuinely ambiguous or you cannot verify, say so — do NOT
   guess. AMBIGUOUS is a valid verdict and is the correct one when the record is
   unclear.
4. Cite what you found: outlet, date, and what it said. Never assert without a source.
5. You do not know who made these forecasts or at what probability. Do not speculate.

Return ONLY a JSON array, no commentary, no markdown fences. Use plain ASCII
straight quotes and do not put quotation marks inside any string value:

[{"id": "KKR-YYYYMMDD-NN", "verdict": "HIT" | "MISS" | "AMBIGUOUS",
  "confidence": "high" | "moderate" | "low",
  "evidence": "what you found, with outlet and date, 1-3 sentences",
  "disconfirming": "contrary evidence found, or: none found",
  "note": "one line an adjudicator should know before ruling"}]

## PROJECTIONS AWAITING AUDIT


_adjudication-prompt sha256: e5a455ef443bcd9fa793de281b47273bc9b857ac4c4bcd5f305bcefba04e9ddf_

### KKR-20260726-19
- **Issued:** 2026-07-26  ·  **Deadline:** 2026-08-06
- **Domain:** political
- **Claim:** A new political party led by Senegal's Faye formally registers with the country's electoral commission between 2026-08-03 and 2026-08-06.
- **Resolution criterion:** The Senegalese electoral commission publishes a formal registration of a new political party led by Faye, as confirmed by Al Jazeera or a government press release, between 2026-08-03 and 2026-08-06.
- **Failure condition:** the condition stated in this entry's resolution basis — The Senegalese electoral commission publishes a formal registration of a new political party led by Faye, as confirmed by Al Jazeera or a government press release, between 2026-08-03 and 2026-08-06 — is not met on or before 2026-08-06; absence at the deadline scores this entry a MISS.

### KKR-20260730-26
- **Issued:** 2026-07-30  ·  **Deadline:** 2026-08-06
- **Domain:** economics/markets
- **Claim:** Meta Platforms stock will close lower than its 2026-07-30 closing price at least once more between 2026-07-31 and 2026-08-06.
- **Resolution criterion:** True if Meta Platforms common stock records at least one additional daily close below its 2026-07-30 close on any trading day between 2026-07-31 and 2026-08-06; otherwise false.
- **Failure condition:** Meta Platforms common stock records no daily close below its 2026-07-30 close on any trading day 2026-07-31 through 2026-08-06, per official exchange closing data as read on 2026-08-06; that reading scores this entry a MISS.

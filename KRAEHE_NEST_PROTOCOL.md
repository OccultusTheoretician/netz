# KRÄHE'S NEST PROTOCOL
## First Edition · 2026 · Revision 2
**KNP-26 · Issued by the Retro-Prescient Audit Desk**
*Implementer specification for the Selective-Disclosure Commitment Method (KNM-26). This document is buildable-to: an implementer who follows it produces a conformant sealer, hashlog, and aggregator without further reference to the desk.*

**PROVENANCE: DRAFT** (Claude-drafted under direction; revision 2 of 2026-07-25. His only after rework. The JSON shapes are normative and the prose explanatory. The 2.01 construction was verified against the demonstration clutch the day after issuance: all nine published commitments reproduce under it, independently re-derived from the vault by a second working session with no sight of the sealing code. The construction paragraph survived its first audit unamended.)

**WHAT CHANGED IN REVISION 2.** Two findings, both from independent working sessions converging on the same gaps. First: revision 1 never pinned the hashlog's container, so two conformant implementations could disagree on the first byte of the file — 4.01 now defines the top-level object. Second: the preimage construction lived only in spec prose and in committers' private vaults, but 5.02 verification is impossible without it — 4.01b now requires the construction as public machine-readable metadata in every hashlog. Also added: optional `level`, `architecture`, and `reveal_date` record fields carrying the KNM-26 rev. 2 conformance declarations (KNM Ch. 4–5) into the wire format.

---

## LETTER OF ISSUANCE

A method is not adoptable until someone other than its author can build it. KNM-26 states what the selective-disclosure commitment method *is*; this document states exactly what to build so that any two independent implementations interoperate — so that a Kall sealed by one conformant tool verifies under another, and an aggregator written by a third party can ingest both. The design goal is a **federated protocol**, the way RSS is federated: each committer runs their own sealer and publishes their own log to their own surface; the Nest is a read-only reader of those logs. There is no server to run, no account to hold, no central store to secure. That is a deliberate property, required by KNM 1.05, and this specification is written to preserve it.

— The Retro-Prescient Audit Desk, 2026

---

## CHAPTER 1 — SCOPE AND ROLES

**1.01** This specification defines three artifacts and the format contract between them:
a. **The sealer** — the committer's local tool. Seals Kalls, writes the hashlog and the vault, performs reveals. Runs on the committer's own machine.
b. **The hashlog** — the committer's public, append-only record of commitments. Published to a surface the committer does not solely control (§4).
c. **The aggregator (the Nest)** — a read-only surface that ingests one or more hashlogs and renders the collation.

**1.02** Roles map to KNM: the sealer and vault are the committer's; the hashlog is the committer's public commitment record; the aggregator holds no vault and receives no submission (KNM 1.05, 4.06).

**1.03** Requirement categories are **must** / **should** per KNM 2.01. JSON shapes marked *normative* are the interoperability contract; deviating from them breaks cross-implementation verification.

---

## CHAPTER 2 — THE COMMITMENT

**2.01 The canonical preimage (normative, must).** A Kall's commitment is the SHA-256 hash of a single UTF-8 string, the *canonical preimage*, formed by joining exactly these fields with the ASCII pipe `|` in exactly this order:

```
id | timestamp | statement | resolution_basis | salt
```

- `id` — the committer's Kall identifier (§3.02). ASCII, no pipe.
- `timestamp` — ISO 8601 UTC, second precision, `Z` suffix (e.g. `2026-07-25T18:30:00Z`).
- `statement` — the predictive claim, UTF-8. Must not contain the pipe character; if the claim requires a pipe, the implementer must escape it as `\u007C` before joining and unescape on reveal (documented per implementation).
- `resolution_basis` — the criterion by which the committer will judge the Kall at reveal. UTF-8, pipe-escaped as above.
- `salt` — a cryptographically random secret, minimum 128 bits, hex-encoded (32 hex chars). One salt per Kall. Never reused.

**2.02** The commitment is `SHA-256(preimage)`, lowercase hex. This is the value published in the hashlog. The preimage (and therefore the salt, statement, and basis) stays in the vault.

**2.03 Reference construction (informative).** In Python:
```python
import hashlib, secrets
salt = secrets.token_hex(16)                      # 128-bit salt
preimage = f"{id}|{timestamp}|{statement}|{basis}|{salt}"
commitment = hashlib.sha256(preimage.encode("utf-8")).hexdigest()
```
Any language producing the identical byte sequence for the preimage yields the identical commitment. That byte-for-byte identity is the interoperability contract (2.01).

**2.04 The hiding property (must).** The salt is mandatory and must be high-entropy. Without it, a low-entropy statement (a yes/no, a short claim from a small space) could be confirmed by an adversary who guesses candidate statements and recomputes the hash. The salt defeats this. An implementation that omits the salt or draws it from a low-entropy source is nonconformant (KNM 3.01).

**2.05 The binding property.** SHA-256 collision resistance provides binding: the committer cannot find a different `(statement, basis)` producing the same commitment, so a published commitment fixes the content.

---

## CHAPTER 3 — THE VAULT

**3.01 Vault contents (normative shape).** The vault is the committer's private store. One record per Kall:
```json
{
  "id": "KK-20260725-01",
  "timestamp": "2026-07-25T18:30:00Z",
  "statement": "...",
  "resolution_basis": "...",
  "probability": 60,
  "deadline": "2027-01-01",
  "salt": "b3f1...",
  "commitment": "b8a0d9b0c78216..."
}
```

**3.02 Identifier scheme (should).** `id` is recommended as `KK-YYYYMMDD-NN` (committer prefix optional for federation, e.g. `NEB-KK-20260725-01`, to disambiguate across committers in an aggregator). Ids must be unique within a committer's hashlog.

**3.03 The vault must never leave the committer's control (must).** It is not transmitted, not committed to any public repository, and not held by any aggregator. An implementation must make it difficult to publish the vault by accident: the sealer should write the vault outside any version-controlled directory by default and should emit the public hashlog as a *separate* file. (Operational note from first deployment: the single highest-risk error is committing the vault to a public repo. Implementations should ship a `.gitignore` fragment matching the vault filename and should refuse, or loudly warn, if asked to publish a file containing salt values.)

**3.04 Salt custody (must).** Loss of a Kall's salt makes that Kall permanently unrevealable — the commitment can never be reproduced. The vault is therefore the committer's critical secret and should be backed up privately.

---

## CHAPTER 4 — THE HASHLOG

**4.01 Hashlog container and record (normative shape).** The hashlog is a single JSON **object** — not a bare array — with exactly this top-level shape:
```json
{
  "protocol": "KNP-26",
  "construction": { ... },
  "records": [ ... ]
}
```
Each entry of `records` carries only opaque and non-sensitive fields — never statement, basis, or salt:
```json
{
  "id": "KK-20260725-01",
  "timestamp": "2026-07-25T18:30:00Z",
  "commitment": "b8a0d9b0c78216b93ba2f535a79f9294041053077b7d25f82e1a7ab85438e704",
  "probability": 60,
  "deadline": "2027-01-01",
  "status": "SEALED",
  "domain": "military_conflict",
  "level": 1,
  "architecture": "A",
  "reveal_date": null
}
```
`status` is one of `SEALED` | `REVEALED` | `RESOLVED_HIT` | `RESOLVED_MISS` | `VOID`. `probability`, `deadline`, and `domain` are publishable metadata; they are **outside the preimage** and therefore anchored by §4.03, not bound by the hash — a hashlog **should** say so on its face. `level` and `architecture` carry the committer's KNM-26 conformance declarations (KNM 2.02, 5.06); `reveal_date` is required where `level` is 2. The interoperability contract is `protocol`, `construction`, and per-record `id`, `timestamp`, `commitment`, `status`.

**4.01b The construction block (must — added rev. 2).** The `construction` object states the preimage recipe in machine-readable form:
```json
{
  "preimage_order": ["id", "timestamp", "statement", "resolution_basis", "salt"],
  "separator": "|",
  "hash": "SHA-256",
  "encoding": "UTF-8",
  "pipe_escape": "\\u007C"
}
```
This block exists because §5.02 verification is impossible without the recipe: a stranger holding a reveal and a bare commitment cannot recompute unless the construction is public. Revision 1 left the recipe in spec prose and in the committer's private store — which meant the one artifact verification depends on lived behind the same wall as the secrets. A hashlog without a construction block is not conformant with revision 2. The block describes §2.01's construction and must match it; a committer using a legacy construction (sealed before this revision) publishes the construction actually used, and the published commitment always governs over any spec text.

**4.02 Append-only (must).** The hashlog is append-only. New Kalls append; a reveal or resolution *updates the status field of an existing record in place* but must never remove a record or alter its `commitment`. The committed count is the number of records.

**4.03 External anchoring (must — this is the count commitment, KNM 3.02).** The append-only property must be enforced by a mechanism the committer does not solely control. Any of:
a. **Public version control** — the hashlog lives in a public git repository; commit history makes the sequence of states tamper-evident (a silent deletion shows in the diff).
b. **External beacon** — the committer periodically posts the count and a hash of the full hashlog to a surface they do not own (a public social post, a timestamping service), creating dated third-party snapshots.
c. **Both** (recommended). The reference deployment uses git commit history as the primary clock and a periodic external beacon as the secondary.
Without external anchoring, the count is not committed — the committer could rewrite the log — and the scheme degrades to gameable per-item commitment (KNM 1.04). This requirement is what makes the method's integrity real.

**4.04 The standing line (should).** The hashlog (or its rendered page) carries a standing summary: `N sealed · M revealed · K resolved`. This is the visible denominator that makes withholding legible (KNM 3.02).

---

## CHAPTER 5 — REVEAL AND VERIFICATION

**5.01 Reveal (must).** To reveal a Kall, the committer publishes its `statement`, `resolution_basis`, and `salt` (the vault fields), and updates the hashlog record's `status` to `REVEALED` (or a resolved status). Reveal is voluntary, per-Kall, and irreversible (a revealed Kall's content is now public).

**5.02 Verification (normative procedure).** Any party verifies a revealed Kall by reconstructing the canonical preimage — per the hashlog's own `construction` block (4.01b) — from the published fields and recomputing the hash:
```
recomputed = SHA-256( id | timestamp | statement | resolution_basis | salt )
verified   = (recomputed == published_commitment)
```
A match proves the revealed content is exactly what was sealed at `timestamp`, unedited. A mismatch means the committer altered the content after sealing (integrity failure) or the reveal is malformed.

**5.03 No forced reveal (must).** There must be no mechanism by which any party other than the committer can reveal, or compel the reveal of, a sealed Kall. Abyssal is the default and only the committer exits it (KNM 3.04).

**5.04 Resolution (should, per RPAS).** A revealed Kall may be resolved against its `resolution_basis`. Where the committer asserts foresight, resolution follows RPAS (blind adjudication where possible; the keyed/keyless split; misses logged with the ceremony of hits). Where the committer makes no faculty claim, bare reveal-and-verify is sufficient and no adjudication standard is invoked. The protocol supports both; the claim the committer makes determines which standard binds.

**5.05 The misses-stay-bound rule (must).** A committer must not delete a sealed Kall to avoid a miss. Because the log is externally anchored (4.03), deletion is detectable against prior-published state. A Kall that is neglected, deleted, or altered is treated as a miss / VOID by any conformant aggregator scoring it (RPAS 5.06 incorporated).

---

## CHAPTER 6 — THE AGGREGATOR (THE NEST)

**6.01 Read-only (must).** The Nest ingests published hashlogs by URL and renders the collation. It receives no submissions, holds no vaults, and performs no writes to any committer's record (KNM 1.05, 5.01).

**6.02 Ingestion (normative).** The Nest is configured with a list of participating hashlog URLs. For each, it fetches the JSON, validates records against the §4.01 shape, and renders. A committer joins the federation by publishing a conformant hashlog and being added to (or self-registering on) the Nest's source list. No account, no backend.

**6.03 Rendering (should).** The Nest may display, per committer: sealed count, revealed count, resolved count, reveal rate, and — for committers past a stated resolution floor (default 30, per RPAS) — a calibration table over their *revealed and resolved* Kalls. It may offer filter/sort/compare across committers as a client-side interactive.

**6.04 Verification on display (should).** For any revealed Kall it renders, the Nest should recompute the commitment (5.02) from the published fields and display a verified / mismatch indicator, so the reader need not trust the committer's own assertion of integrity.

**6.05 No faculty ranking (must).** The Nest must not rank committers as "prescient" or present aggregate display as evidence of foresight (KNM 5.03, 1.06). Calibration is displayed as data with its noise-floor caveat, not as a leaderboard of insight.

**6.06 Revealed-content responsibility (must).** For revealed content it renders, the Nest attributes each Kall to its source hashlog, states on its face that it is an aggregator of commitments and not a publisher vouching for content, and carries a revealed-content policy covering unlawful material and material targeting private individuals (KNM 5.02). Sealed commitments are opaque and carry no such burden; the burden attaches only at reveal.

---

## CHAPTER 7 — CONFORMANCE

**7.01** A **conformant sealer** implements Chapters 2, 3, 5 (§5.01–5.03): canonical preimage, mandatory high-entropy salt, vault/hashlog separation with the vault kept private, append-only status updates, and voluntary per-Kall reveal with no forced-reveal path.

**7.02** A **conformant hashlog** satisfies Chapter 4: the §4.01 container and record shape (at minimum `protocol`, `construction`, and the four per-record fields), the §4.01b construction block, append-only with in-place status updates, and external anchoring per §4.03.

**7.03** A **conformant aggregator** satisfies Chapter 6: read-only, no submissions, no faculty ranking, verification-on-display, and revealed-content responsibility.

**7.04** An implementation claiming conformance with KNP-26 must meet all applicable *must* requirements. A scheme with a submission backend, a mutable log, or a missing salt is not a KNP-26 implementation regardless of surface similarity (KNM 2.03).

**7.05** Citation is by paragraph ("KNP 2.01"). Conformance certifies the integrity properties of the commitment scheme (KNM 1.06); it certifies nothing about the quality of any committer's predictions.

---

*End of KNP-26. The method this protocol implements is KNM-26. Together they define Krähe's Nest: a federated, trustless, selective-disclosure prediction-commitment protocol in which each committer holds their own vault and the Nest only reads.*

---

## REVISION HISTORY

**Rev. 2 · 2026-07-25.** Container pinned as a JSON object (4.01), closing the finding that two conformant implementations could disagree on the file's first byte. Construction block made mandatory public metadata (4.01b) so §5.02 verification never depends on private material; this and the container finding were reached independently by two working sessions operating without sight of each other, and the convergence is recorded here as the reason for the change. Optional `level`, `architecture`, `reveal_date` fields added, carrying KNM-26 rev. 2 declarations into the wire format. Separately recorded: §2.01's construction was verified against the nine published commitments of the demonstration clutch by independent re-derivation from the vault — 9/9 reproduce — the day after issuance. The construction paragraph stands unamended.

**Rev. 1 · 2026-07-25.** First edition, issued the day the demonstration clutch was sealed.

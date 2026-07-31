# DECC-26™ — DENOMINATOR-COMMITTED EVIDENCE STANDARD
## Evidentiary completeness for machine-generated records
### First Edition · 2026 · Revision 1

**Issued by the Retro-Prescient Audit™ Desk**
*Companion to the reference implementation `denom.py`. This document defines the
METHOD; the implementation is one conformant build of it.*

**PROVENANCE: DRAFT** (Claude-drafted under direction, 2026-07-30. His only
after rework pass. Every regulatory citation is named at article level and
requires paragraph-level verification against the current authoritative text
before it is printed as a citation. The prior-art boundary in Chapter 9 is
stated conservatively and is his to verify before any ownership assertion is
made in public.)

---

## LETTER OF ISSUANCE

There is a standard problem in any regime where an operator must show a
regulator, an auditor, or a court what a machine produced: **the party who
selects the evidence is the party the evidence is about.**

The instruments in current use each solve half of it. **Per-record
timestamping** — now shipping in several commercial products, generally on an
RFC 3161 token or a chained hash — proves that a specific record existed at a
specific time and has not been altered. It is sound, and it is not enough: an
operator may seal a thousand records, disclose the nine that flatter, and every
disclosed hash will verify perfectly while the disclosure is a lie of omission.
**Whole-set disclosure** removes that discretion by revealing everything, and
is unusable wherever records carry trade secrets, personal data, or privilege.

Stated in the register a practitioner recognises: **a disclosed subset chosen by
the party under examination is a management-selected sample, and a
management-selected sample is not evidence about the population it came from.**
Every substantive control in this standard is subordinate to fixing that.

This standard resolves the two instruments against each other. Records are
sealed individually, so any subset may be disclosed. The **count** of sealed
records is committed externally, so the population's size cannot be revised
after the fact. Contents stay dark; **cardinality does not.** The denominator
becomes a fact the operator cannot move, and selective disclosure becomes an
audited choice rather than an invisible one.

The mechanism does not make the operator independent. In any deployment the
operator remains custodian, discloser, and — absent further controls —
adjudicator of what gets sealed. No cryptography changes that. What the
mechanism does is **narrow discretion until only nameable amounts remain**, and
this standard then requires those remainders to be printed on the record's own
face (Chapter 8). A record stating which discretions survive is stronger than
one implying it has none. That is what a professional standard does with an
impairment it cannot eliminate, and it is what this one does.

— The Retro-Prescient Audit Desk, 2026

---

## CHAPTER 1 — FOUNDATION AND TERMS

**1.01** This standard defines the *denominator-committed evidence method*: a
scheme by which an operator seals machine-generated records individually,
commits the population's cardinality to an external record, discloses any
subset with inclusion proofs, and cannot understate the population without
detection.

**1.02** Terms.
- **Record.** One machine-generated output and its bound metadata.
- **Operator.** The party who generates and seals records.
- **Vault.** The operator's append-only sealed store.
- **Commitment.** A hiding, binding digest of a record.
- **Anchor.** A published tuple fixing the population count, its Merkle root,
  and the chain head at a point in time.
- **Disclosure bundle.** A subset of opened records with inclusion proofs.
- **Relying party.** Auditor, regulator, counterparty, or court.

**1.03** Normative keywords: MUST, MUST NOT, SHOULD, MAY, per their ordinary
standards meaning.

---

## CHAPTER 2 — THE COMPLETENESS PROBLEM (informative)

**2.01** Integrity and completeness are different properties. Integrity asks
whether *this* record is unaltered. Completeness asks whether *these* records
fairly represent the population. Tooling that supplies only the first invites a
relying party to infer the second, which is the failure this standard addresses.

**2.02** The failure is not hypothetical or exotic. It is the ordinary shape of
selective disclosure, and it survives every per-record integrity control,
because each disclosed item is genuinely authentic. Authenticity of a sample is
silent about the sample's construction.

**2.03** Committing cardinality is the minimum control that makes the
construction visible. It does not prevent an operator from disclosing
favourably; it prevents the relying party from being unable to see that a choice
was made and how large the unseen remainder is.

---

## CHAPTER 3 — COMMITMENT CONSTRUCTION (normative)

**3.01** Each record MUST be committed as:

```
commitment = H( TAG_COMMIT ‖ salt ‖ H(content) ‖ H(canonical_metadata) )
```

**3.02** `H` MUST be a cryptographic hash with at least 256-bit output. SHA-256
satisfies this edition.

**3.03** `salt` MUST be at least 32 bytes from a cryptographically secure
source, unique per record. The salt provides the hiding property; without it a
low-entropy record is recoverable from its commitment by exhaustive search.

**3.04** `canonical_metadata` MUST be a deterministic serialisation — sorted
keys, fixed separators, explicit encoding — so that a relying party recomputes
the identical digest.

**3.05** Domain separation tags MUST distinguish commitment hashing, chain
hashing, and tree hashing. A construction that reuses one digest across roles
invites cross-protocol substitution.

---

## CHAPTER 4 — THE CHAIN (normative)

**4.01** The vault MUST maintain an append-only chain:
`h_i = H( TAG_CHAIN ‖ h_{i-1} ‖ canonical_entry_core )`, with the genesis
predecessor a fixed zero value.

**4.02** `entry_core` MUST bind at minimum the sequence number, the seal
timestamp, and the commitment.

**4.03** The chain makes retroactive edits detectable *internally*. It is not a
substitute for external anchoring (Chapter 5): an operator who controls the
whole vault can rebuild a consistent chain. The chain detects corruption and
accident; the anchor is what binds the operator.

---

## CHAPTER 5 — ANCHORING (normative)

**5.01** An anchor MUST contain the population count, a Merkle root over all
commitments in sequence, the chain head, and a generation timestamp.

**5.02** The Merkle construction MUST use domain-separated leaf and internal
node hashing and MUST NOT duplicate a final odd leaf. The RFC 6962 construction
— leaf `H(0x00 ‖ data)`, node `H(0x01 ‖ left ‖ right)`, split at the largest
power of two below the count — satisfies this and avoids the duplicate-leaf
malleability class.

**5.03** The anchor, or a digest of its canonical form, MUST be published to a
venue **the operator does not control**. Acceptable venues include a public
version-control host, an RFC 3161 timestamp authority, a certificate
transparency log, or a public distributed ledger.

**5.04** **The evidentiary weight of an anchor equals the independence of its
venue.** An anchor published only to operator-controlled storage provides
internal consistency and no external binding, and MUST be described as such.

**5.05** Anchors SHOULD be emitted on a stated cadence declared in advance.
Anchoring only when convenient reintroduces timing discretion.

---

## CHAPTER 6 — DISCLOSURE AND VERIFICATION (normative)

**6.01** A disclosure bundle MUST contain, for each disclosed record: the
opening material (salt, content, metadata), the commitment, the sequence index,
and an inclusion proof against a named anchor.

**6.02** The bundle MUST carry the anchor's count. **The denominator travels
with the disclosure.** A bundle that omits it is non-conformant.

**6.03** A relying party MUST be able to verify a bundle using only the bundle,
the independently published anchor, and a conformant verifier — with **no
service call to the operator and no trust in the operator's infrastructure.**

**6.04** Verification MUST confirm, for each disclosed record: content digest
matches; commitment reopens from salt, content, and metadata; and the inclusion
proof binds the commitment to the anchored root at the claimed index.

**6.05** A conformant verifier MUST reject: altered content, altered metadata,
altered salt, substituted commitments, relabelled indices, reduced counts, and
substituted roots.

---

## CHAPTER 7 — CUSTODY (normative)

**7.01** Opening material — salts and record contents — is the sensitive asset.
It MUST NOT be published, and MUST NOT reside in any repository or storage
synchronised to a public venue.

**7.02** Loss of opening material renders affected records permanently
undisclosable. The commitments and the anchored count survive, so the population
size remains provable; the records themselves do not. Custody design MUST state
the retention period and the backup regime.

**7.03** Anchors and disclosure bundles are the only artefacts intended for
release.

---

## CHAPTER 8 — DISCLOSED DISCRETIONS (normative)

**8.01** A conformant deployment MUST publish, with any disclosure, the
discretions the mechanism does not remove. At minimum:

**a. Capture completeness.** The method proves the size of the *sealed*
population, not that every record the system produced was sealed. This gap MUST
be addressed by deployment control — sealing enforced in the generation path —
and the reconciliation basis (inference logs, billing records, request counts)
MUST be stated. **This is the standard's principal residual risk and MUST NOT be
left unstated.**

**b. Anchor independence.** The venue MUST be named, so a relying party can
assess it against 5.04.

**c. Sampling.** Which records are disclosed remains the operator's choice. The
method makes the choice visible and its remainder measurable; it does not make
it neutral.

**8.02** Conformance levels.
- **Level 1 — Sealed.** Chapters 3, 4, 7. Internal integrity only.
- **Level 2 — Anchored.** Level 1 plus Chapter 5 with an independent venue.
- **Level 3 — Disclosing.** Level 2 plus Chapter 6.
- **Level 4 — Reconciled.** Level 3 plus a stated, tested reconciliation under
  8.01(a) binding the sealed population to the generated population.

**8.03** Only Level 4 supports an unqualified completeness assertion. Levels 1–3
MUST qualify their claims to the sealed population.

---

## CHAPTER 9 — PRIOR ART BOUNDARY (informative)

**9.01** Claimed as occupied, and not claimed here: hash commitment to a
prediction or record; commit-reveal protocols; RFC 3161 timestamping of
model outputs; Merkle inclusion proofs and transparency logs; sealed forecasts
published as digests. These are decades-established, patented in places, and
shipping commercially.

**9.02** The contribution claimed by this standard is narrow and specific: **the
committed cardinality of a partially disclosed population, carried with the
disclosure, as a completeness control** — together with the requirement that
surviving discretions be printed on the record's face (Chapter 8).

**9.03** That claim is stated conservatively and requires independent
verification before any ownership assertion is made in public.

---

## CHAPTER 10 — REGULATORY MAPPING (informative)

**10.01** This standard is a technical evidence control, not legal advice, and
conformance is not a compliance determination. The mapping below identifies
obligations onto which the control plausibly maps and MUST be confirmed against
current authoritative texts and counsel.

**10.02** EU AI Act — record-keeping and logging obligations (Article 12) call
for records adequate to trace system functioning; a denominator-committed vault
supplies traceable records whose population size is provable. Technical
documentation obligations (Article 11, Annex IV) call for evidence a conformity
assessor can rely on. Transparency obligations (Article 50) concern marking and
disclosure of machine-generated content, where provenance evidence is relevant.
Each citation requires paragraph-level verification before use.

**10.03** Assurance and audit standards generally — the completeness assertion
over a population is a standard audit concern, and the control is designed to
be legible in that register: a fixed denominator, a defined population, stated
scope limitations.

**10.04** Nothing in this standard asserts endorsement by, or affiliation with,
any regulator, agency, or standards body.

---

## REVISION HISTORY

**Revision 1 (2026-07-30).** First issuance. Reference implementation
`denom.py` 0.1.0 published concurrently, adversarially tested against eight
forgery classes and property-tested over tree sizes 1–24.

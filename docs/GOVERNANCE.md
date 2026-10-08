# Governance Model

**Status:** Proposed  
**Purpose:** Translate Sovereign Human Authority into enforceable decision controls.

---

## Decision Classes

### D0 — Informational

Examples:
- summarize public material
- classify documents
- draft options

Default:
- no special approval
- no external side effect

### D1 — Reversible Operational

Examples:
- create a draft
- organize internal files
- schedule a non-binding internal task

Default:
- delegated authority may be sufficient
- action must be reversible
- audit required

### D2 — Material but Reversible

Examples:
- publish approved material
- send consequential outreach
- change a non-critical system configuration

Possible controls:
- SHA approval
- second confirmation
- trusted-device confirmation
- explicit rollback path

### D3 — High Consequence

Examples:
- material financial commitment
- binding contract action
- governance change
- transfer of sensitive information
- persistent privileged access

Proposed controls:
- SHA authorization
- cooling-off
- second-human confirmation
- trusted-device confirmation
- multi-signature where appropriate
- independent verification
- full audit record

### D4 — Sovereign / Irreversible

Examples:
- ownership transfer
- permanent governance change
- high-value asset transfer
- key-root replacement
- succession activation

Proposed controls:
- highest human threshold
- no autonomous execution
- explicit legal / governance process
- multi-party authorization
- delay / challenge window where lawful and practical
- independent verification
- recovery plan

---

## Cooling-Off

Cooling-off is intended to reduce:

- manipulation under urgency
- impulsive irreversible action
- compromised-session risk
- social engineering

It should not be universal.

Use it where delay reduces risk more than it destroys value.

---

## Second-Human Confirmation

A second human is not automatically a rubber stamp.

The second confirmer should receive:

- the proposed action
- material evidence
- main dissent
- key risks
- what becomes irreversible
- scope of authorization

---

## Trusted-Device Confirmation

Device confirmation is an additional factor, not sovereign authority.

It can help prove that approval came through an expected control channel.

It cannot prove that:

- the person understood the decision
- the device is uncompromised
- the evidence is correct

---

## Multi-Signature Governance

Multi-signature control may be useful for:

- asset movement
- root governance changes
- high-privilege key operations
- emergency control

But signature count is not legitimacy.

A compromised or captured signer set can still make a bad decision.

SFII therefore treats multi-signature as one control inside a broader governance process.

---

## DAO Elements

DAO-like mechanisms may be useful for:

- transparent proposals
- voting rules
- quorum
- delegation
- time locks
- auditability

SFII does not assume public-token governance.

A family governance system may use cryptographic governance without creating a speculative token or public DAO.

---

## Authorization Record

A consequential authorization should be able to answer:

- who authorized
- what exactly was authorized
- under which policy version
- decision class
- evidence package hash / reference
- dissent presented
- time
- expiry
- required co-approvers
- permitted execution channel
- result
- verification

---

## Governance Failure Modes

- approval fatigue
- rubber-stamp second approver
- emergency bypass becoming normal
- authority creep
- key-person dependency
- family capture / coercion
- silent policy change
- AI manipulation of framing
- inaccurate identity / role data
- unusable recovery process

Governance design must account for these explicitly.

# Threat Model

**Status:** Public conceptual threat model  
**Scope:** SFII architecture, governance and AI-assisted decision flows

This is not a penetration test or a security certification.

---

## T1 — Hallucinated Evidence

**Failure:** an AI invents a source, fact or relationship.

**Control direction:**
- provenance
- source retrieval
- evidence / inference separation
- material-claim verification
- no execution based solely on unsupported generated text

---

## T2 — Prompt Injection

**Failure:** retrieved content attempts to alter agent instructions or authorize actions.

**Control direction:**
- treat retrieved content as data
- isolate policy from content
- connector permission boundaries
- explicit execution authorization
- suspicious-instruction detection

---

## T3 — Model Monoculture

**Failure:** many “agents” share the same underlying model or assumptions, creating fake diversity.

**Control direction:**
- provider / model diversity where material
- independent prompts and methods
- dependency mapping
- correlated-failure reporting

---

## T4 — False Consensus

**Failure:** majority agreement suppresses a correct minority view.

**Control direction:**
- preserve dissent
- severity-weighted escalation
- minority evidence channel
- red-team review
- no simple majority-as-truth rule

---

## T5 — Automation Bias

**Failure:** humans defer to a polished AI recommendation without real review.

**Control direction:**
- expose uncertainty
- show counterarguments
- show what would change the recommendation
- identify irreversible consequences
- meaningful approval interface

---

## T6 — Poisoned Memory

**Failure:** incorrect, malicious or obsolete information enters canonical family memory.

**Control direction:**
- provenance
- versioning
- confidence
- correction history
- source-bound facts
- quarantine for unverified memory

---

## T7 — Connector Compromise

**Failure:** an external application or connector returns manipulated data or executes outside intended scope.

**Control direction:**
- least privilege
- connector isolation
- output validation
- transaction verification
- separate authorization gateway
- revocation

---

## T8 — Key Compromise

**Failure:** attacker obtains authority credentials.

**Control direction:**
- multi-factor / trusted-device controls
- multi-signature where appropriate
- key rotation
- offline / recovery path
- spending / action limits
- anomaly detection

---

## T9 — Governance Capture

**Failure:** a human or coalition legally or technically captures decision rights against family intent.

**Control direction:**
- clear constitutional rules
- separation of powers
- succession logic
- challenge / delay mechanisms
- transparent policy history
- independent recovery path

---

## T10 — Silent Authority Creep

**Failure:** repeated convenience delegations gradually become permanent authority.

**Control direction:**
- expiring permissions
- explicit renewal
- decision-class boundaries
- periodic authority review
- no self-expansion

---

## T11 — Model Drift / Vendor Change

**Failure:** behavior changes without architecture change.

**Control direction:**
- model version logging
- benchmark suites
- critical-workflow regression tests
- vendor portability
- policy external to model

---

## T12 — Vendor Lock-In

**Failure:** family memory, governance or workflows become inseparable from one provider.

**Control direction:**
- open/exportable schemas
- canonical local records
- adapter layer
- model abstraction
- exit testing

---

## T13 — Audit-Layer Failure

**Failure:** logs can be altered, lost or made inaccessible.

**Control direction:**
- append-only / tamper-evident design
- independent backup
- cryptographic verification where useful
- retention policy
- recovery testing

---

## T14 — Human Coercion / Social Engineering

**Failure:** authorized person is manipulated into approving a harmful action.

**Control direction:**
- cooling-off
- second-human confirmation
- out-of-band verification
- risk-triggered delay
- clear display of consequences

---

## T15 — Complexity Collapse

**Failure:** governance becomes so complex that humans bypass it.

**Control direction:**
- decision classes
- proportional controls
- usability testing
- remove low-value gates
- measure approval burden

---

# Threat-Model Rule

A new control is justified only if it materially reduces a plausible failure mode without creating greater fragility, cost or bypass pressure elsewhere.

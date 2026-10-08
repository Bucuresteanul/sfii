# Threat → Control Matrix

**Status:** Proposed control mapping  
**Purpose:** Make the SFII threat model testable.

| Threat | Primary controls | Verification direction | Current status |
| --- | --- | --- | --- |
| T1 Hallucinated evidence | provenance, evidence labels, source verification | unsupported material claim must be rejected or labeled | Proposed |
| T2 Prompt injection | content/policy separation, least privilege, authorization gateway | hostile retrieved instruction cannot alter policy | Proposed |
| T3 Model monoculture | provider/model diversity, dependency map | detect correlated agent dependencies | Research |
| T4 False consensus | dissent preservation, severity escalation | minority severe risk must survive synthesis | Proposed |
| T5 Automation bias | uncertainty, counterarguments, consequence display | human review interface test | Research |
| T6 Poisoned memory | provenance, versioning, quarantine, correction history | tampered/unverified memory cannot become canonical silently | Proposed |
| T7 Connector compromise | isolation, bounded tokens, transaction verification | connector cannot exceed authorization envelope | Proposed |
| T8 Key compromise | MFA/device, multisig, rotation, limits | stolen single factor insufficient for D3/D4 | Research |
| T9 Governance capture | separation of powers, challenge window, recovery | governance takeover scenario | Research |
| T10 Authority creep | expiring permissions, explicit renewal | delegated authority expires automatically | Proposed |
| T11 Model drift | model/version logging, regression suite | critical workflow behavior compared across versions | Research |
| T12 Vendor lock-in | portable schemas, local canonical state, adapters | replace provider without losing governance/memory | Proposed |
| T13 Audit failure | tamper evidence, independent backup, recovery | audit remains verifiable after primary-store failure | Research |
| T14 Human coercion | cooling-off, second human, out-of-band verification | simulated coercion/urgency scenario | Research |
| T15 Complexity collapse | proportional controls, usability, burden measurement | users can complete required approvals without bypass | Research |

---

## Control Principles

### Defense in depth

No single control should be treated as sufficient for a D3/D4 action.

### Independent verification

Where practical, the system that performs a consequential action should not be the sole system attesting that it succeeded correctly.

### Proportionality

D0 and D1 workflows should remain lightweight.

If every action feels like D4, users will bypass governance.

### Fail closed for authority

If required approval state cannot be established, execution stops.

### Fail gracefully for intelligence

If a model/provider fails, the system should preserve evidence, policy and human authority and degrade rather than collapse.

---

## Verification Priority

The first reference implementation should test, in order:

1. self-escalation prevention
2. prompt-injection resistance at the policy boundary
3. dissent preservation
4. approval expiry
5. target / parameter binding
6. second-human role validation
7. connector permission containment
8. audit integrity
9. provider substitution
10. recovery from partial infrastructure failure

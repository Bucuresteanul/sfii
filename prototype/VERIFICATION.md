# Prototype Verification Record

**Artifact:** `prototype/policy_gate.py`  
**Test suite:** `prototype/test_policy_gate.py`  
**CI workflow:** `.github/workflows/reference-policy-tests.yml`

## Automated Test Set

1. valid D3 baseline → PASS
2. remove second-human confirmation → BLOCK
3. enable execution without scope → BLOCK
4. enable execution without expiry → BLOCK
5. authorize with unresolved critical dissent → BLOCK
6. unknown decision class → BLOCK

## Verification Model

The repository now contains a GitHub Actions workflow that runs the committed test suite when the prototype, specs or workflow itself changes.

A successful CI run establishes only that the encoded reference checks behave as tested.

It does **not** establish:

- production security
- identity verification
- cryptographic authorization
- safe external execution
- full JSON Schema validation
- correctness of the broader SFII architecture

Those require later milestones.

## Claim Boundary

**Tests passing ≠ SFII verified.**

It means only that this narrow prototype behaves consistently with the six currently encoded governance tests.

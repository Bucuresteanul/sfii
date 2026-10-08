# Prototype Verification Record

**Artifact:** `prototype/policy_gate.py`  
**Test suite:** `prototype/test_policy_gate.py`  
**Verification status:** Logic reviewed against the documented baseline; execution evidence should be recorded when tests are run in a repository checkout.

## Expected Test Cases

1. valid D3 baseline → PASS
2. remove second-human confirmation → BLOCK
3. enable execution without scope → BLOCK
4. enable execution without expiry → BLOCK
5. authorize with unresolved critical dissent → BLOCK
6. unknown decision class → BLOCK

## Claim Boundary

Until an execution log from the committed code is preserved, these are test definitions rather than a CI-backed verification claim.

A future milestone should add deterministic automated execution and preserve the result.

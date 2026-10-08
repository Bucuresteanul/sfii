# SFII Reference Prototype

**Status:** Research prototype  
**Language:** Python standard library only  
**External side effects:** None

This prototype tests one narrow governance property:

> Can a proposed decision envelope weaken SFII's baseline controls without being detected?

The answer should be **no** for the cases currently encoded.

---

## What It Does

`policy_gate.py` reads a JSON decision envelope and returns:

- `PASS` when no encoded baseline violation is detected
- `BLOCK` with explicit reasons when the policy is weaker than the baseline

The current gate checks:

- known decision class
- mandatory controls for D2 / D3 / D4
- bounded execution scope
- execution expiry
- unresolved high / critical dissent at authorization time

---

## What It Does Not Do

It does not:

- execute transactions
- authenticate humans
- verify cryptographic signatures
- enforce cooling-off time
- validate device identity
- validate the full JSON Schema
- connect to external services
- prove SFII security
- make a family decision

Those belong to later milestones.

---

## Run

From this directory:

```bash
python policy_gate.py ../specs/example-d3-synthetic.json
```

Expected result:

```text
PASS
No baseline governance violation detected by this reference gate.
```

---

## Tests

```bash
python -m unittest -v test_policy_gate.py
```

The initial test set covers:

- valid D3 baseline
- attempted removal of second-human confirmation
- execution without scope
- execution without expiry
- unresolved critical dissent
- invalid decision class

See [Verification Plan](../docs/VERIFICATION-PLAN.md) for the broader architecture test program.

---

## Security Boundary

A `PASS` means only:

**this small reference gate did not detect one of the governance violations it currently knows how to test.**

It does not mean an action is safe, authorized, correct or production-ready.

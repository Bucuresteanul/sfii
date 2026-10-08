#!/usr/bin/env python3
"""
SFII reference policy gate.

Research prototype only.
It validates whether a decision envelope weakens baseline SFII governance.
It does not execute actions, verify identities, validate cryptographic signatures,
or provide production security guarantees.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


BASELINE_REQUIRED_CONTROLS = {
    "D0": (),
    "D1": (),
    "D2": ("primary_approval",),
    "D3": (
        "primary_approval",
        "second_human",
        "cooling_off_required",
        "trusted_device_required",
    ),
    "D4": (
        "primary_approval",
        "second_human",
        "cooling_off_required",
        "trusted_device_required",
        "multisig_required",
    ),
}


def check_policy(envelope: dict[str, Any]) -> list[str]:
    """Return governance violations. Empty list means the draft policy passes."""

    violations: list[str] = []

    decision_class = envelope.get("decision_class")
    if decision_class not in BASELINE_REQUIRED_CONTROLS:
        return [f"unknown decision_class: {decision_class!r}"]

    approval_policy = envelope.get("approval_policy") or {}

    for control in BASELINE_REQUIRED_CONTROLS[decision_class]:
        if approval_policy.get(control) is not True:
            violations.append(
                f"{decision_class} requires approval_policy.{control}=true"
            )

    execution_policy = envelope.get("execution_policy") or {}

    if execution_policy.get("enabled") is True:
        if not execution_policy.get("scope"):
            violations.append("enabled execution requires non-empty scope")

        if execution_policy.get("expires_at") is None:
            violations.append("enabled execution requires expires_at")

    if envelope.get("status") == "authorized" and decision_class in {"D3", "D4"}:
        for dissent in envelope.get("dissent") or []:
            if (
                dissent.get("severity") in {"high", "critical"}
                and dissent.get("resolved") is not True
            ):
                violations.append(
                    "authorized D3/D4 cannot suppress unresolved "
                    "high/critical dissent"
                )
                break

    return violations


def load_envelope(path: str) -> dict[str, Any]:
    with Path(path).open("r", encoding="utf-8") as handle:
        data = json.load(handle)

    if not isinstance(data, dict):
        raise ValueError("decision envelope must be a JSON object")

    return data


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: python policy_gate.py <decision-envelope.json>", file=sys.stderr)
        return 64

    try:
        envelope = load_envelope(argv[1])
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"BLOCK: invalid envelope: {exc}", file=sys.stderr)
        return 2

    violations = check_policy(envelope)

    if violations:
        print("BLOCK")
        for violation in violations:
            print(f"- {violation}")
        return 2

    print("PASS")
    print("No baseline governance violation detected by this reference gate.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

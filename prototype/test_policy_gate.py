import copy
import unittest

from policy_gate import check_policy


BASE_D3 = {
    "decision_class": "D3",
    "status": "research",
    "approval_policy": {
        "primary_approval": True,
        "second_human": True,
        "cooling_off_required": True,
        "trusted_device_required": True,
        "multisig_required": False,
    },
    "execution_policy": {
        "enabled": False,
        "scope": [],
        "expires_at": None,
    },
    "dissent": [],
}


class PolicyGateTests(unittest.TestCase):
    def test_valid_d3_policy_passes(self):
        self.assertEqual(check_policy(copy.deepcopy(BASE_D3)), [])

    def test_d3_cannot_remove_second_human(self):
        envelope = copy.deepcopy(BASE_D3)
        envelope["approval_policy"]["second_human"] = False

        violations = check_policy(envelope)

        self.assertIn(
            "D3 requires approval_policy.second_human=true",
            violations,
        )

    def test_enabled_execution_requires_scope(self):
        envelope = copy.deepcopy(BASE_D3)
        envelope["execution_policy"]["enabled"] = True
        envelope["execution_policy"]["expires_at"] = "2030-01-01T00:00:00Z"

        violations = check_policy(envelope)

        self.assertIn("enabled execution requires non-empty scope", violations)

    def test_enabled_execution_requires_expiry(self):
        envelope = copy.deepcopy(BASE_D3)
        envelope["execution_policy"]["enabled"] = True
        envelope["execution_policy"]["scope"] = ["synthetic-action"]

        violations = check_policy(envelope)

        self.assertIn("enabled execution requires expires_at", violations)

    def test_authorized_d3_cannot_hide_severe_unresolved_dissent(self):
        envelope = copy.deepcopy(BASE_D3)
        envelope["status"] = "authorized"
        envelope["dissent"] = [
            {
                "source": "red-team",
                "severity": "critical",
                "summary": "Synthetic critical risk",
                "resolved": False,
            }
        ]

        violations = check_policy(envelope)

        self.assertIn(
            "authorized D3/D4 cannot suppress unresolved high/critical dissent",
            violations,
        )

    def test_unknown_decision_class_blocks(self):
        envelope = copy.deepcopy(BASE_D3)
        envelope["decision_class"] = "D9"

        violations = check_policy(envelope)

        self.assertEqual(violations, ["unknown decision_class: 'D9'"])


if __name__ == "__main__":
    unittest.main()

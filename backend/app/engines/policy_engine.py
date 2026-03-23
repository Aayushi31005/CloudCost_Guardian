import yaml
import logging
from typing import List
from app.models.aggregation import AggregatedCost
from app.models.policy import PolicyViolation


logger = logging.getLogger(__name__)

class PolicyEngine:
    def __init__(self, policy_path: str):
        with open(policy_path) as f:
            self.policies = yaml.safe_load(f)
        
    def evaluate(self, aggregation: AggregatedCost) -> List[PolicyViolation]:
        violations = []

        for name, policy in self.policies.items():
            if policy["window"] != aggregation.window:
                continue

            if policy.get("service") != aggregation.service:
                continue

            if aggregation.total_cost > policy["max_cost"]:
                violation = PolicyViolation(
                    policy_name=name,
                    window=aggregation.window,
                    service=aggregation.service,
                    severity=policy["severity"],
                    current_cost=aggregation.total_cost,
                    threshold=policy["max_cost"],
                )
                violations.append(violation)
                logger.warning(
                    "policy_violation_detected",
                    extra=violation.model_dump()
                )
        return violations

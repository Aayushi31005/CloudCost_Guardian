import yaml
import logging
from typing import List
from app.models.aggregation import AggregatedCost
from app.models.policy import PolicyViolation


logger = logging.getLogger(__name__)

class PolicyEngine:
    def __init__(self, policy_path: str):
        self.policy_path = policy_path

    def _load_policies(self):
        with open(self.policy_path, encoding="utf-8") as f:
            return yaml.safe_load(f) or {}
        
    def evaluate(self, aggregation: AggregatedCost, latest_increment: float) -> List[PolicyViolation]:
        violations = []
        policies = self._load_policies()

        for name, policy in policies.items():
            if policy["window"] != aggregation.window:
                continue

            if policy.get("service") != aggregation.service:
                continue

            max_cost = policy["max_cost"]
            warning_ratio = policy.get("warning_ratio", 0.75)
            warning_threshold = max_cost * warning_ratio
            projected_cost = aggregation.total_cost + max(0, latest_increment)

            if aggregation.total_cost >= max_cost:
                violation = PolicyViolation(
                    policy_name=name,
                    window=aggregation.window,
                    period_start=aggregation.period_start,
                    service=aggregation.service,
                    severity=policy["severity"],
                    stage="exceeded",
                    current_cost=aggregation.total_cost,
                    threshold=max_cost,
                    projected_cost=projected_cost,
                )
                violations.append(violation)
                logger.warning(
                    "policy_violation_detected",
                    extra=violation.model_dump()
                )

            elif projected_cost >= max_cost:
                violation = PolicyViolation(
                    policy_name=name,
                    window=aggregation.window,
                    period_start=aggregation.period_start,
                    service=aggregation.service,
                    severity="warning",
                    stage="projected",
                    current_cost=aggregation.total_cost,
                    threshold=max_cost,
                    projected_cost=projected_cost,
                )
                violations.append(violation)
                logger.warning(
                    "policy_projection_warning_detected",
                    extra=violation.model_dump()
                )

            elif aggregation.total_cost >= warning_threshold:
                violation = PolicyViolation(
                    policy_name=name,
                    window=aggregation.window,
                    period_start=aggregation.period_start,
                    service=aggregation.service,
                    severity="warning",
                    stage="approaching",
                    current_cost=aggregation.total_cost,
                    threshold=max_cost,
                    projected_cost=projected_cost,
                )
                violations.append(violation)
                logger.warning(
                    "policy_warning_detected",
                    extra=violation.model_dump()
                )
        return violations

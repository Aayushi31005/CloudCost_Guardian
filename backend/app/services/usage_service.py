from sqlalchemy.orm import Session

from app.engines.alert_engine import AlertEngine
from app.engines.aggregation_engine import CostAggregationEngine
from app.engines.cost_engine import CostEstimationEngine
from app.engines.policy_engine import PolicyEngine
from app.models.usage import UsageCreate
from app.repositories.aggregation_repository import AggregationRepository
from app.repositories.cost_repository import CostRepository
from app.repositories.usage_repository import UsageRepository


alert_engine = AlertEngine()
usage_repo = UsageRepository()
cost_engine = CostEstimationEngine("app/config/pricing.yaml")
cost_repo = CostRepository()
aggregation_engine = CostAggregationEngine()
aggregation_repo = AggregationRepository()
policy_engine = PolicyEngine("app/config/policies.yaml")


def create_usage(_: Session | None, usage: UsageCreate) -> bool:
    created = usage_repo.create(usage)

    if not created:
        return False

    estimate = cost_engine.estimate(usage)
    cost_repo.save(estimate)
    aggregations = aggregation_engine.aggregate(estimate, usage.timestamp)

    for aggregation in aggregations:
        updated_aggregation = aggregation_repo.upsert(aggregation)

        violations = policy_engine.evaluate(
            updated_aggregation,
            latest_increment=aggregation.total_cost,
        )

        for violation in violations:
            alert_engine.emit(violation)

    return True

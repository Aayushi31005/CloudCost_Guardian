import logging
from datetime import datetime
from typing import List
from app.models.cost import CostEstimate
from app.models.aggregation import AggregatedCost

logger = logging.getLogger(__name__)

class CostAggregationEngine:
    def aggregate(self, estimate: CostEstimate) -> List[AggregatedCost]:
        now = datetime.utcnow()
        daily_period = now.strftime("%Y-%m-%d")
        monthly_period = now.strftime("%Y-%m")

        aggregations = [
            AggregatedCost(
                service=estimate.service,
                window="daily_service",
                period_start=daily_period,
                total_cost=estimate.estimated_cost,
            ),
            AggregatedCost(
                service=estimate.service,
                window="monthly_service",
                period_start=monthly_period,
                total_cost=estimate.estimated_cost,
            ),
            AggregatedCost(
                service=None,
                window="monthly_global",
                period_start=monthly_period,
                total_cost=estimate.estimated_cost,
            ),
        ]

        logger.info(
            "aggregation_created",
            extra={"count": len(aggregations)},
        )

        return aggregations

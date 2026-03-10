import logging
from datetime import datetime
from app.models.cost import CostEstimate
from app.models.aggregation import AggregatedCost

logger = logging.getLogger(__name__)

class CostAggregationEngine:
    def aggregate_monthly_service(self, estimate: CostEstimate):
        now = datetime.utcnow()
        period = now.strftime("%Y-%m")

        aggregated = AggregatedCost(
            service=estimate.service,
            window="monthly_service",
            period_start=period,
            total_cost=estimate.estimated_cost,
        )

        logger.info("aggregation_created", extra=aggregated.model_dump())

        return aggregated

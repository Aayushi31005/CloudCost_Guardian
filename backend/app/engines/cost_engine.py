import yaml
import logging
from app.models.cost import CostEstimate

logger = logging.getLogger(__name__)


class CostEstimationEngine:

    def __init__(self, pricing_path: str):
        with open(pricing_path) as f:
            config = yaml.safe_load(f)

        self.pricing = config["pricing"]
        self.version = config["version"]

    def estimate(self, usage):
        rules = self.pricing.get(usage.service)

        if not rules:
            raise ValueError(f"No pricing defined for service {usage.service}")

        billable = max(0, usage.usage_amount - rules.get("free_tier", 0))
        cost = billable * rules["price_per_unit"]

        estimate = CostEstimate(
            usage_id=usage.id,
            service=usage.service,
            estimated_cost=round(cost, 4),
            pricing_version=self.version
        )

        logger.info("cost_estimated", extra=estimate.model_dump())

        return estimate
from fastapi import APIRouter, HTTPException
from app.models.usage import UsageCreate, UsageResponse
from app.repositories.usage_repository import UsageRepository
from app.engines.cost_engine import CostEstimationEngine
from app.repositories.cost_repository import CostRepository
from app.engines.aggregation_engine import CostAggregationEngine
from app.repositories.aggregation_repository import AggregationRepository

router = APIRouter(prefix="/usage", tags=["usage"])

repo = UsageRepository()
cost_engine = CostEstimationEngine("app/config/pricing.yaml")
cost_repo = CostRepository()
aggregation_engine = CostAggregationEngine()
aggregation_repo = AggregationRepository()


@router.post("/", response_model=UsageResponse)
def create_usage(usage: UsageCreate):
    created = repo.create(usage)

    if not created:
        raise HTTPException(
            status_code=409,
            detail="Usage record with this ID already exists.",
        )

    estimate = cost_engine.estimate(usage)
    cost_repo.save(estimate)
    aggregations = aggregation_engine.aggregate(estimate)

    for aggregation in aggregations:
        aggregation_repo.upsert(aggregation)

    return usage

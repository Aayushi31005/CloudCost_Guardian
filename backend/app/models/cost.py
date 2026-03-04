from pydantic import BaseModel


class CostEstimate(BaseModel):
    usage_id: str
    service: str
    estimated_cost: float
    pricing_version: str
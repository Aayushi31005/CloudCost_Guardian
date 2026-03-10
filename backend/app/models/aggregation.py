from pydantic import BaseModel
from typing import Optional

class AggregatedCost(BaseModel):
    service: Optional[str]
    window: str
    period_start: str
    total_cost: float

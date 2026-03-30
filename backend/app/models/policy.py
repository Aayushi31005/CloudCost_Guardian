from typing import Optional

from pydantic import BaseModel


class PolicyViolation(BaseModel):
    policy_name: str
    window: str
    period_start: str
    service: Optional[str]
    severity: str
    stage: str
    current_cost: float
    threshold: float
    projected_cost: Optional[float] = None

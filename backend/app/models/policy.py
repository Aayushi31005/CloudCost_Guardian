from typing import Optional

from pydantic import BaseModel


class PolicyViolation(BaseModel):
    policy_name: str
    window: str
    service: Optional[str]
    severity: str
    current_cost: float
    threshold: float

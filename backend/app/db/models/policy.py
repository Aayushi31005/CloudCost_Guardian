from pydantic import BaseModel
from typing import Optional

class PolicyViolation(BaseModel):
    policy_name: str
    window: str
    service: Optional[str]
    severity: str
    current_cost: float
    threshold: float

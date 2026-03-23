from pydantic import BaseModel
from typing import List


class DashboardSummary(BaseModel):
    monthly_total: float
    daily_total: float


class ServiceCost(BaseModel):
    service: str
    monthly_cost: float


class AlertResponse(BaseModel):
    severity: str
    message: str
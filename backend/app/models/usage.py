from datetime import datetime
from pydantic import BaseModel, Field

class UsageCreate(BaseModel):
    id: str = Field(..., description="Unique usage record ID")
    service: str
    resource_type: str
    usage_amount: float
    unit: str
    timestamp: datetime


class UsageResponse(BaseModel):
    id: str
    service: str
    resource_type: str
    usage_amount: float
    unit: str
    timestamp: datetime

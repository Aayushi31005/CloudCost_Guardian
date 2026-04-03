from pydantic import BaseModel


class CostHistoryPoint(BaseModel):
    period_start: str
    period_label: str
    cost: float

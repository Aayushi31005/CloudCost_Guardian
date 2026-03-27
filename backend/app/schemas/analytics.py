from datetime import date

from pydantic import BaseModel


class DailyCost(BaseModel):
    date: date
    cost: float

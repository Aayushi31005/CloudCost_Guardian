from typing import Literal

from fastapi import APIRouter, Depends, Header
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.analytics import CostHistoryPoint
from app.services.analytics_service import get_cost_history

router = APIRouter(prefix="/analytics", tags=["analytics"])


@router.get("/cost-history", response_model=list[CostHistoryPoint])
def cost_history(
    db: Session = Depends(get_db),
    x_timezone: str | None = Header(default=None),
    granularity: Literal["daily", "weekly", "monthly"] = "daily",
):
    return get_cost_history(db, granularity, x_timezone)

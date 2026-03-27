from fastapi import APIRouter, Depends, Header
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.services.analytics_service import get_daily_costs
from app.schemas.analytics import DailyCost

router = APIRouter(prefix="/analytics", tags=["analytics"])


@router.get("/daily-costs", response_model=list[DailyCost])
def daily_costs(
    db: Session = Depends(get_db),
    x_timezone: str | None = Header(default=None),
):
    return get_daily_costs(db, x_timezone)

from collections import defaultdict
from datetime import timezone
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

from sqlalchemy.orm import Session

from app.db.models.cost import CostEstimateDB
from app.db.models.usage import UsageRecordDB


def get_daily_costs(db: Session, timezone_name: str | None = None):
    try:
        user_timezone = ZoneInfo(timezone_name) if timezone_name else timezone.utc
    except ZoneInfoNotFoundError:
        user_timezone = timezone.utc

    results = (
        db.query(
            UsageRecordDB.timestamp,
            CostEstimateDB.estimated_cost,
        )
        .join(CostEstimateDB, CostEstimateDB.usage_id == UsageRecordDB.id)
        .order_by(UsageRecordDB.timestamp)
        .all()
    )

    daily_totals: dict[str, float] = defaultdict(float)

    for timestamp, estimated_cost in results:
        timestamp_value = (
            timestamp.replace(tzinfo=timezone.utc)
            if timestamp.tzinfo is None
            else timestamp.astimezone(timezone.utc)
        )
        local_date = timestamp_value.astimezone(user_timezone).date().isoformat()
        daily_totals[local_date] += float(estimated_cost)

    return [
        {
            "date": day,
            "cost": cost,
        }
        for day, cost in sorted(daily_totals.items())
    ]

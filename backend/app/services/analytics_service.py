from collections import defaultdict
from datetime import timedelta, timezone
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

from sqlalchemy.orm import Session

from app.db.models.cost import CostEstimateDB
from app.db.models.usage import UsageRecordDB


def _get_user_timezone(timezone_name: str | None):
    try:
        return ZoneInfo(timezone_name) if timezone_name else timezone.utc
    except ZoneInfoNotFoundError:
        return timezone.utc


def _build_period(timestamp_value, user_timezone, granularity: str) -> tuple[str, str]:
    localized_timestamp = timestamp_value.astimezone(user_timezone)

    if granularity == "daily":
        local_date = localized_timestamp.date()
        return local_date.isoformat(), local_date.strftime("%b %d")

    if granularity == "weekly":
        local_date = localized_timestamp.date()
        week_start = local_date - timedelta(days=local_date.weekday())
        iso_year, iso_week, _ = week_start.isocalendar()
        return week_start.isoformat(), f"{iso_year}-W{iso_week:02d}"

    month_start = localized_timestamp.date().replace(day=1)
    return month_start.isoformat(), month_start.strftime("%b %Y")


def get_cost_history(
    db: Session,
    granularity: str = "daily",
    timezone_name: str | None = None,
):
    user_timezone = _get_user_timezone(timezone_name)

    results = (
        db.query(
            UsageRecordDB.timestamp,
            CostEstimateDB.estimated_cost,
        )
        .join(CostEstimateDB, CostEstimateDB.usage_id == UsageRecordDB.id)
        .order_by(UsageRecordDB.timestamp)
        .all()
    )

    history_totals: dict[str, float] = defaultdict(float)
    history_labels: dict[str, str] = {}

    for timestamp, estimated_cost in results:
        timestamp_value = (
            timestamp.replace(tzinfo=timezone.utc)
            if timestamp.tzinfo is None
            else timestamp.astimezone(timezone.utc)
        )
        period_start, period_label = _build_period(timestamp_value, user_timezone, granularity)
        history_totals[period_start] += float(estimated_cost)
        history_labels[period_start] = period_label

    return [
        {
            "period_start": period_start,
            "period_label": history_labels[period_start],
            "cost": cost,
        }
        for period_start, cost in sorted(history_totals.items())
    ]

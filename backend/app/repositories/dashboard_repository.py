from datetime import datetime

from sqlalchemy import func
from app.db.session import SessionLocal
from app.db.models.aggregation import AggregatedCostDB


class DashboardRepository:

    def get_summary(self):
        today_period = datetime.utcnow().strftime("%Y-%m-%d")
        month_period = datetime.utcnow().strftime("%Y-%m")

        db = SessionLocal()

        monthly_total = db.query(func.sum(AggregatedCostDB.total_cost)) \
            .filter(AggregatedCostDB.window == "monthly_global") \
            .filter(AggregatedCostDB.period_start == month_period) \
            .scalar() or 0.0

        daily_total = db.query(func.sum(AggregatedCostDB.total_cost)) \
            .filter(AggregatedCostDB.window == "daily_service") \
            .filter(AggregatedCostDB.period_start == today_period) \
            .scalar() or 0.0

        weekly_total = self._get_weekly_total(db)

        db.close()

        return {
            "monthly_total": round(monthly_total, 4),
            "weekly_total": round(weekly_total, 4),
            "daily_total": round(daily_total, 4)
        }

    def get_service_breakdown(self):
        month_period = datetime.utcnow().strftime("%Y-%m")

        db = SessionLocal()

        rows = db.query(
            AggregatedCostDB.service,
            AggregatedCostDB.total_cost
        ).filter(
            AggregatedCostDB.window == "monthly_service",
            AggregatedCostDB.period_start == month_period,
        ).all()

        db.close()

        return [
            {
                "service": r[0],
                "monthly_cost": round(r[1], 4)
            }
            for r in rows
        ]

    def _get_weekly_total(self, db):
        today = datetime.utcnow().date()
        week_start = today.fromordinal(today.toordinal() - today.weekday())

        week_periods = [
            today.fromordinal(week_start.toordinal() + offset).strftime("%Y-%m-%d")
            for offset in range(7)
        ]

        return db.query(func.sum(AggregatedCostDB.total_cost)) \
            .filter(AggregatedCostDB.window == "daily_service") \
            .filter(AggregatedCostDB.period_start.in_(week_periods)) \
            .scalar() or 0.0

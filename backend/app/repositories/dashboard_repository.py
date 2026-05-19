from datetime import datetime

from sqlalchemy import func
from app.db.session import SessionLocal
from app.db.models.aggregation import AggregatedCostDB


class DashboardRepository:

    def get_summary(self):
        today_period = datetime.utcnow().strftime("%Y-%m-%d")
        month_period = datetime.utcnow().strftime("%Y-%m")

        db = SessionLocal()

        daily_rows = self._get_window_rows(
            db,
            window="daily_service",
            period_starts=[today_period],
        )
        weekly_rows = self._get_window_rows(
            db,
            window="daily_service",
            period_starts=self._get_week_periods(),
        )
        monthly_rows = self._get_window_rows(
            db,
            window="monthly_service",
            period_starts=[month_period],
        )

        db.close()

        return {
            "daily_total": round(daily_rows["total"], 4),
            "daily_ec2_total": round(daily_rows["ec2"], 4),
            "daily_s3_total": round(daily_rows["s3"], 4),
            "weekly_total": round(weekly_rows["total"], 4),
            "weekly_ec2_total": round(weekly_rows["ec2"], 4),
            "weekly_s3_total": round(weekly_rows["s3"], 4),
            "monthly_total": round(monthly_rows["total"], 4),
            "monthly_ec2_total": round(monthly_rows["ec2"], 4),
            "monthly_s3_total": round(monthly_rows["s3"], 4),
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

    def _get_week_periods(self):
        today = datetime.utcnow().date()
        week_start = today.fromordinal(today.toordinal() - today.weekday())

        return [
            today.fromordinal(week_start.toordinal() + offset).strftime("%Y-%m-%d")
            for offset in range(7)
        ]

    def _get_window_rows(self, db, window: str, period_starts: list[str]):
        rows = db.query(
            AggregatedCostDB.service,
            AggregatedCostDB.total_cost,
        ).filter(
            AggregatedCostDB.window == window,
            AggregatedCostDB.period_start.in_(period_starts),
        ).all()

        totals = {
            "total": 0.0,
            "ec2": 0.0,
            "s3": 0.0,
        }

        for service, total_cost in rows:
            amount = float(total_cost)
            totals["total"] += amount

            normalized_service = (service or "").lower()
            if normalized_service in ("ec2", "s3"):
                totals[normalized_service] += amount

        return totals

from sqlalchemy import func
from app.db.session import SessionLocal
from app.db.models.aggregation import AggregatedCostDB


class DashboardRepository:

    def get_summary(self):

        db = SessionLocal()

        monthly_total = db.query(func.sum(AggregatedCostDB.total_cost)) \
            .filter(AggregatedCostDB.window == "monthly_global") \
            .scalar() or 0.0

        daily_total = db.query(func.sum(AggregatedCostDB.total_cost)) \
            .filter(AggregatedCostDB.window == "daily_service") \
            .scalar() or 0.0

        db.close()

        return {
            "monthly_total": round(monthly_total, 4),
            "daily_total": round(daily_total, 4)
        }

    def get_service_breakdown(self):

        db = SessionLocal()

        rows = db.query(
            AggregatedCostDB.service,
            AggregatedCostDB.total_cost
        ).filter(
            AggregatedCostDB.window == "monthly_service"
        ).all()

        db.close()

        return [
            {
                "service": r[0],
                "monthly_cost": round(r[1], 4)
            }
            for r in rows
        ]
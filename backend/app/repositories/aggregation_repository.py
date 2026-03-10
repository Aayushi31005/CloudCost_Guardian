import logging
from app.db.session import SessionLocal
from app.db.models.aggregation import AggregatedCostDB
from app.models.aggregation import AggregatedCost

logger = logging.getLogger(__name__)

class AggregationRepository:
    def upsert(self, aggregation: AggregatedCost):
        db = SessionLocal()

        try:
            existing = db.query(AggregatedCostDB).filter_by(
                service=aggregation.service,
                window=aggregation.window,
                period_start=aggregation.period_start,
            ).first()

            if existing:
                existing.total_cost += aggregation.total_cost
                db.commit()
                logger.info("aggregation_updated")
            else:
                service_key = aggregation.service or "all"
                new_record = AggregatedCostDB(
                    id=f"{aggregation.window}_{service_key}_{aggregation.period_start}",
                    service=aggregation.service,
                    window=aggregation.window,
                    period_start=aggregation.period_start,
                    total_cost=aggregation.total_cost,
                )

                db.add(new_record)
                db.commit()
                logger.info("aggregation_created")

        finally:
            db.close()

import logging
from app.db.session import SessionLocal
from app.db.models.cost import CostEstimateDB
from app.models.cost import CostEstimate

logger = logging.getLogger(__name__)

class CostRepository:
    def save(self, estimate: CostEstimate):
        db = SessionLocal()

        try:
            db_record = CostEstimateDB(
                id=estimate.usage_id,
                usage_id=estimate.usage_id,
                service=estimate.service,
                estimated_cost=estimate.estimated_cost,
                pricing_version=estimate.pricing_version
            )
            db.add(db_record)
            db.commit()

            logger.info("cost_persisted",extra={"usage_id":estimate.usage_id})
        
        finally:
            db.close()

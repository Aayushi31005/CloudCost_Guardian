import logging
from datetime import datetime, timezone

from sqlalchemy import func
from sqlalchemy.exc import IntegrityError
from app.db.session import SessionLocal
from app.db.models.usage import UsageRecordDB
from app.models.usage import UsageCreate

logger = logging.getLogger(__name__)

class UsageRepository:

    def create(self, usage: UsageCreate) -> bool:
        db = SessionLocal()

        try:
            db_record = UsageRecordDB(**usage.model_dump())
            db.add(db_record)
            db.commit()
            logger.info("usage_created", extra={"usage_id": usage.id})
            return True
        except IntegrityError:
            db.rollback()
            logger.info("usage_duplicate", extra={"usage_id": usage.id})
            return False
        finally:
            db.close()

    def get_cumulative_usage_before(self, service: str, timestamp: datetime) -> float:
        db = SessionLocal()

        try:
            timestamp_utc = (
                timestamp.replace(tzinfo=timezone.utc)
                if timestamp.tzinfo is None
                else timestamp.astimezone(timezone.utc)
            )
            period_start = timestamp_utc.replace(day=1, hour=0, minute=0, second=0, microsecond=0)

            return db.query(func.sum(UsageRecordDB.usage_amount)).filter(
                UsageRecordDB.service == service,
                UsageRecordDB.timestamp >= period_start,
                UsageRecordDB.timestamp < timestamp,
            ).scalar() or 0.0
        finally:
            db.close()

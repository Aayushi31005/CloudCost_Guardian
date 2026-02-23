import logging
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

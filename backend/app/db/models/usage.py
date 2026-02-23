from sqlalchemy import Column, DateTime, Float, String
from app.db.base import Base


class UsageRecordDB(Base):
    __tablename__ = "usage_records"

    id = Column(String, primary_key=True, index=True)
    service = Column(String, nullable=False)
    resource_type = Column(String, nullable=False)
    usage_amount = Column(Float, nullable=False)
    unit = Column(String, nullable=False)
    timestamp = Column(DateTime, nullable=False)

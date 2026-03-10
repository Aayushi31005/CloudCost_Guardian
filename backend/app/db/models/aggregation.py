from sqlalchemy import Column, String, Float, UniqueConstraint
from app.db.base import Base

class AggregatedCostDB(Base):
    __tablename__ = "aggregated_costs"

    id = Column(String, primary_key=True)
    service = Column(String, nullable=True)
    window = Column(String, nullable=False)
    period_start = Column(String, nullable=False)
    total_cost = Column(Float, nullable=False)

    __table_args__ = (
        UniqueConstraint("service", "window", "period_start"),
    )

from sqlalchemy import Column, String, Float
from app.db.base import Base


class CostEstimateDB(Base):
    __tablename__ = "cost_estimates"

    id = Column(String, primary_key=True)
    usage_id = Column(String, unique=True, nullable=False)
    service = Column(String, nullable=False)
    estimated_cost = Column(Float, nullable=False)
    pricing_version = Column(String, nullable=False)
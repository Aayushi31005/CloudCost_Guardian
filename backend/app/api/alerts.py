from fastapi import APIRouter
from app.repositories.alert_repository import AlertRepository
from app.services.usage_service import alert_engine

router = APIRouter(prefix="/alerts", tags=["alerts"])

repo = AlertRepository(alert_engine)


@router.get("/")
def get_alerts():
    return repo.get_active_alerts()

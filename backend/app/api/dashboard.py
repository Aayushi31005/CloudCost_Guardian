from fastapi import APIRouter
from app.repositories.dashboard_repository import DashboardRepository

router = APIRouter(prefix="/dashboard", tags=["dashboard"])

repo = DashboardRepository()


@router.get("/summary")
def get_summary():
    return repo.get_summary()


@router.get("/services")
def get_services():
    return repo.get_service_breakdown()
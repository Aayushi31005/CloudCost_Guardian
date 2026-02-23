from fastapi import APIRouter, HTTPException
from app.models.usage import UsageCreate, UsageResponse
from app.repositories.usage_repository import UsageRepository


router = APIRouter(prefix="/usage",tags=["usage"])

repo = UsageRepository()

@router.post("/", response_model= UsageResponse)
def create_usage(usage: UsageCreate):
    created = repo.create(usage)

    if not created:
        raise HTTPException(
            status_code=409,
            detail="Usage record with  this ID already exists."
        )
    return usage
from fastapi import APIRouter, HTTPException
from app.models.usage import UsageCreate, UsageResponse
from app.services.usage_service import create_usage as ingest_usage
router = APIRouter(prefix="/usage", tags=["usage"])

@router.post("/", response_model=UsageResponse)
def create_usage(usage: UsageCreate):
    created = ingest_usage(None, usage)
    if not created:
        raise HTTPException(
            status_code=409,
            detail="Usage record with this ID already exists.",
        )

    return usage

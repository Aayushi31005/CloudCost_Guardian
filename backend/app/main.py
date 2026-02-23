from fastapi import FastAPI
from app.core.logging import setup_logging
from app.db.init_db import init_db
from app.api.health import router as health_router
from app.api.usage import router as usage_router

setup_logging()

app= FastAPI(title="CloudCost Guardian")

init_db()

app.include_router(health_router)
app.include_router(usage_router)
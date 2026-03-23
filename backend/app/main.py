from fastapi import FastAPI
from app.core.logging import setup_logging
from app.db.init_db import init_db
from app.api.health import router as health_router
from app.api.usage import router as usage_router
from app.api.dashboard import router as dashboard_router
from app.api.alerts import router as alerts_router


setup_logging()

app= FastAPI(title="CloudCost Guardian")

init_db()

app.include_router(health_router)
app.include_router(usage_router)
app.include_router(dashboard_router)
app.include_router(alerts_router)
import threading

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.logging import setup_logging
from app.db.init_db import init_db
from app.api.health import router as health_router
from app.api.usage import router as usage_router
from app.api.dashboard import router as dashboard_router
from app.api.alerts import router as alerts_router
from app.api.routes import simulator
from app.api.routes.analytics import router as analytics_router
from app.services.simulator import simulator_loop

setup_logging()

app = FastAPI(title="CloudCost Guardian")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

init_db()

@app.on_event("startup")
def start_simulator():
    thread = threading.Thread(target=simulator_loop, daemon=True)
    thread.start()

app.include_router(health_router)
app.include_router(usage_router)
app.include_router(dashboard_router)
app.include_router(alerts_router)
app.include_router(simulator.router)
app.include_router(analytics_router)

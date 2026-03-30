from fastapi import APIRouter
from app.services import simulator

router = APIRouter(prefix="/simulator", tags=["simulator"])


@router.post("/start")
def start_simulator():
    simulator.RUNNING = True
    return {"status": "simulator started"}


@router.post("/stop")
def stop_simulator():
    simulator.RUNNING = False
    return {"status": "simulator stopped"}


@router.get("/status")
def simulator_status():
    return {"running": simulator.RUNNING}
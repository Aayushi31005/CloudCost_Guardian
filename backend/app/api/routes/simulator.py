from fastapi import APIRouter
from app.services import simulator

router = APIRouter(prefix="/simulator", tags=["simulator"])


@router.post("/start")
def start_simulator(service: str | None = None):
    return simulator.start_simulator(service)


@router.post("/stop")
def stop_simulator():
    return simulator.stop_simulator()


@router.get("/status")
def simulator_status():
    return simulator.get_simulator_status()

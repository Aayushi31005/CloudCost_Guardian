import random
import threading
import time
from datetime import datetime
import logging

from app.models.usage import UsageCreate
from app.services.usage_service import create_usage

logger = logging.getLogger(__name__)

RUNNING = False
SIMULATOR_THREAD: threading.Thread | None = None
THREAD_LOCK = threading.Lock()
SIMULATION_INTERVAL_SECONDS = 5
SELECTED_SERVICE = "ec2"


def generate_usage():
    service = SELECTED_SERVICE or random.choice(["ec2", "s3"])

    return {
        "id": f"sim_{int(time.time() * 1000)}",
        "service": service,
        "resource_type": "t3.micro",
        "usage_amount": random.randint(50, 200),
        "unit": "hour",
        "timestamp": datetime.utcnow(),
    }


def simulator_loop():
    while True:
        if RUNNING:
            try:
                usage = UsageCreate(**generate_usage())
                create_usage(None, usage)
                logger.info("simulator_usage_generated", extra={"service": usage.service, "usage_id": usage.id})
            except Exception:
                logger.exception("simulator_loop_iteration_failed")

        time.sleep(SIMULATION_INTERVAL_SECONDS)


def ensure_simulator_thread() -> None:
    global SIMULATOR_THREAD

    with THREAD_LOCK:
        if SIMULATOR_THREAD and SIMULATOR_THREAD.is_alive():
            return

        SIMULATOR_THREAD = threading.Thread(target=simulator_loop, daemon=True)
        SIMULATOR_THREAD.start()


def start_simulator(service: str | None = None) -> dict[str, str]:
    global RUNNING, SELECTED_SERVICE

    ensure_simulator_thread()
    if service not in (None, ""):
        SELECTED_SERVICE = service
    RUNNING = True
    return {"status": "simulator started"}


def stop_simulator() -> dict[str, str]:
    global RUNNING

    RUNNING = False
    return {"status": "simulator stopped"}


def get_simulator_status() -> dict[str, bool | str]:
    if RUNNING and (SIMULATOR_THREAD is None or not SIMULATOR_THREAD.is_alive()):
        ensure_simulator_thread()

    return {
        "running": RUNNING,
        "selected_service": SELECTED_SERVICE,
    }

import random
import threading
import time
from datetime import datetime

from app.models.usage import UsageCreate
from app.services.usage_service import create_usage

RUNNING = False
SIMULATOR_THREAD: threading.Thread | None = None
THREAD_LOCK = threading.Lock()
SIMULATION_INTERVAL_SECONDS = 5


def generate_usage():
    return {
        "id": f"sim_{int(time.time() * 1000)}",
        "service": random.choice(["ec2", "s3"]),
        "resource_type": "t3.micro",
        "usage_amount": random.randint(50, 200),
        "unit": "hour",
        "timestamp": datetime.utcnow(),
    }


def simulator_loop():
    while True:
        if RUNNING:
            usage = UsageCreate(**generate_usage())
            create_usage(None, usage)

            print(f"[SIMULATOR] {usage}")

        time.sleep(SIMULATION_INTERVAL_SECONDS)


def ensure_simulator_thread() -> None:
    global SIMULATOR_THREAD

    with THREAD_LOCK:
        if SIMULATOR_THREAD and SIMULATOR_THREAD.is_alive():
            return

        SIMULATOR_THREAD = threading.Thread(target=simulator_loop, daemon=True)
        SIMULATOR_THREAD.start()


def start_simulator() -> dict[str, str]:
    global RUNNING

    ensure_simulator_thread()
    RUNNING = True
    return {"status": "simulator started"}


def stop_simulator() -> dict[str, str]:
    global RUNNING

    RUNNING = False
    return {"status": "simulator stopped"}


def get_simulator_status() -> dict[str, bool]:
    return {"running": RUNNING}

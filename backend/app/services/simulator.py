import random
import time
from datetime import datetime
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.models.usage import UsageCreate
from app.services.usage_service import create_usage

RUNNING = False  # global control


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
    global RUNNING
    db: Session = SessionLocal()

    while True:
        if RUNNING:
            usage = UsageCreate(**generate_usage())
            create_usage(db, usage)

            print(f"[SIMULATOR] {usage}")

        time.sleep(5)

from pathlib import Path

import yaml
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(tags=["budget"])

POLICY_FILE = Path("app/config/policies.yaml")
DAILY_POLICY_KEY = "daily_ec2_limit"
MONTHLY_POLICY_KEY = "monthly_global_limit"


class BudgetConfig(BaseModel):
    daily_limit: float
    monthly_limit: float


def load_policies() -> dict:
    with POLICY_FILE.open("r", encoding="utf-8") as file:
        return yaml.safe_load(file) or {}


def save_policies(data: dict) -> None:
    with POLICY_FILE.open("w", encoding="utf-8") as file:
        yaml.safe_dump(data, file, sort_keys=False)


@router.get("/budget", response_model=BudgetConfig)
def get_budget() -> BudgetConfig:
    data = load_policies()

    return BudgetConfig(
        daily_limit=float(data.get(DAILY_POLICY_KEY, {}).get("max_cost", 0)),
        monthly_limit=float(data.get(MONTHLY_POLICY_KEY, {}).get("max_cost", 0)),
    )


@router.post("/budget", response_model=BudgetConfig)
def update_budget(config: BudgetConfig) -> BudgetConfig:
    data = load_policies()

    data.setdefault(DAILY_POLICY_KEY, {})["max_cost"] = config.daily_limit
    data.setdefault(MONTHLY_POLICY_KEY, {})["max_cost"] = config.monthly_limit

    save_policies(data)
    return config

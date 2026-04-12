from pathlib import Path

import yaml
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(tags=["budget"])

POLICY_FILE = Path("app/config/policies.yaml")


class BudgetConfig(BaseModel):
    service: str
    daily_limit: float
    monthly_limit: float


def load_policies() -> dict:
    with POLICY_FILE.open("r", encoding="utf-8") as file:
        return yaml.safe_load(file) or {}


def save_policies(data: dict) -> None:
    with POLICY_FILE.open("w", encoding="utf-8") as file:
        yaml.safe_dump(data, file, sort_keys=False)


def get_policy_keys(service: str) -> tuple[str, str]:
    normalized_service = service.lower()
    return (
        f"daily_{normalized_service}_limit",
        f"monthly_{normalized_service}_limit",
    )


@router.get("/budget", response_model=BudgetConfig)
def get_budget(service: str = "ec2") -> BudgetConfig:
    data = load_policies()
    daily_policy_key, monthly_policy_key = get_policy_keys(service)

    return BudgetConfig(
        service=service,
        daily_limit=float(data.get(daily_policy_key, {}).get("max_cost", 0)),
        monthly_limit=float(data.get(monthly_policy_key, {}).get("max_cost", 0)),
    )


@router.post("/budget", response_model=BudgetConfig)
def update_budget(config: BudgetConfig) -> BudgetConfig:
    data = load_policies()
    daily_policy_key, monthly_policy_key = get_policy_keys(config.service)

    data.setdefault(daily_policy_key, {
        "window": "daily_service",
        "service": config.service,
        "warning_ratio": 0.75,
        "severity": "warning",
    })["max_cost"] = config.daily_limit

    data.setdefault(monthly_policy_key, {
        "window": "monthly_service",
        "service": config.service,
        "warning_ratio": 0.75,
        "severity": "warning",
    })["max_cost"] = config.monthly_limit

    save_policies(data)
    return config

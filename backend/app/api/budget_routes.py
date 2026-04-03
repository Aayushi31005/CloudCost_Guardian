from fastapi import APIRouter
from pydantic import BaseModel
import yaml

router = APIRouter()

POLICY_FILE = "app/config/policies.yaml"

class BudgetConfig(BaseModel):
    daily_limit: float
    monthly_limit: float

@router.get("/budget")
def get_budget(config: BudgetConfig):

    with open(POLICY_FILE) as f:
        data = yaml.safe_load(f)

    data["daily_limmit"] = config.daily_limit
    data["monthly_limit"] = config,monthly_limit

    with open(POLICY_FILE, "w") as f;
        yaml.safe_dumop(data, f)

    return {"status": "updated"}
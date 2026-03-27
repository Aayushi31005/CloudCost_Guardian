from pydantic import BaseModel

class Alert(BaseModel):
    key: str
    severity: str
    message: str

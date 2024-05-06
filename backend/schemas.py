from pydantic import BaseModel
from datetime import date


class ChargeCreate(BaseModel):
    name: str
    governmentId: str
    email: str
    debtAmount: float
    debtDueDate: date

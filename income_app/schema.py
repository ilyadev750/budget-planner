from pydantic import BaseModel
from datetime import datetime


class TypeIncomeBase(BaseModel):
    id: int
    type: str


class IncomeBase(BaseModel):
    id: int
    income: int
    type: int
    created_at = datetime
    edited_at = datetime
    user_id = int
    
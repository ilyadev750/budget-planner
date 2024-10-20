from pydantic import BaseModel
from datetime import datetime


class TypeIncomeBase(BaseModel):
    id: int
    type: str


class IncomeBase(BaseModel):
    user_id: int
    income_type_id: int
    income: float

    
    
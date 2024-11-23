from sqlalchemy import (Column,
                        ForeignKey,
                        Integer,
                        String,
                        DateTime,
                        Float)
from sqlalchemy.orm import relationship
import datetime
from db.database import Base


class TypeIncome(Base):
    __tablename__ = "income_types"
    id = Column(Integer, primary_key=True)
    type = Column(String, unique=True)
    incomes = relationship("Income", back_populates="type_income")


class Income(Base):
    __tablename__ = "incomes"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    income_type_id = Column(Integer, ForeignKey("income_types.id"))
    income = Column(Float)
    created_at = Column(DateTime(timezone=True),
                        default=datetime.datetime.now())
    edited_at = Column(DateTime(timezone=True),
                       default=datetime.datetime.now())
    type_income = relationship("TypeIncome", back_populates="incomes")

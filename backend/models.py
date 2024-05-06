from sqlalchemy import Column, Integer, String, Float, Date
from database import Base


class Charge(Base):
    __tablename__ = "charges"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    government_id = Column(String, index=True)
    email = Column(String, index=True)
    debt_amount = Column(Float)
    debt_due_date = Column(Date)

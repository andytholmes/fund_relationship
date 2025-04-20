from sqlalchemy import Column, Integer, String, Float, Date
from .database import Base

class FundPosition(Base):
    __tablename__ = "fund_positions"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=False)
    fund_name = Column(String, nullable=False)
    security_id = Column(String, nullable=False)
    security_name = Column(String, nullable=False)
    position_type = Column(String, nullable=False)
    quantity = Column(Float)
    market_value = Column(Float)
    currency = Column(String)
    sector = Column(String)
    country = Column(String) 
from sqlalchemy import Column, Integer, String, Numeric, DateTime
from sqlalchemy.sql import func

from database import Base


class Card(Base):
    __tablename__ = "cards_card"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    card_type = Column(String(10), nullable=False)
    masked_card = Column(String(19), nullable=False)
    last_four = Column(String(4), nullable=False)
    card_holder_name = Column(String(100), nullable=False)
    expiry_month = Column(Integer, nullable=False)
    expiry_year = Column(Integer, nullable=False)
    created_at = Column(DateTime, server_default=func.now())


class Transaction(Base):
    __tablename__ = "transactions_transaction"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    card_id = Column(Integer, nullable=False)
    amount = Column(Numeric(10, 2), nullable=False)
    status = Column(String(10), default="PENDING")
    transaction_reference = Column(
        String(100),
        unique=True,
        nullable=False
    )
    created_at = Column(DateTime, server_default=func.now())
from sqlalchemy import Column, DateTime, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import relationship

from .meta import Base

class Receipt(Base):
    __tablename__ = 'receipts'

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('users.id'), nullable=False, index=True)
    type = Column(String(255, 'utf8mb4_unicode_ci'), nullable=False)
    created_at = Column(DateTime, nullable=False)
    amount_balance = Column(Numeric(10, 2), nullable=False)
    amount_guarantee = Column(Numeric(10, 2), nullable=False)

    user = relationship('User')

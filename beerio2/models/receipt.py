import factory
import factory.fuzzy

from sqlalchemy_defaults import Column
from sqlalchemy import DateTime, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import relationship

from datetime import datetime

from .meta import Base

class Receipt(Base):
    __tablename__ = 'receipts'

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('users.id'), nullable=False)
    type = Column(String(255))
    created_at = Column(DateTime, auto_now=True, nullable=False)
    amount_balance = Column(Numeric(10, 2), nullable=False)
    amount_guarantee = Column(Numeric(10, 2), nullable=False)

    user = relationship('User', backref='receipts')

class ReceiptFactory(factory.Factory):

    class Meta:
        model = Receipt

    created_at = factory.fuzzy.FuzzyNaiveDateTime(datetime(2015, 1, 1))
    type = "Bar"
    amount_balance = 0
    amount_guarantee = 0

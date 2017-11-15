import factory

from sqlalchemy_defaults import Column
from sqlalchemy import DateTime, Integer

from .meta import Base

class Purchase(Base):
    __lazy_options__ = {}
    __tablename__ = 'purchases'

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, auto_now=True,nullable=False)

class PurchaseFactory(factory.Factory):

    class Meta:
        model = Purchase

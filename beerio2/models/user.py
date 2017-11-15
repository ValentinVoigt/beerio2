import factory
import factory.fuzzy

from sqlalchemy_defaults import Column
from sqlalchemy import DateTime, Integer, Numeric, String

from datetime import datetime

from .meta import Base

class User(Base):
    __lazy_options__ = {}
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    email = Column(String(255))
    created_at = Column(DateTime, auto_now=True, nullable=False)
    room = Column(Integer)
    active = Column(Integer, nullable=False)
    balance = Column(Numeric(10, 2), nullable=False)
    guarantee = Column(Numeric(10, 2), nullable=False)

    def add_receipt(self, receipt):
        receipt.user = self
        self.balance += receipt.amount_balance
        self.guarantee += receipt.amount_guarantee

class UserFactory(factory.Factory):

    class Meta:
        model = User

    created_at = factory.fuzzy.FuzzyNaiveDateTime(datetime(2013, 1, 1))
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')
    balance = 0
    guarantee = 0
    active = True

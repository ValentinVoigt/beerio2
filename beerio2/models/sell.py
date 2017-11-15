from sqlalchemy_defaults import Column
from sqlalchemy import DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship

from .meta import Base

from pyramid.decorator import reify

class Sell(Base):
    __lazy_options__ = {}
    __tablename__ = 'sells'

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, nullable=False)
    user_id = Column(ForeignKey('users.id'), nullable=False, index=True)

    user = relationship('User', backref='sells')

    @reify
    def price(self):
        return sum([p.price for p in self.sell_products])

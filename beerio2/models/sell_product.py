import factory

from sqlalchemy_defaults import Column
from sqlalchemy import ForeignKey, Integer, Numeric
from sqlalchemy.orm import relationship

from decimal import Decimal

from .meta import Base

class SellProduct(Base):
    __lazy_options__ = {}
    __tablename__ = 'sell_products'

    id = Column(Integer, primary_key=True)
    sell_id = Column(ForeignKey('sells.id'), nullable=False)
    product_id = Column(ForeignKey('products.id'), nullable=False)
    num_bottles = Column(Integer, nullable=False)
    price = Column(Numeric(10, 2), nullable=False)

    product = relationship('Product')
    sell = relationship('Sell', backref='sell_products')

class SellProductFactory(factory.Factory):

    class Meta:
        model = SellProduct

    price = factory.Iterator([
        Decimal("0.99"),
        Decimal("1.84"),
        Decimal("0.70"),
    ])

import factory
import factory.fuzzy

from sqlalchemy_defaults import Column
from sqlalchemy import ForeignKey, Integer, Numeric
from sqlalchemy.orm import relationship

from decimal import Decimal

from .meta import Base

class PurchaseProduct(Base):
    __tablename__ = 'purchase_products'

    id = Column(Integer, primary_key=True)
    purchase_id = Column(ForeignKey('purchases.id'), nullable=False)
    product_id = Column(ForeignKey('products.id'), nullable=False)
    num_bottles = Column(Integer, nullable=False)
    num_crates = Column(Integer, nullable=False)
    all_bottles_price = Column(Numeric(10, 2), nullable=False)
    crate_deposit = Column(Numeric(10, 2), nullable=False)
    bottle_deposit = Column(Numeric(10, 2), nullable=False)

    product = relationship('Product')
    purchase = relationship('Purchase')

class PurchaseProductFactory(factory.Factory):

    class Meta:
        model = PurchaseProduct

    num_bottles = factory.Iterator([12, 20])
    num_crates = factory.Iterator([1, 2, 3])
    all_bottles_price = factory.fuzzy.FuzzyDecimal(4, 10)
    crate_deposit = Decimal("1.50")
    bottle_deposit =factory.Iterator([
        Decimal("0.15"),
        Decimal("0.25"),
    ])

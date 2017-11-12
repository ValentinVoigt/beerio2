from sqlalchemy import Column, ForeignKey, Integer, Numeric
from sqlalchemy.orm import relationship

from .meta import Base

class PurchaseProduct(Base):
    __tablename__ = 'purchase_products'

    id = Column(Integer, primary_key=True)
    purchase_id = Column(ForeignKey('purchases.id'), nullable=False, index=True)
    product_id = Column(ForeignKey('products.id'), nullable=False, index=True)
    num_bottles = Column(Integer, nullable=False)
    num_crates = Column(Integer, nullable=False)
    bottle_price = Column(Numeric(10, 2), nullable=False)
    crate_deposit = Column(Numeric(10, 2), nullable=False)
    bottle_deposit = Column(Numeric(10, 2), nullable=False)

    product = relationship('Product')
    purchase = relationship('Purchase')

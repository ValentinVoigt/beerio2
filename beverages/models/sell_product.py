from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from .meta import Base

class SellProduct(Base):
    __tablename__ = 'sell_products'

    id = Column(Integer, primary_key=True)
    sell_id = Column(ForeignKey('sells.id'), nullable=False, index=True)
    product_id = Column(ForeignKey('products.id'), nullable=False, index=True)
    num_bottles = Column(Integer, nullable=False)

    product = relationship('Product')
    sell = relationship('Sell')

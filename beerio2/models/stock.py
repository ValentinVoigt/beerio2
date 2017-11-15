from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from .meta import Base

class Stock(Base):
    __tablename__ = 'stocks'

    id = Column(Integer, primary_key=True)
    stocktaking_id = Column(ForeignKey('stocktakings.id'), nullable=False, index=True)
    product_id = Column(ForeignKey('products.id'), nullable=False, index=True)
    num_bottles = Column(Integer, nullable=False)
    num_crates = Column(Integer, nullable=False)

    product = relationship('Product')
    stocktaking = relationship('Stocktaking')

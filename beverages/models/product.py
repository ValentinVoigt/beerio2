from sqlalchemy import Column, Integer, LargeBinary, String

from .meta import Base

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, info={'label': "Name"})
    company = Column(String(255))
    volume_ml = Column(Integer)
    picture = Column(LargeBinary)

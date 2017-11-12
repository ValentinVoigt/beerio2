from sqlalchemy import Column, Integer, LargeBinary, String

from .meta import Base

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String(255, 'utf8mb4_unicode_ci'), nullable=False)
    company = Column(String(255, 'utf8mb4_unicode_ci'))
    volume_ml = Column(Integer)
    picture = Column(LargeBinary)

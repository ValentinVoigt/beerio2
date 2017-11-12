from sqlalchemy import Column, DateTime, Integer, Numeric, String

from .meta import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(255, 'utf8mb4_unicode_ci'), nullable=False)
    last_name = Column(String(255, 'utf8mb4_unicode_ci'), nullable=False)
    email = Column(String(255, 'utf8mb4_unicode_ci'), nullable=False)
    created_at = Column(DateTime, nullable=False)
    room = Column(Integer)
    active = Column(Integer, nullable=False)
    balance = Column(Numeric(10, 2), nullable=False)
    guarantee = Column(Numeric(10, 2), nullable=False)

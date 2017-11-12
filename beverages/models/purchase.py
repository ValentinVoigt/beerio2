from sqlalchemy import Column, DateTime, Integer

from .meta import Base

class Purchase(Base):
    __tablename__ = 'purchases'

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, nullable=False)

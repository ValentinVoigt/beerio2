from sqlalchemy import Column, DateTime, Integer

from .meta import Base

class Stocktaking(Base):
    __tablename__ = 'stocktakings'

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, nullable=False)

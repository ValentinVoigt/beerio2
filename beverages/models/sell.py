from sqlalchemy import Column, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship

from .meta import Base

class Sell(Base):
    __tablename__ = 'sells'

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, nullable=False)
    user_id = Column(ForeignKey('users.id'), nullable=False, index=True)

    user = relationship('User')

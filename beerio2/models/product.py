import factory
import factory.fuzzy

from sqlalchemy_defaults import Column
from sqlalchemy import Integer, LargeBinary, String

from .meta import Base

class Product(Base):
    __lazy_options__ = {}
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, label="Name")
    company = Column(String(255), nullable=True, label="Hersteller")
    volume_ml = Column(Integer, label="Volumen in ml")
    picture_url = Column(String(255), nullable=True)

class ProductFactory(factory.Factory):

    class Meta:
        model = Product

    name = factory.Faker('bs')
    company = factory.Faker('company')
    volume_ml = factory.Iterator([500, 1000])
    picture_url = factory.Faker('image_url', width=150, height=150)

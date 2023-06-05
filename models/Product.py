from sqlalchemy import Column,Integer, String, Float

from config.database import Base


class Pruduct(Base):

    __tablename__ = "Product"

    id = Column(Integer,primary_key = True)
    name = Column(String)
    brand = Column(String)
    description = Column(String)
    price = Column(Float)
    entry_date = Column(Integer)
    availability  = Column(String)
    available_quantity = Column(Integer)
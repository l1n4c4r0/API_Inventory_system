from sqlalchemy import Column,Integer, String, Float
from config.database import Base

class SupplierModel(Base):

    __tablename__ = "supplier"
    id = Column(Integer,primary_key = True)
    name = Column(String)
    addrees = Column(String)
    phone = Column(Integer)
    email = Column(String)
from tokenize import String
from database import Base
from sqlalchemy import Column, Integer,String

class Address(Base):
    __tablename__="address"

    id = Column(Integer,primary_key=True,nullable=False)
    user=Column(String,nullable=False)
    address = Column(String,nullable=False)

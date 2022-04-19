from sqlalchemy import Column, Integer, PickleType, String
from db.index import Base

class Unique_Eliza(Base):
  id = Column(Integer, primary_key=True)
  eliza = Column(PickleType())
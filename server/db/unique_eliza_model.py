from sqlalchemy import Column, Integer, PickleType, String, ForeignKey
from db.index import Base


class Unique_Eliza(Base):
    __tablename__ = 'unique_eliza'
    id = Column(Integer, primary_key=True)
    eliza = Column(PickleType())
    user_id = Column(Integer, ForeignKey('users.id'))

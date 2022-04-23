from sqlalchemy import Column, Integer, PickleType, String, ForeignKey
from sqlalchemy.orm import relationship
from db.index import Base


class Unique_Eliza(Base):
    __tablename__ = 'unique_eliza'
    id = Column(Integer, primary_key=True)
    eliza = Column(PickleType())
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="users_eliza")

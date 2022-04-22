from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from flask_login import UserMixin
from db.index import Base


class User(UserMixin, Base):

    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    password = Column(String(80), unique=False)
    name = Column(String(18), unique=False)
    children = relationship('Unique_Eliza', back_populates='users')

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User {self.username!r}>'

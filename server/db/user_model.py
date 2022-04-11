from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import mapper
from db.index import metadata, db_session


class User(object):
    query = db_session.query_property()

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User {self.username!r}>'


users = Table('users', metadata,
              Column('id', Integer, primary_key=True),
              Column('username', String(50), unique=True),
              Column('password', String(50), unique=False),
              Column('name', String(32), unique=False)
              )

mapper(User, users)

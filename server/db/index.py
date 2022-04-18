from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os.environ as env

database_config = 'postgresql://' + \
    env.get('POSTGRES_USER') + ":" + env.get('')

engine = create_engine(
    "postgresql://mindspaceuser:mindspaceapp@db:5432/mindspacedb"
)

db_session = scoped_session(sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
))

Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    # import models
    import db.user_model
    Base.metadata.create_all(bind=engine)

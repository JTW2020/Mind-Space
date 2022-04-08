from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(
    "postgresql://mindspaceuser:mindspaceapp@db:5432/mindspacedb")
metadata = MetaData()
db_session = scoped_session(sessionmaker(
    autocommit=False, autoflush=False, bind=engine))


def init_db():
    metadata.create_all(bind=engine)

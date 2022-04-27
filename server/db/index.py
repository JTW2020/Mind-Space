import os
import sys

from sqlalchemy import create_engine, select
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from Eliza.countReassemblies import countReassembliesVal
print(os.environ.get("POSTGRES_USER"),file=sys.stderr)

engine = create_engine(
    f'postgresql://{os.environ.get("POSTGRES_USER")}:{os.environ.get("POSTGRES_PASSWORD")}@{os.environ.get("POSTGRES_HOST")}:{os.environ.get("POSTGRES_PORT")}/{os.environ.get("POSTGRES_DB")}'
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
    import db.unique_eliza_model
    import db.disorder_reassembly_rating_model
    import db.depression_reassembly_rating_model
    import db.anxiety_reassembly_rating_model
    import db.anger_reassembly_rating_model
    import db.inbetween_reassembly_rating_model
    Base.metadata.create_all(bind=engine)

    # All lines afterwards will prefill ratings tables with just 1 rating

    if db_session.execute(select(db.inbetween_reassembly_rating_model.InBetweenReassemblyRatings)).fetchone() == None:
        for i in range(countReassembliesVal('Eliza/inbetween.txt')):
            db_session.add(db.inbetween_reassembly_rating_model.InBetweenReassemblyRatings(reassembly_rule_index=i))
    if db_session.execute(select(db.disorder_reassembly_rating_model.DisorderReassemblyRatings)).fetchone() == None:
        for i in range(countReassembliesVal('Eliza/disorder.txt')):
            db_session.add(db.disorder_reassembly_rating_model.DisorderReassemblyRatings(reassembly_rule_index=i))
    
    if db_session.execute(select(db.depression_reassembly_rating_model.DepressionReassemblyRatings)).fetchone() == None:
        for i in range(countReassembliesVal('Eliza/depressed.txt')):
            db_session.add(db.depression_reassembly_rating_model.DepressionReassemblyRatings(reassembly_rule_index=i))

    if db_session.execute(select(db.anxiety_reassembly_rating_model.AnxietyReassemblyRatings)).fetchone() == None:
        for i in range(countReassembliesVal('Eliza/anxious.txt')):
            db_session.add(db.anxiety_reassembly_rating_model.AnxietyReassemblyRatings(reassembly_rule_index=i))
    if db_session.execute(select(db.anger_reassembly_rating_model.AngerReassemblyRatings)).fetchone() == None:
        for i in range(countReassembliesVal('Eliza/anger.txt')):
            db_session.add(db.anger_reassembly_rating_model.AngerReassemblyRatings(reassembly_rule_index=i))
    db_session.commit()

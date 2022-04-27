from sqlalchemy import Column, Integer, String, select
from db.index import Base, db_session

from Eliza.countReassemblies import countReassembliesVal

class DepressionReassemblyRatings(Base):

    __tablename__ = 'depression_reassembly_ratings'
    id = Column(Integer, primary_key=True)
    reassembly_rule_index = Column(Integer, unique=True)
    rating = Column(Integer, unique=False)

    def __init__(self, reassembly_rule_index=None, rating=1):
        self.reassembly_rule_index = reassembly_rule_index
        self.rating = rating

    def __repr__(self):
        return f'<Reassembly rule: {self.reassembly_rule_index!r}>'

#if db_session.execute(select(DepressionReassemblyRatings)).fetchone() == None:
#    for i in range(countReassembliesVal('Eliza/depressed.txt')):
#        db_session.add(DepressionReassemblyRatings(reassembly_rule_index=i))
#
#db_session.commit()

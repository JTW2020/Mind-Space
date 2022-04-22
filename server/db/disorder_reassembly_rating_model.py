from sqlalchemy import Column, Integer, String
from db.index import Base


class DisorderReassemblyRatings(Base):

    __tablename__ = 'disorder_reassembly_ratings'
    id = Column(Integer, primary_key=True)
    reassembly_rule_index = Column(Integer, unique=True)
    rating = Column(Integer, unique=False)

    def __init__(self, reassembly_rule_index=None, rating=None):
        self.reassembly_rule_index = reassembly_rule_index
        self.rating = rating

    def __repr__(self):
        return f'<Reassembly rule: {self.reassembly_rule_index!r}>'

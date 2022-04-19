from sqlalchemy import Column, Integer, String
from db.index import Base


class DepressionReassemblyRatings(Base):

    __tablename__ = 'depression_reassembly_ratings'
    id = Column(Integer, primary_key=True)
    reassembly_rule = Column(String(50), unique=True)
    rating = Column(Integer, unique=False)

    def __init__(self, reassembly_rule=None, rating=None):
        self.reassembly_rule = reassembly_rule
        self.rating = rating

    def __repr__(self):
        return f'<Reassembly rule: {self.reassembly_rule!r}>'

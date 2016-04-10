import datetime
from tickets_app.models.meta import Base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    Float,
    DateTime,
    )

class Price(Base):
    __tablename__ = 'prices'
    id = Column(Integer, primary_key=True)
    game_id = Column(Integer, ForeignKey('games.id'))
    datetime = Column(DateTime, nullable=False)
    price = Column(Float)
    source = Column(Integer)
    num_tix = Column(Integer)

    game = relationship("Game", backref=backref("prices", order_by=id))
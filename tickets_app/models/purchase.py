import datetime
from tickets_app.models.meta import Base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    Float,
    DateTime,
    Text,
    )

class Purchase(Base):
    __tablename__ = 'purchases'
    id = Column(Integer, primary_key=True)
    game_id = Column(Integer, ForeignKey('games.id'))
    datetime = Column(DateTime, nullable=False)
    price = Column(Float)
    seat_21 = Column(Integer)
    seat_22 = Column(Integer)

    game = relationship("Game", backref=backref("purchases", order_by=id))
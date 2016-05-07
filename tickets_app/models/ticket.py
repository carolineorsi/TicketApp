import datetime
from tickets_app.models.meta import Base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import (
    Column,
    ForeignKey,
    Date,
    Time,
    String,
    Integer,
    Float,
)

class Ticket(Base):
    __tablename__ = 'tickets'
    ticket_id = Column(Integer, primary_key=True)
    game_date = Column(Date, ForeignKey('games.game_date'))
    section = Column(String(20), nullable=False)
    row = Column(String(5), nullable=False)
    seat = Column(Integer, nullable=False)
    price = Column(Float)
    is_purchased = Column(Integer)
    hold_for_us = Column(Integer)

    game = relationship("Game", backref=backref("tickets", order_by=game_date))
    # need backref?

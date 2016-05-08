import datetime
from tickets_app.models.meta import Base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    Float,
    Date,
    DateTime
    )

class Price(Base):
    __tablename__ = 'prices'
    price_id = Column(Integer, primary_key=True)
    ticket_id = Column(Integer, ForeignKey('tickets.ticket_id'))
    game_id = Column(Integer, ForeignKey('games.game_id'))
    price_date = Column(DateTime)
    price = Column(Float)
    source = Column(Integer)
    num_tix = Column(Integer)

    game = relationship("Game", backref=backref("prices", order_by=game_id))
    ticket = relationship("Ticket", backref=backref("prices", order_by=ticket_id))
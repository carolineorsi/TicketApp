import datetime
from tickets_app.models.meta import Base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    Float,
    String,
    Date,
    Text,
    )

class Purchase(Base):
    __tablename__ = 'purchases'
    purchase_id = Column(Integer, primary_key=True)
    ticket_id = Column(Integer, ForeignKey('tickets.ticket_id'))
    game_id = Column(Integer, ForeignKey('games.game_id'))
    purchase_date = Column(Date)
    buyer = Column(String(50))
    price = Column(Float)
    payment_type = Column(String(20))

    game = relationship("Game", backref=backref("purchases", order_by=game_id))
    ticket = relationship("Ticket", backref=backref("tickets", order_by=ticket_id))

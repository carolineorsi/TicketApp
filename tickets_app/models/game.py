import datetime
from tickets_app.models.meta import Base
from sqlalchemy import (
    Column,
    Date,
    Time,
    String,
    Integer,
    Float,
)

class Game(Base):
    __tablename__ = 'games'
    game_id = Column(Integer, primary_key=True)
    game_date = Column(Date, nullable=False)
    time = Column(Time)
    opponent = Column(String(50), nullable=False)
    promotion = Column(String(50))

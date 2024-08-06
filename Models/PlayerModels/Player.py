from sqlalchemy import  Column, Integer, String, Float , event
from sqlalchemy.ext.declarative import declarative_base

## DOMAIN OBJECT ENTITY MODEL ---------------------------------------------------
Base = declarative_base()

class Player(Base):
    __tablename__ = 'players'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    fn = Column(String(50), nullable=False)
    ln = Column(String(50), nullable=False)
    apt = Column(Integer, nullable=False)
    set = Column(Integer, nullable=False)
    position = Column(String(50), nullable=False)
    nationality = Column(String(50), nullable=False)
    avg = Column(Float, nullable=False)

    def to_dict(obj):
        return {c.key: getattr(obj, c.key) for c in obj.__table__.columns}



#> TASK 2
def calculate_avg(mapper, connection, target):
    target.avg = (target.apt + target.set) / 2.0

event.listen(Player, 'before_insert', calculate_avg) 
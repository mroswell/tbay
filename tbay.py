#A TBay item and the user selling the item - One to many
#A TBay item and the users who have bid on it - Many to Many
#A TBay item and the bids placed on it - One to Many



from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import Table, Column, Integer, String, DateTime, Float, ForeignKey

engine = create_engine('postgresql://marjorieroswell:marjorieroswell@localhost:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

item_user_table = Table('item_user_association', Base.metadata,
    Column('item_id', Integer, ForeignKey('item.id')),
    Column('user_id', Integer, ForeignKey('user.id'))
)

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    start_time = Column(DateTime, default=datetime.utcnow)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)

class Bid(Base):
    __tablename__ = "bids"
    id = Column(Integer, primary_key=True)
    price = Column(Float, nullable=False)

Base.metadata.create_all(engine)

beyonce = User()
beyonce.username = "bknowles"
beyonce.password = "crazyinlove"
sylvester = User()
sylvester.username = "sylvester"
sylvester.password = "meow453"
jane = User()
jane.username = "jane"
jane.password = "mejane879"
Base.metadata.create_all(engine)

session.add_all([beyonce, sylvester, jane])
session.commit()


#    guitars = relationship("Guitar", backref="manufacturer")

#    manufacturer_id = Column(Integer, ForeignKey('manufacturer.id'),
#                           nullable=False)

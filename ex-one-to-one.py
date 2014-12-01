
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, ForeignKey, create_engine
from datetime import datetime

engine = create_engine('postgresql://marjorieroswell:marjorieroswell@localhost:5432/tbay')

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    passport = relationship("Passport", uselist=False, backref="owner")

class Passport(Base):
    __tablename__ = 'passport'
    id = Column(Integer, primary_key=True)
    issue_date = Column(Date, nullable=False, default=datetime.utcnow)
    owner_id = Column(Integer, ForeignKey('person.id'), nullable=False)

beyonce = Person(name="Beyonce Knowles")
passport = Passport()
beyonce.passport = passport

Base.metadata.create_all(engine)
session.add(beyonce)
session.commit()

print beyonce.passport.issue_date
print passport.owner.name

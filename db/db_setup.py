from sqlalchemy import Column, Integer
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:116143@localhost/postgres"

engine = create_engine(SQLALCHEMY_DATABASE_URL, future=True, echo=False)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine, future=True)

class Base(object):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True, autoincrement="auto", index=True) 

Base = declarative_base(cls=Base)

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()    
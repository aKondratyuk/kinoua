Base = 'postgresql+psycopg2'
USERNAME = 'kinoua'
PASSWORD = '1234'
HOST = 'localhost'
PORT = '5432'
DATABase = 'kino'

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_Base
from sqlalchemy.orm import sessionmaker

db_string = '{Base}://{user}:{pw}@{host}:{port}/{db}'.format(Base=Base, user=USERNAME, pw=PASSWORD, host=HOST, port=PORT, db=DATABase)

engine = create_engine(db_string)
Session = sessionmaker(bind=engine)

Base = declarative_Base()

metadata = Base.metadata

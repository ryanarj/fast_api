import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import config

engine = create_engine("postgresql+psycopg2://postgres:1234@localhost/fast_api")
Session = sessionmaker(bind=engine)


def connect():
    connection = None
    try:
        params = config()
        connection = psycopg2.connect(**params)

        crsr = connection.cursor()
        crsr.execute("SELECT version()")
        db_version = crsr.fetchone()
        crsr.close()
    except (Exception, psycopg2.DatabaseError) as err:
        print(err)
    finally:
        if connection is not None:
            connection.close()


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

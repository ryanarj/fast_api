import psycopg2

from config import config


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

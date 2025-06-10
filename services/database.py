from pysqlcipher3 import dbapi2 as sqlite

from config import DATABASE


def get_db_connection():
    return sqlite.connect(DATABASE)


def init_db():
    get_db_connection()

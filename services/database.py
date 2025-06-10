from pysqlcipher3 import dbapi2 as sqlite

from config import DATABASE


def get_db_connection():
    return sqlite.connect(DATABASE)


def init_db():
    conn = get_db_connection()

    conn.execute("PRAGMA key = 'secure_password_placeholder';")

    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
    )

    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER REFERENCES users(id),
            amount REAL NOT NULL,
            description TEXT,
            date DATETIME
        );
        """
    )

    conn.commit()
    conn.close()

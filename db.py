import mysql.connector
from config import Config

def get_db_connection():
    """Establishes and returns a database connection."""
    conn = mysql.connector.connect(
        host=Config.MYSQL_HOST,
        user=Config.MYSQL_USER,
        password=Config.MYSQL_PASSWORD,
        charset=Config.MYSQL_CHARSET,
        database=Config.MYSQL_DB,

    )
    return conn

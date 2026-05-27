import pymysql
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME

class Database:

    @staticmethod
    def get_connection():
        return pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            cursorclass=pymysql.cursors.DictCursor,
            # 👇 ESTO SOLUCIONA EL ERROR DE SSL CON AWS RDS
            ssl={'ssl_disabled': True}
        )
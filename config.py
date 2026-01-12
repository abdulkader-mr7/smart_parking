import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    MYSQL_HOST = os.getenv("MYSQL_HOST")
    MYSQL_USER = os.getenv("MYSQL_USER")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
    MYSQL_DB = os.getenv("MYSQL_DB","smart_parking_face")
    MYSQL_CHARSET = os.getenv("MYSQL_CHARSET", "utf8")
    MYSQL_PORT = os.getenv("MYSQL_PORT")

# import os
# from dotenv import load_dotenv
#
# class Config:
#     SECRET_KEY = os.getenv('SECRET_KEY') or 'abcdef'
#     MYSQL_HOST = 'localhost'
#     MYSQL_USER = 'root'
#     MYSQL_PASSWORD =''
#     MYSQL_DB = 'smart_parking_face'
#     MYSQL_CHARSET = 'utf8'
#     MYSQL_PORT = 3306

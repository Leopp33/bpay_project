import os
import binascii
from urllib import parse
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

db_user = os.getenv("DB_USER")
db_password = parse.quote_plus(os.getenv("DB_PASSWORD"))
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT", 3306)
db_name = os.getenv("DB_NAME")

class Config():
    FLASK_RUN_PORT = os.getenv('APP_PORT', 8000)
    SECRET_KEY = os.getenv('SECRET_KEY', binascii.hexlify(os.urandom(32)).decode())
    FLASK_APP = os.getenv('APP_FILE')
    FLASK_DEBUG = os.getenv('APP_DEBUG')

    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


import os
import binascii                           import urllib.parse
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config():
    FLASK_RUN_PORT = os.getenv('APP_PORT', 8000)
    SECRET_KEY = os.getenv('SECRET_KEY', binascii.hexlify(os.urandom(32)).decode())
    FLASK_APP = os.getenv('APP_FILE')
    FLASK_DEBUG = os.getenv('APP_DEBUG')

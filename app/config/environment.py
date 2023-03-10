import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

DATABASE_DIALECT = os.getenv('DATABASE_DIALECT')
DATABASE_HOSTNAME = os.getenv('DATABASE_HOSTNAME')
DATABASE_NAME = os.getenv('DATABASE_NAME')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
DATABASE_PORT = os.getenv('DATABASE_PORT')
DATABASE_USERNAME = os.getenv('DATABASE_USERNAME')
DEBUG_MODE = os.getenv('DEBUG_MODE') == 'true'


SQLALCHEMY_DATABASE_URI = (
        f"{DATABASE_DIALECT}://{DATABASE_USERNAME}:"
        f"{DATABASE_PASSWORD}@{DATABASE_HOSTNAME}:"
        f"{DATABASE_PORT}/{DATABASE_NAME}"
)
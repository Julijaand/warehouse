import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file


class Config:
    MYSQL_DATABASE_USER = os.getenv('MYSQL_USER')
    MYSQL_DATABASE_PASSWORD = os.getenv('MYSQL_PASSWORD')
    MYSQL_DATABASE_DB = os.getenv('MYSQL_DB')
    MYSQL_DATABASE_HOST = os.getenv('MYSQL_HOST')
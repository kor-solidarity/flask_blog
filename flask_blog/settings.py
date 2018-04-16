import os

SECRET_KEY = 'AAA'
DEBUG = True
DB_USERNAME = 'root'
DB_PASSWORD = '123'
BLOG_DATABASE_NAME = 'blog'
DB_HOST = os.getenv("IP", 'localhost')
DB_URI = 'mysql+pymysql://{}:{}@{}/{}'.format(DB_USERNAME, DB_PASSWORD, DB_HOST, BLOG_DATABASE_NAME)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True

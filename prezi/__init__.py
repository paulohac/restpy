from dotenv import load_dotenv, find_dotenv
import os

try:
    load_dotenv(find_dotenv())
except:
    print("couldn't load env variables from .env!")


PAGE_SIZE = 10

PG_HOST = os.environ.get('PG_HOST', 'postgres')
PG_PORT = os.environ.get('PG_PORT', 5432)
PG_DATABASE = os.environ.get('PG_DATABASE', 'prezis')
PG_USER = os.environ.get('PG_USER', 'postgres')
PG_PASSWORD = os.environ.get('PG_PASSWORD', 'postgres')

PG_DSN = 'postgres://{}:{}@{}:{}/{}'.format(PG_USER, PG_PASSWORD, PG_HOST, PG_PORT, PG_DATABASE)
PACKAGE_ROOT = os.path.join(os.path.dirname(__file__), '..')


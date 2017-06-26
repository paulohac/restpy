import psycopg2
from prezi import PG_HOST, PG_USER, PG_PORT, PG_PASSWORD, PG_DATABASE, PG_DSN, PACKAGE_ROOT
from yoyo import read_migrations, get_backend
from datetime import datetime
import os
import json

connection = None

def init():
    create()
    migrate()
    seed()
    connect()


def create():
    try:
        with psycopg2.connect(host=PG_HOST, user=PG_USER, port=PG_PORT, password=PG_PASSWORD) as connection:
            connection.autocommit = True
            with connection.cursor() as cursor:
                cursor.execute("CREATE DATABASE {}".format(PG_DATABASE))
            print('database created')
    except:
        pass


def migrate():
    """Migrate up"""
    backend = get_backend(PG_DSN, '_migrations')
    migrations = read_migrations(os.path.join(PACKAGE_ROOT, 'db', 'migrations'))
    backend.apply_migrations(backend.to_apply(migrations))


def seed():
    with psycopg2.connect(host=PG_HOST, user=PG_USER, port=PG_PORT, password=PG_PASSWORD, database=PG_DATABASE) as connection:
        cur = connection.cursor()
        cur.execute('SELECT COUNT(id) from prezis')
        row_count, = cur.fetchone()
        if row_count == 0:
            print('seeding the database')
            with open(os.path.join(PACKAGE_ROOT, 'db', 'seed', 'big_json_infra_hw.json'), 'rt') as f:
                seed_data = json.load(f)

            for row in seed_data:
                cur.execute('INSERT INTO prezis (id, title, picture, created_at, creator_id, creator_name) VALUES (%s, %s, %s, %s, %s, %s)',
                                (row['id'], row['title'], row['picture'],
                                 datetime.strptime(row['createdAt'], '%a %b %d %Y %H:%M:%S %Z%z'),
                                 row['creator']['id'], row['creator']['name']))


def connect():
    global connection
    connection = psycopg2.connect(dsn=PG_DSN)

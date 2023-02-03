import psycopg2
from flask import current_app, g


def get_db():

    if "db" not in g:
        with open("db-connection-string.txt", "r") as f:
            conn_str = f.read()
        g.db = psycopg2.connect(conn_str)
    return g.db


def close_db(e=None):

    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_app(app):

    app.teardown_appcontext(close_db)

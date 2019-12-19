from contextlib import contextmanager
import json

import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker


#------------------------------------------------------
# DB helper functions, you don't need to modify these.|
# -----------------------------------------------------

def make_uri(db_user, db_password, db_host, db_name):
    return 'mysql+pymysql://{}:{}@{}/{}'.format(
        db_user,
        db_password,
        db_host,
        db_name,
    )


@contextmanager
def commit_session(uri):
    engine = sa.create_engine(uri)
    dbsession = sa.orm.sessionmaker(bind=engine)()
    yield dbsession
    dbsession.commit()


def fetch_data(query):
    """
    Returns a SQLAlchemy `ResultProxy`, which is an iterable of tuples
    corresponding to the rows returned by the query.
    """
    uri = make_uri(
        'demouser',
        'demopass',
        'giantotterdbinstance-staging.cdpfkoxivmj6.us-east-1.rds.amazonaws.com',
        'caidb_dev',
    )

    with commit_session(uri) as db:
        query = sa.text(query)
        rows = db.execute(query)

    # SQLAlchemy allows dot access by column name on results.
    return rows


#----------------------------------
# Do modify this code             |
#----------------------------------

def get_utterances():
    """
    Extract the utterances from a list of data dictionaries. The query supplied

    to this function will be run against the chat_data table described above.
    :param decoded_data: SQL query (string)
    :returns utterances: list of utterances
    """
    query = "Your SQL query here"
    rows = fetch_data(query)
    row_data = [row.data for row in rows]
    # TODO: parse the utterances out of the row data.
    return

import psycopg2
from contextlib import contextmanager


@contextmanager
def get_pg_connection(dbname, user, password, host, port):
    conn = None
    try:
        conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
        yield conn
    finally:
        if conn:
            conn.close()


def insert_data(conn):
    cur = conn.cursor()
    for i in range(1, 1000001):
        cur.execute("INSERT INTO books (title, author, year) VALUES (%s, %s, %s)", (f'Title {i}', f'Author {i}', 2020))
    conn.commit()
    cur.close()


if __name__ == "__main__":
    with get_pg_connection(dbname='books_db', user='user', password='password', host='localhost', port='5432') as conn:
        insert_data(conn)

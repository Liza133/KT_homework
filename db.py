import psycopg2
def connection():
    try:
        # пытаемся подключиться к базе данных
        conn = psycopg2.connect(dbname='mydb', user='postgres', password='133133', host="localhost",  port='5432')
        return conn
    except:
        # в случае сбоя подключения будет выведено сообщение в STDOUT
        return 'Can`t establish connection to database'



def table_creation(conn):
    try:
        with conn.cursor() as curs:
            curs.execute('CREATE TABLE filedata (uuid UUID, file_path TEXT, type CHAR(3), size FLOAT8, create_dttm TIMESTAMP);')
        conn.commit()
        # conn.close()
    except psycopg2.errors.DuplicateTable:
        return 'table is already exists'


def insert(conn, uuid, file_path, type, size):
    with conn.cursor() as curs:
        curs.execute("INSERT INTO filedata (uuid, file_path, type, size, create_dttm) VALUES (uuid(%s), %s, %s, %s, now());", (uuid, file_path, type, size))
    conn.commit()
    # conn.close()


# print(table_creation(connection()))

# conn = connection()
# with conn.cursor() as curs:
#     curs.execute('CREATE TABLE filedata (uuid UUID, file_path TEXT, type CHAR(3), size FLOAT8, create_dttm TIMESTAMP);')
#     # curs.execute("INSERT INTO filedata VALUES ('047c0458-46c2-4f3b-945a-d063ab2c0bef', 'text', 'TST', 1234, now());")
# conn.commit()
# conn.close()
#


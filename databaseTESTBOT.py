import psycopg2
from config import host, dbname, user, password, port

connection = None


try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        dbname=dbname,
        password=password,
        port=port
    )

    cur = connection.cursor()
    connection.autocommit = True

    cur.execute("""CREATE TABLE IF NOT EXISTS personBOT(
                telegram_id BIGINT UNIQUE,
                name VARCHAR(255) UNIQUE
                )""")

    def add_user(telegram_id, name):
        cur.execute("INSERT INTO personBOT (telegram_id, name) VALUES (%s,%s) ON CONFLICT (telegram_id) DO NOTHING", (telegram_id, name))

    def check_user_register(telegram_id):
        cur.execute("SELECT * FROM personBOT WHERE telegram_id = %s ; ", (telegram_id,)) 
        user = cur.fetchone()
        return user
    

except Exception as _ex:
    print("[INFO!] Error while working with PostgreSQL", _ex)



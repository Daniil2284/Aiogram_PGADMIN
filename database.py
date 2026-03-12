import psycopg2
from config import host, dbname, user, password, port

connection = None

name = input("Enter your name: ")
find_user = input("Enter name users: ")

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

    cur.execute("""CREATE TABLE IF NOT EXISTS person(
                telegram_id BIGINT UNIQUE,
                id SERIAL PRIMARY KEY,
                name VARCHAR(255) UNIQUE,
                age INT,
                gender CHAR,
                )""")
    
    # cur.execute("""INSERT INTO person (name,age,gender) VALUES 
    #             ('test', 23, 'm'),
    #             ('Mike', 27, 'm'),
    #             ('Daniel', 24, 'f')
    #             ON CONFLICT (name) DO NOTHING
    #             """)

    # cur.execute("SELECT * FROM person WHERE name= %s ", (name,) )
    cur.execute("INSERT INTO person ( name, age, gender) VALUES (%s,%s,%s) ON CONFLICT (name) DO NOTHING RETURNING id", ( name, 25, 'M'))
    row = cur.fetchone()

    cur.execute("SELECT * FROM person WHERE name =%s;", (name,))
    user = cur.fetchone()

    if row:
        print("[INFO!] successfully register new users")
    else:
        print("[SUCCES] logged in systems", user[1])
        

    sql = cur.mogrify("SELECT * FROM person WHERE starts_with(name, %s);", (find_user,))
    # print(sql)

    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row[1])

    def add_user(telegram_id, name):
        cur.execute("INSERT INTo person (telegram_id, name) VALUES (%s,%s) ON CONFLICT (telegram_id) DO NOTHING")

    cur.close()
    # print("[INFO!] Table created successfully")

    # cur.execute("ISNERT INTO person(telegram_id, name)" \
    # "VALUES(%s, %s)" \
    # "ON CONFLICT (telegram_id) DO NOTHING ", telegram_id, name)


except Exception as _ex:
    print("[INFO!] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        connection.close()
        print("[INFO!] PosqtgreSQL connection closed")


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
                name VARCHAR(255) UNIQUE,
                balance INT DEFAULT 1000,
                username VARCHAR(255) UNIQUE,
                bitcoin FLOAT DEFAULT 0,
                gold FLOAT DEFAULT 0,
                coins INT DEFAULT 0,

                home INT DEFAULT 0,
                car INT DEFAULT 0,
                business INT DEFAULT 0,
                
                bank_balance INT DEFAULT 0,
                bank_balance_deposite INT DEFAULT 0,
                tax_balance INT DEFAULT 0,

                level INT DEFAULT 1,
                exp INT DEFAULT 0,
                max_exp INT DEFAULT 1000,

                date_register TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )""") 

    def add_user(telegram_id, name, username):
        cur.execute("INSERT INTO personBOT (telegram_id, name, username, balance, level, exp, max_exp) VALUES (%s,%s,%s, 1000, 1, 0, 1000) ON CONFLICT (telegram_id) DO NOTHING", (telegram_id, name, username))

    def check_user_register(telegram_id):
        cur.execute("SELECT * FROM personBOT WHERE telegram_id = %s", (telegram_id,)) 
        user = cur.fetchone()
        return user
    
    def update_balance(balance, telegram_id):
        cur.execute("UPDATE personBOT SET balance = %s WHERE telegram_id = %s", (balance,telegram_id))
    
    def update_exp(exp, telegram_id):
        cur.execute("UPDATE personBOT SET exp = %s WHERE telegram_id = %s", (exp, telegram_id))

    def update_level(level, telegram_id):
        cur.execute("UPDATE personBOT SET level = %s WHERE telegram_id = %s", (level, telegram_id))    
    
    def update_max_exp(max_exp, telegram_id):
        cur.execute("UPDATE personBOT SET max_exp = %s WHERE telegram_id = %s", (max_exp, telegram_id))    
    

except Exception as _ex:
    print("[INFO!] Error while working with PostgreSQL", _ex)



import psycopg2
from db_config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD

try:
    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("NOTIFY pgrst, 'reload schema';")
    print("PostgREST schema cache reloaded.")
    cur.close()
    conn.close()
except Exception as e:
    print(f"Error: {e}")

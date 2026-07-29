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
    cur.execute("GRANT ALL PRIVILEGES ON TABLE teacher_certificates TO anon, authenticated;")
    cur.execute("GRANT USAGE, SELECT ON SEQUENCE teacher_certificates_id_seq TO anon, authenticated;")
    cur.execute("NOTIFY pgrst, 'reload schema';")
    print("Permissions granted and schema reloaded.")
    cur.close()
    conn.close()
except Exception as e:
    print(f"Error: {e}")

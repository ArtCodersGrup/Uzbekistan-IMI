import psycopg2

try:
    conn = psycopg2.connect(
        host="aws-1-ap-northeast-2.pooler.supabase.com",
        port=5432,
        dbname="postgres",
        user="postgres.obswrerbtrznxhcvridd",
        password="R9Q9jGLeXj24foc7"
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

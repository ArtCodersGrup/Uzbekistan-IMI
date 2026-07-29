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
    cur.execute("NOTIFY pgrst, 'reload schema';")
    print("PostgREST schema cache reloaded.")
    cur.close()
    conn.close()
except Exception as e:
    print(f"Error: {e}")

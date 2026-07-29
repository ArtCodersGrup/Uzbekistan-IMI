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

    print("Running migration...")

    cur.execute("ALTER TABLE teachers ADD COLUMN IF NOT EXISTS phone_number VARCHAR(150);")
    cur.execute("ALTER TABLE teachers ADD COLUMN IF NOT EXISTS telegram_username VARCHAR(150);")
    
    cur.execute("""
    CREATE TABLE IF NOT EXISTS teacher_certificates (
        id SERIAL PRIMARY KEY,
        teacher_id INT NOT NULL,
        title VARCHAR(200),
        image_url VARCHAR(255),
        CONSTRAINT fk_teacher
           FOREIGN KEY(teacher_id)
           REFERENCES teachers(id)
           ON DELETE CASCADE
    );
    """)

    print("Migration successful!")

    cur.close()
    conn.close()
except Exception as e:
    print(f"Error: {e}")

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

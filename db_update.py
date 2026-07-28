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

    print("Updating tables...")

    cur.execute("ALTER TABLE teachers ADD COLUMN IF NOT EXISTS phone VARCHAR(50);")
    cur.execute("ALTER TABLE teachers ADD COLUMN IF NOT EXISTS telegram VARCHAR(255);")
    cur.execute("ALTER TABLE teachers ADD COLUMN IF NOT EXISTS bio TEXT;")
    cur.execute("ALTER TABLE teachers ADD COLUMN IF NOT EXISTS certificates JSONB DEFAULT '[]'::jsonb;")
    
    # Update dummy data manually so it has info
    cur.execute("""
    UPDATE teachers SET 
        phone='+998901234567', 
        telegram='@eshmatov', 
        bio='Ushbu o''qituvchi uzoq yillar davomida xalq ta''limi sohasida mehnat qilib keladi.',
        certificates='["img/cert1.jpg", "img/cert2.jpg"]'::jsonb
    WHERE full_name='Toshmatov Eshmat';
    """)
    print("Database updated!")
    
    cur.close()
    conn.close()
except Exception as e:
    print(f"Error: {e}")

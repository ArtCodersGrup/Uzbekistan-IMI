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

    print("Connected. Creating tables...")

    cur.execute("""
    CREATE TABLE IF NOT EXISTS teachers (
        id SERIAL PRIMARY KEY,
        full_name VARCHAR(255) NOT NULL,
        role VARCHAR(255) NOT NULL,
        description TEXT,
        image_url VARCHAR(500),
        created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS news (
        id SERIAL PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        content TEXT NOT NULL,
        image_url VARCHAR(500),
        created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
    );
    """)

    print("Tables created. Inserting dummy data...")

    cur.execute("SELECT COUNT(*) FROM teachers")
    if cur.fetchone()[0] == 0:
        cur.execute("""
        INSERT INTO teachers (full_name, role, description, image_url) VALUES
        ('Quziyeva Xafizaxon Abdullayevna', 'Maktab-internat direktori', 'Tajribali rahbar, ta''lim sohasida 20 yildan ortiq tajribaga ega.', 'img/direktor.jpg'),
        ('Xalilov Dilshodbek Abduqahhor o''g''li', 'Maktab-internat maslahatchisi', 'Yoshlar bilan ishlash bo''yicha mutaxassis.', 'img/maslahatchi.jpg')
        """)

    cur.execute("SELECT COUNT(*) FROM news")
    if cur.fetchone()[0] == 0:
        cur.execute("""
        INSERT INTO news (title, content, image_url) VALUES
        ('Maktabimizda Navro''z sayli o''tkazildi', 'Kuni kecha maktab-internatimiz hovlisida bahor ayyomi — Navro''z umumxalq bayrami keng nishonlandi.', 'img/hero-1.jpg'),
        ('Matematika bo''yicha ochiq darslar', 'Viloyat mutaxassislari tashrif buyurdi va darslarni kuzatdi.', 'img/hero-2.jpg')
        """)
        
    print("Dummy data inserted.")
    
    cur.close()
    conn.close()
    print("Success")
except Exception as e:
    print(f"Error: {e}")

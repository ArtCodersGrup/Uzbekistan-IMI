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

    print("Setting up storage...")
    
    # Create bucket
    cur.execute("""
    INSERT INTO storage.buckets (id, name, public) 
    VALUES ('images', 'images', true) 
    ON CONFLICT (id) DO UPDATE SET public = true;
    """)
    
    # Create policies to allow public uploading and reading
    # First, drop if exists to avoid errors
    cur.execute("DROP POLICY IF EXISTS \"Public Upload policy\" ON storage.objects;")
    cur.execute("DROP POLICY IF EXISTS \"Public Read policy\" ON storage.objects;")
    
    # Now create
    cur.execute("""
    CREATE POLICY "Public Upload policy" ON storage.objects FOR INSERT WITH CHECK (bucket_id = 'images');
    """)
    cur.execute("""
    CREATE POLICY "Public Read policy" ON storage.objects FOR SELECT USING (bucket_id = 'images');
    """)

    print("Storage configured successfully!")

    cur.close()
    conn.close()
except Exception as e:
    print(f"Error: {e}")

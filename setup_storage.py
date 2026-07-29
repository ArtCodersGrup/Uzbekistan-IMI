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

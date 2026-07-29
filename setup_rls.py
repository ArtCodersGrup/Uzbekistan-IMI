"""Enable Row Level Security and lock down anon access.

Currently `anon` (i.e. any site visitor, via the public ANON_KEY embedded in
supabase-client.js) has full INSERT/UPDATE/DELETE on every table because
setup_surveys.py / grant_permissions.py granted it directly with no RLS
policy in place. This script:

  - Enables RLS on every app table.
  - Tightens table-level GRANTs so `anon` only has SELECT (plus INSERT on
    the two survey-submission tables that the public form writes to).
  - Adds explicit policies: anon/authenticated can read everything public;
    only `authenticated` (the logged-in admin, via Supabase Auth) can
    insert/update/delete, except survey_responses/survey_answers where
    anon also needs INSERT to submit a survey.

Run this once after rotating the DB password and updating .env.
"""
import psycopg2
from db_config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD

# Tables anon may only read.
READ_ONLY_TABLES = [
    'teachers', 'news', 'surveys', 'survey_questions',
    'survey_options', 'teacher_certificates',
]

# Tables the public survey form also needs to INSERT into.
READ_WRITE_TABLES = ['survey_responses', 'survey_answers']

ALL_TABLES = READ_ONLY_TABLES + READ_WRITE_TABLES

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

    print("Enabling RLS and tightening privileges...")

    for t in ALL_TABLES:
        cur.execute(f"ALTER TABLE {t} ENABLE ROW LEVEL SECURITY;")

        cur.execute(f"REVOKE ALL ON TABLE {t} FROM anon;")
        cur.execute(f"REVOKE ALL ON TABLE {t} FROM authenticated;")
        cur.execute(f"GRANT SELECT ON TABLE {t} TO anon;")
        cur.execute(f"GRANT ALL PRIVILEGES ON TABLE {t} TO authenticated;")
        cur.execute(f"GRANT USAGE, SELECT ON SEQUENCE {t}_id_seq TO authenticated;")

        cur.execute(f'DROP POLICY IF EXISTS "public_read" ON {t};')
        cur.execute(f'CREATE POLICY "public_read" ON {t} FOR SELECT TO anon, authenticated USING (true);')

        cur.execute(f'DROP POLICY IF EXISTS "admin_insert" ON {t};')
        cur.execute(f'CREATE POLICY "admin_insert" ON {t} FOR INSERT TO authenticated WITH CHECK (true);')

        cur.execute(f'DROP POLICY IF EXISTS "admin_update" ON {t};')
        cur.execute(f'CREATE POLICY "admin_update" ON {t} FOR UPDATE TO authenticated USING (true) WITH CHECK (true);')

        cur.execute(f'DROP POLICY IF EXISTS "admin_delete" ON {t};')
        cur.execute(f'CREATE POLICY "admin_delete" ON {t} FOR DELETE TO authenticated USING (true);')

        print(f"  - {t}: RLS enabled")

    for t in READ_WRITE_TABLES:
        cur.execute(f"GRANT INSERT ON TABLE {t} TO anon;")
        cur.execute(f"GRANT USAGE, SELECT ON SEQUENCE {t}_id_seq TO anon;")

        cur.execute(f'DROP POLICY IF EXISTS "public_insert" ON {t};')
        cur.execute(f'CREATE POLICY "public_insert" ON {t} FOR INSERT TO anon WITH CHECK (true);')

        print(f"  - {t}: public INSERT policy added")

    cur.execute("NOTIFY pgrst, 'reload schema';")
    print("RLS enabled and policies created successfully.")

    cur.close()
    conn.close()
except Exception as e:
    print(f"Error: {e}")

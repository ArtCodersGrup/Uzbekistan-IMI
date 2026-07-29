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

    print("Running survey migrations...")

    # Surveys
    cur.execute("""
    CREATE TABLE IF NOT EXISTS surveys (
        id SERIAL PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        description TEXT,
        is_anonymous_allowed BOOLEAN DEFAULT TRUE,
        is_open BOOLEAN DEFAULT TRUE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # Questions
    cur.execute("""
    CREATE TABLE IF NOT EXISTS survey_questions (
        id SERIAL PRIMARY KEY,
        survey_id INT REFERENCES surveys(id) ON DELETE CASCADE,
        question_text TEXT NOT NULL,
        question_type VARCHAR(50) NOT NULL,
        order_num INT
    );
    """)

    # Options (choices for multiple choice questions)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS survey_options (
        id SERIAL PRIMARY KEY,
        question_id INT REFERENCES survey_questions(id) ON DELETE CASCADE,
        option_text TEXT NOT NULL
    );
    """)

    # Responses (One row per user submitting the survey)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS survey_responses (
        id SERIAL PRIMARY KEY,
        survey_id INT REFERENCES surveys(id) ON DELETE CASCADE,
        responder_name VARCHAR(150),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # Answers
    cur.execute("""
    CREATE TABLE IF NOT EXISTS survey_answers (
        id SERIAL PRIMARY KEY,
        response_id INT REFERENCES survey_responses(id) ON DELETE CASCADE,
        question_id INT REFERENCES survey_questions(id) ON DELETE CASCADE,
        option_id INT REFERENCES survey_options(id) ON DELETE CASCADE,
        answer_text TEXT
    );
    """)

    # Permissions
    tables = ['surveys', 'survey_questions', 'survey_options', 'survey_responses', 'survey_answers']
    for t in tables:
        cur.execute(f"GRANT ALL PRIVILEGES ON TABLE {t} TO anon, authenticated;")
        cur.execute(f"GRANT USAGE, SELECT ON SEQUENCE {t}_id_seq TO anon, authenticated;")

    cur.execute("NOTIFY pgrst, 'reload schema';")
    
    print("Migration and permissions successful!")

    cur.close()
    conn.close()
except Exception as e:
    print(f"Error: {e}")

def create_schema_ver(conn):
    conn.execute("""
    CREATE TABLE IF NOT EXISTS
    schema_ver(
    version INTEGER NOT NULL
    )
    """)

    cur=conn.execute("SELECT COUNT(*) FROM schema_ver")
    if cur.fetchone()[0]==0:
        conn.execute("INSERT INTO schema_ver VALUES(0)")
        conn.commit()

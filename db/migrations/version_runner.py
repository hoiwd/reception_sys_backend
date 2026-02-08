def get_schema_ver(conn):
    return conn.execute(
        "SELECT version FROM schema_ver"
    ).fetchone()[0]

def set_schema_ver(conn, version):
    conn.execute("UPDATE schema_ver SET version =?", (version, ))



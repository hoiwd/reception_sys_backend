
def migrate_0_1(conn):
    conn.execute("""
    CREATE TABLE guests(
    name TEXT PRIMARY KEY,
    room INTEGER UNIQUE NOT NULL,
    plan INTEGER NOT NULL
    )
    """)

def migrate_1_2(conn):
    conn.execute("""
    ALTER TABLE guests
    ADD COLUMN created_at TEXT
    DEFAULT CURRENT_TIMESTAMP
    """)

def migrate_2_3(conn):
    conn.execute("""
    ALTER TABLE guests
    ADD COLUMN deleted_at TEXT
    DEFAULT NULL
    """)

def migrate_3_4(conn):

    conn.execute("""
    ALTER TABLE guests ADD COLUMN last_room 
    INTEGER
    """)

    conn.execute("""
    ALTER TABLE guests ADD COLUMN last_plan 
    INTEGER
    """)

def migrate_4_5(conn):
    conn.execute("ALTER TABLE guests RENAME TO guests_old")

    conn.execute("""
    CREATE TABLE guests(
    name TEXT PRIMARY KEY,
    room INTEGER,
    plan INTEGER,
    last_room INTEGER,
    last_plan INTEGER,
    created_at TEXT
    DEFAULT CURRENT_TIMESTAMP,
    deleted_at TEXT)
     
    """)

    conn.execute("""
    INSERT INTO guests
    SELECT name, room, plan, last_room, last_plan, created_at, deleted_at 
    FROM guests_old
    """)

    conn.execute("DROP TABLE guests_old")

def migrate_5_6(conn):
    # Rename old table
    conn.execute("ALTER TABLE guests RENAME TO guests_old")

    # Create new table with id as PK
    conn.execute("""
        CREATE TABLE guests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            room INTEGER,
            plan INTEGER,
            cached_user TEXT, 
            last_room INTEGER,
            last_plan INTEGER,
            created_at TEXT,
            deleted_at TEXT
        )
    """)

    # Drop old table
    conn.execute("DROP TABLE guests_old")
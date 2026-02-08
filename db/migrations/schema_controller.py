from .define_migrations import migrate_0_1, migrate_1_2, migrate_2_3, migrate_3_4, migrate_4_5, migrate_5_6
from .schema_version import create_schema_ver
from .version_runner import get_schema_ver, set_schema_ver

MIGRATIONS={
    1: migrate_0_1,
    2: migrate_1_2,
    3: migrate_2_3,
    4: migrate_3_4,
    5: migrate_4_5,
    6: migrate_5_6
}

def migrate(conn):
    create_schema_ver(conn)
    curr_ver= get_schema_ver(conn)

    for up_ver in sorted(MIGRATIONS):
        if up_ver > curr_ver:
            with conn:
                MIGRATIONS[up_ver](conn)
                set_schema_ver(conn, up_ver)


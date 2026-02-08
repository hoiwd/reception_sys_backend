import sqlite3
from .repo_interface import GuestRepository

class sqliteGuestRepo(GuestRepository):
    def __init__(self, conn):
        self.conn=sqlite3.connect("hotel.db")
        self.conn.execute("PRAGMA foreign_keys=ON")
        self._create_table()

    def _create_table(self):
        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS guests(
        name TEXT PRIMARY KEY,
        room INTEGER UNIQUE,
        plan INTEGER
        )
        """)
        self.conn.commit()

    def add(self, name, room, plan):
        self.conn.execute("INSERT INTO guests(name, room, plan) VALUES (?,?,?)",
                          (name, room, plan))
        self.conn.commit()

    def name_exists(self, name):
        return self.conn.execute("SELECT 1 FROM guests WHERE name=?",
                                 (name, )).fetchone() is not None

    def room_exists(self, room):
        return self.conn.execute("SELECT 1 FROM guests WHERE room=?",
                                 (room, )).fetchone() is not None

    def soft_delete(self, name):
        cur=self.conn.execute("""
        UPDATE guests SET 
        cached_user=name,
        last_room=room,
        last_plan=plan,
        name=NULL,
        room=NULL,
        plan=NULL,
        deleted_at = CURRENT_TIMESTAMP
        WHERE name = ? AND 
        deleted_at IS NULL
        """, (name, ))
        self.conn.commit()

    def restore_guest(self, name, new_room, new_plan):
        cur=self.conn.execute("""
        UPDATE guests SET
        room = ?,
        plan = ?,
        created_at = CURRENT_TIMESTAMP
        WHERE name = ? AND 
        deleted_at IS NULL
        """, (new_room, new_plan, name))
        self.conn.commit()










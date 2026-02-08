from .read_interface import GuestReadModel

class SQLiteGuestReadModel(GuestReadModel):
    def __init__(self, conn):
        self.conn=conn

    def list_guests(self):
        return self.conn.execute("""
        SELECT name, room, plan, created_at
        FROM guests 
        WHERE deleted_at IS NULL
        ORDER BY room
        GROUP BY plan
        """).fetchall()

    def list_past_guests(self):
        return self.conn.execute("""
        SELECT name, last_room, last_plan, deleted_at
        FROM guests
        WHERE deleted_at IS NOT NULL
        ORDER BY room
        GROUP BY plan
        """).fetchall()



    def find_by_room(self, room):
        return self.conn.execute("""
        SELECT name, room, plan
        FROM guests 
        WHERE room=?
        """, (room, )).fetchone()

    def occupancy(self):
        return self.conn.execute("""
        SELECT COUNT(*) FROM guests
        """).fetchone()[0]


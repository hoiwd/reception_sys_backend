# project_1/main.py
import sqlite3
from reception_sys.repos.guest_repository import sqliteGuestRepo
from reception_sys.services.reception_service import ReceptionService
from reception_sys.db.migrations.schema_controller import migrate
from reception_sys.read_models.SQLite_read import SQLiteGuestReadModel

def main():
    conn = sqlite3.connect("hotel.db")

    # schema_migration
    migrate(conn)

    # infrastructure
    repo = sqliteGuestRepo(conn)

    # services
    service = ReceptionService(repo)

    # read_models
    read_model = SQLiteGuestReadModel(conn)

    # run_app
    # service.guest_add("ALICE", 64, 3)
    # service.restore_guest("ALICE", 77, 3)
    # service.guest_add("BOB", 64, 2)
    # service.withdraw_guest("ALICE")
    # service.withdraw_guest("BOB")
    # print(read_model.occupancy())
    # print(read_model.find_by_room(67))
    # print(read_model.list_guests())

if __name__ == "__main__":
    main()


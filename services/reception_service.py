# hotel/services/reception_service.py
from reception_sys.repos.repo_interface import GuestRepository

class ReceptionService:
    ROOM_MIN = 10
    ROOM_MAX = 100
    ALLOWED_PLANS = (1, 2, 3)

    def __init__(self, repo:GuestRepository):
        self.repo=repo

    def guest_add(self, name, room, plan):
        self._validate_name(name)
        self._validate_room(room)
        self._validate_plan(plan)

        if self.repo.name_exists(name):
            return False, "Guest already exists!"
        if self.repo.room_exists(room):
            return False, "Room already booked!"
        try:
            self.repo.add(name, room, plan)
        except Exception as e:
            return False, "Database error!"
        return True, f"Guest {name} registered successfully!"

    def withdraw_guest(self, name):
        self.repo.soft_delete(name)

        if not self.repo.soft_delete(name):
            return False, f"Unable to delete {name}, not found!"
        return True, f"Guest {name} removed"

    def restore_guest(self, name, room, plan):
        self.repo.restore_guest(name, room, plan)

    # ____________________Validation___________________________

    def _validate_name(self, name: str) -> None:
        if not name or not name.replace(" ", "").isalpha():
            # or not all(part.isalpha() for part in name.split()):
            raise ValueError(f"guest {name} not found!")

    def _validate_room(self, room: int) -> None:
        if not (ReceptionService.ROOM_MIN <= room <= ReceptionService.ROOM_MAX):
            raise ValueError(f"invalid {room} number")

    def _validate_plan(self, plan: int) -> None:
        if plan not in ReceptionService.ALLOWED_PLANS:
            raise ValueError(f"Invalid {plan} selection")



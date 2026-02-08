# import json
# from typing import Dict, Tuple
#
#
# class ReceptionService:
#     ROOM_MIN = 10
#     ROOM_MAX = 100
#
#     ALLOWED_PLANS = (1, 2, 3)
#
#     def __init__(self):
#         self.guests_db: Dict[str, Dict] = {}
#
#     # ---------------- Persistence ----------------
#
#     def save_to_json(self, filename: str = "project_1.json") -> None:
#         with open(filename, "w") as f:
#             json.dump(self.guests_db, f, indent=2)
#
#     def load_from_json(self, filename: str = "project_1.json") -> None:
#         try:
#             with open(filename, "r") as f:
#                 self.guests_db = json.load(f)
#         except FileNotFoundError:
#             self.guests_db = {}
#
#     # ---------------- Business Logic ----------------
#
#     def add_guest(self, name: str, room: int, plan: int) -> Tuple[bool, str]:
#         self._validate_name(name)
#         self._validate_room(room)
#         self._validate_plan(plan)
#
#         if name in self.guests_db:
#             return False, "Guest already exists"
#
#         if room in (g["room"] for g in self.guests_db.values()):
#             return False, "Room already booked"
#
#         self.guests_db[name] = {
#             "room": room,
#             "plan": plan
#         }
#
#         return True, "Guest added successfully"
#
#     def withdraw_guest(self, name: str) -> Tuple[bool, str]:
#         self._validate_name(name)
#
#         if name not in self.guests_db:
#             return False, "Guest not found"
#
#         del self.guests_db[name]
#         return True, "Guest withdrawn successfully"
#
#     # ---------------- Validation ----------------
#
#     def _validate_name(self, name: str) -> None:
#         if not name or not name.replace(" ", "").isalpha():
#             # or not all(part.isalpha() for part in name.split()):
#             raise ValueError("guest name not found!")
#
#     def _validate_room(self, room: int) -> None:
#         if not room.isdigit() or not (ROOM_MIN <= room <= ROOM_MAX):
#             raise ValueError("invalid room number")
#
#     def _validate_plan(self, plan: int) -> None:
#         if plan not in ALLOWED_PLANS:
#             raise ValueError("Invalid plan selection")
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

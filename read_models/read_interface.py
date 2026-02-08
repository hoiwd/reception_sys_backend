
class GuestReadModel:
    def list_guests(self):
        raise NotImplementedError

    def find_by_room(self, room):
        raise NotImplementedError

    def occupancy(self):
        raise  NotImplementedError



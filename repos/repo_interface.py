from abc import ABC, abstractmethod


class GuestRepository(ABC):
    @abstractmethod
    def add(self, name: str, room: int, plan: int)-> None:
        pass

    @abstractmethod
    def name_exists(self, name: str)-> bool:
        pass

    @abstractmethod
    def room_exists(self, room: int)-> bool:
        pass

    @abstractmethod
    def soft_delete(self, name: str)-> bool:
        pass



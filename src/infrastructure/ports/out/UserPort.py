from abc import ABC, abstractmethod
from typing import List
from src.domain.model.User import User


class UserPort(ABC):

    @abstractmethod
    def save_user(self, user: User):
        pass

    @abstractmethod
    def update_user(self, user: User):
        pass

    @abstractmethod
    def delete_user(self, user_id: int):
        pass

    @abstractmethod
    def find_user_by_id(self, user_id: int) -> User:
        pass

    @abstractmethod
    def find_all(self) -> List[User]:
        pass

from abc import ABC, abstractmethod
from typing import List
from src.domain.model.User import User


class UserPort(ABC):

    @abstractmethod
    def create_user(self, user: User):
        pass

    @abstractmethod
    def update_user(self, user: User):
        pass

    @abstractmethod
    def delete_user(self, user_id: int):
        pass

    @abstractmethod
    def get_user(self, user_id: int) -> User:
        pass

    @abstractmethod
    def get_users(self) -> List[User]:
        pass

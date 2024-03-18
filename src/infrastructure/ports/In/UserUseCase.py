from abc import ABC, abstractmethod
from src.domain.model import User


class UserUseCase(ABC):

    @abstractmethod
    def create_user(self, user: User) -> User: pass

    @abstractmethod
    def update_user(self, user_id: int, user: User) -> User: pass

    @abstractmethod
    def delete_user(self, user_id: int) -> None: pass

    @abstractmethod
    def get_user(self, user_id: int) -> User: pass

    @abstractmethod
    def get_users(self) -> list: pass
from src.domain.model import User
from src.infrastructure.ports.In.UserUseCase import UserUseCase
from src.infrastructure.ports.out import UserPort


class UserUseCaseImpl(UserUseCase):
    def __init__(self, user_port: UserPort):
        self.user_port = user_port

    def create_user(self, user: User) -> User:
        return self.user_port.save_user(user)

    def update_user(self, user_id: int, user: User) -> User:
        return self.user_port.update_user(user_id, user)

    def delete_user(self, user_id: int) -> None:
        return self.user_port.delete_user(user_id)

    def get_user(self, user_id: int) -> User:
        return self.user_port.find_user_by_id(user_id)

    def get_users(self) -> list:
        return self.user_port.find_all()

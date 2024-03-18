from src.domain.model import User
from src.infrastructure.ports.In.UserUseCase import UserUseCase
from src.infrastructure.ports.out import UserPort


class UserUseCaseImpl:

    def __init__(self, user_adapter: UserPort):
        self.user_adapter = user_adapter

    def create_user(self, user):
        self.user_adapter.create_user(user)

    def get_users(self):
        return self.user_adapter.get_users()

    def get_user(self, identifier):
        return self.user_adapter.get_user(identifier)

    def get_user_by_email(self, email):
        return self.user_adapter.get_user_by_email(email)

    def update_user(self, identifier, user):
        existing_user = self.user_adapter.get_user(identifier)
        if existing_user:
            self.user_adapter.update_user(identifier, user)
        else:
            raise ValueError("User not found")

    def update_user_by_email(self, email, user):
        existing_user = self.user_adapter.get_user_by_email(email)
        if existing_user:
            self.user_adapter.update_user_by_email(email, user)
        else:
            raise ValueError("User not found")

    def delete_user(self, identifier):
        existing_user = self.user_adapter.get_user(identifier)
        if existing_user:
            self.user_adapter.delete_user(identifier)
        else:
            raise ValueError("User not found")

    def delete_user_by_email(self, email):
        existing_user = self.user_adapter.get_user_by_email(email)
        if existing_user:
            self.user_adapter.delete_user_by_email(email)
        else:
            raise ValueError("User not found")
import logging
from src.domain.model.User import User
from src.infrastructure.adapters.out.ports.In import UserUseCase
from src.infrastructure.adapters.out.ports.out import UserPort


class UserUseCaseImpl:

    def __init__(self, user_adapter: UserPort):
        self.user_adapter = user_adapter

    def create_user(self, user):
        user_id = self.user_adapter.create_user(user)
        if user_id:
            logging.debug(f"Retrieving created user with ID: {user_id}")
            created_user = self.user_adapter.get_user(user_id)
            return created_user
        logging.error("User creation failed; no ID was returned.")
        return None

    def get_user(self, identifier):
        if identifier is None:
            return None  
        if identifier.isdigit():
            return self.user_adapter.get_user(int(identifier))
        else:
            return self.user_adapter.get_user_by_email(identifier)

    def get_users(self):
        return self.user_adapter.get_users()

    def update_user(self, identifier, user):
        existing_user = self.user_adapter.get_user(identifier)
        if existing_user:
            self.user_adapter.update_user(identifier, user)
            return True
        else:
            raise ValueError("User not found")

    def delete_user(self, identifier):
        if identifier.isdigit():
            self.user_adapter.delete_user(int(identifier))
        else:
            self.user_adapter.delete_user_by_email(identifier)

    def update_user_by_email(self, email: str, user: User) -> bool:
        existing_user = self.user_adapter.get_user_by_email(email)
        if existing_user:
            user.id = existing_user.id  
            self.user_adapter.update_user_by_email(email, user)
            return True
        else:
            return False
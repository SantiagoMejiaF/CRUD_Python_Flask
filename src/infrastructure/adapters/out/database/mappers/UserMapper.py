from domain.model.User import User
from infrastructure.adapters.out.database.entities import UserEntity

class UserEntityMappers:
    @staticmethod
    def to_domain(user_entity: UserEntity) -> User:
        return User(
            id=user_entity.id,
            name=user_entity.name,
            email=user_entity.email,
            gender=user_entity.gender,
            status=user_entity.status
        )

    @staticmethod
    def to_entity(user: User) -> UserEntity:
        return UserEntity(
            id=user.id,
            name=user.name,
            email=user.email,
            gender=user.gender,
            status=user.status
        )

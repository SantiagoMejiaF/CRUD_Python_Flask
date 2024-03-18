from src.domain.model.User import User

class DomainResponseMapper:

    @staticmethod
    def from_domain(user: User):
        return {
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'gender': user.gender,
            'status': user.status
        }

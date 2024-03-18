from src.domain.model.User import User

class DomainRequestMapper:
    @staticmethod
    def to_domain(request_object):
        return User(
            id=None,
            name=request_object.name,
            email=request_object.email,
            gender=request_object.gender,
            status=request_object.status
        )

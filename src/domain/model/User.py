class User:
    def __init__(self, id=None, name=None, email=None, gender=None, status=None):
        self.id = id
        self.name = name
        self.email = email
        self.gender = gender
        self.status = status

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'gender': self.gender,
            'status': self.status
        }

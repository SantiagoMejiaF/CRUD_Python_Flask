from flask import jsonify

class UserResponse:
    def __init__(self, user):
        self.user = user

    def to_json(self):
        return jsonify({
            'id': self.user.id,
            'name': self.user.name,
            'email': self.user.email,
            'gender': self.user.gender,
            'status': self.user.status
        })

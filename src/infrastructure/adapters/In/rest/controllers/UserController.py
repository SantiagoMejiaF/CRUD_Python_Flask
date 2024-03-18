from flask import request, jsonify
from flask.views import MethodView
from src.application.usecases.UserUseCaseImpl import UserUseCaseImpl
from src.domain.model.User import User
from src.infrastructure.adapters.out.UserAdapter import UserAdapter

class UserController(MethodView):

    def __init__(self):
        self.user_adapter = UserAdapter()
        self.user_use_case = UserUseCaseImpl(self.user_adapter)

    def post(self):
        user_data = request.get_json()
        user = User(None, user_data['name'], user_data['email'], user_data['gender'], user_data['status'])
        user_id = self.user_use_case.create_user(user)
        return jsonify({'message': 'User created successfully', 'id': user_id}), 201

    def get(self, user_id_or_email=None):
        if user_id_or_email is not None:
            if user_id_or_email.isdigit():
                # Fetch a single user by ID
                user = self.user_use_case.get_user(int(user_id_or_email))
                if user:
                    user_data = {
                        'id': user.id,
                        'name': user.name,
                        'email': user.email,
                        'gender': user.gender,
                        'status': user.status
                    }
                    return jsonify(user_data), 200
                else:
                    return jsonify({'message': 'User not found'}), 404
            else:
                # Fetch a single user by email
                user = self.user_use_case.get_user_by_email(user_id_or_email)
                if user:
                    user_data = {
                        'id': user.id,
                        'name': user.name,
                        'email': user.email,
                        'gender': user.gender,
                        'status': user.status
                    }
                    return jsonify(user_data), 200
                else:
                    return jsonify({'message': 'User not found'}), 404
        else:
            # Fetch all users
            users = self.user_use_case.get_users()
            users_data = [{
                'id': user.id,
                'name': user.name,
                'email': user.email,
                'gender': user.gender,
                'status': user.status
            } for user in users]
            return jsonify(users_data), 200

    def put(self, user_id_or_email):
        user_data = request.get_json()

        if 'name' in user_data:
            user_name = user_data['name']
        else:
            user_name = None

        if user_id_or_email.isdigit():
            user_id = int(user_id_or_email)
            user_email = None
        else:
            user_id = None
            user_email = user_id_or_email

        user_gender = user_data.get('gender')
        user_status = user_data.get('status')

        if user_id is not None:
            user = User(user_id, user_name, user_email, user_gender, user_status)
            self.user_use_case.update_user(user_id, user)
        elif user_email is not None:
            user = User(None, user_name, user_email, user_gender, user_status)
            self.user_use_case.update_user_by_email(user_email, user)

        return jsonify({'message': 'User updated successfully'}), 200



    def delete(self, user_id_or_email):
        if user_id_or_email.isdigit():
            self.user_use_case.delete_user(int(user_id_or_email))
        else:
            self.user_use_case.delete_user_by_email(user_id_or_email)
        return jsonify({'message': 'User deleted successfully'}), 204

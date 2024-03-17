from flask import Flask, request, jsonify
from src.application.usecases.UserUseCaseImpl import UserUseCaseImpl
from src.domain.model.User import User
from src.infrastructure.adapters.out.UserAdapter import UserAdapter


app = Flask(__name__)
user_adapter = UserAdapter()
user_use_case = UserUseCaseImpl(user_adapter)


class UserController:

    @staticmethod
    @app.route('/user', methods=['POST'])
    def create_user():
        user_data = request.get_json()
        user = User(None, user_data['name'], user_data['email'], user_data['gender'], user_data['status'])
        user_use_case.create_user(user)
        return jsonify({'message': 'User created successfully'}), 201

    @staticmethod
    @app.route('/users', methods=['GET'])
    def get_users():
        users = user_use_case.get_users()
        users_data = [{
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'gender': user.gender,
            'status': user.status
        } for user in users]
        return jsonify(users_data)

    @staticmethod
    @app.route('/user/<int:user_id>', methods=['GET'])
    def get_user(user_id):
        user = user_use_case.get_user(user_id)
        if user:
            user_data = {
                'id': user.id,
                'name': user.name,
                'email': user.email,
                'gender': user.gender,
                'status': user.status
            }
            return jsonify(user_data)
        else:
            return jsonify({'message': 'User not found'}), 404

    @staticmethod
    @app.route('/user/<int:user_id>', methods=['PUT'])
    def update_user(user_id):
        user_data = request.get_json()
        user = User(user_id, user_data['name'], user_data['email'], user_data['gender'], user_data['status'])
        user_use_case.update_user(user_id, user)
        return jsonify({'message': 'User updated successfully'}), 200

    @staticmethod
    @app.route('/user/<int:user_id>', methods=['DELETE'])
    def delete_user(user_id):
        user_use_case.delete_user(user_id)
        return jsonify({'message': 'User deleted successfully'})


if __name__ == '__main__':
    app.run(debug=True, port=4000)

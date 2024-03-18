from flask import request, jsonify
from flask.views import MethodView
from src.application.usecases.UserUseCaseImpl import UserUseCaseImpl
from src.infrastructure.adapters.In.rest.mappers.DomainRequestMapper import DomainRequestMapper
from src.infrastructure.adapters.In.rest.mappers.DomainResponseMapper import DomainResponseMapper
from src.infrastructure.adapters.In.rest.controllers.response.UserResponse import UserResponse
from src.infrastructure.adapters.out.UserAdapter import UserAdapter
from src.infrastructure.adapters.In.rest.controllers.request.CreateUserRequest import CreateUserRequest

class UserController(MethodView):

    def __init__(self):
        user_port = UserAdapter() 
        self.user_use_case = UserUseCaseImpl(user_port)

    def post(self):
        data = request.get_json()
        create_user_request = CreateUserRequest(**data)
        user_domain = DomainRequestMapper.to_domain(create_user_request)
        user_created = self.user_use_case.create_user(user_domain)
        
        if user_created:
            response = UserResponse(user_created)
            return response.to_json(), 201
        else:
            return jsonify({'message': 'Failed to create user'}), 500

    def get(self, user_id_or_email=None):
        # Fetching a specific user
        if user_id_or_email:
            user = self.user_use_case.get_user(user_id_or_email)
            if user:
                return jsonify(DomainResponseMapper.from_domain(user)), 200
            else:
                return jsonify({'message': 'User not found'}), 404
        else:
            users = self.user_use_case.get_users()
            if users:
                responses = [DomainResponseMapper.from_domain(user) for user in users]
                return jsonify(responses), 200
            else:
                return jsonify({'message': 'No users found'}), 404

    def put(self, user_id_or_email):
        try:
            data = request.get_json()

            required_fields = ['name', 'email', 'gender', 'status']
            for field in required_fields:
                if field not in data:
                    return jsonify({'message': f'Missing attribute in request: {field}'}), 400

            class RequestObject:
                def __init__(self, name, email, gender, status):
                    self.name = data['name']
                    self.email = data['email']
                    self.gender = data['gender']
                    self.status = data['status']

            user_domain = DomainRequestMapper.to_domain(RequestObject(**data))

            if user_id_or_email.isdigit():
                success = self.user_use_case.update_user(int(user_id_or_email), user_domain)
            else:
                success = self.user_use_case.update_user_by_email(user_id_or_email, user_domain)

            if success:
                return jsonify({'message': 'User updated successfully'}), 200
            else:
                return jsonify({'message': 'User update failed'}), 404

        except ValueError as e:
            return jsonify({'message': str(e)}), 400
        except Exception as e:
            return jsonify({'message': f'Unexpected error: {str(e)}'}), 500

    def delete(self, user_id_or_email):
        self.user_use_case.delete_user(user_id_or_email)
        return jsonify({'message': 'User deleted successfully'}), 204
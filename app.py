from flask import Flask
from src.infrastructure.database.oracle_db import initialize_database
from src.infrastructure.adapters.In.rest.controllers.UserController import UserController

app = Flask(__name__)

# Initialize the database
initialize_database()

# Register the UserController routes
user_view = UserController.as_view('user_api')
app.add_url_rule('/user', view_func=user_view, methods=['POST', 'GET'])
app.add_url_rule('/user/<user_id_or_email>', view_func=user_view, methods=['GET', 'PUT', 'DELETE'])

if __name__ == '__main__':
    app.run(debug=True, port=4000)

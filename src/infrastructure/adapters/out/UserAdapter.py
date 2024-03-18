# Importa get_database_connection desde el módulo correcto
from src.infrastructure.database.oracle_db import get_database_connection
from src.domain.model.User import User
from src.infrastructure.ports.out.UserPort import UserPort

class UserAdapter(UserPort):

    def create_user(self, user):
        connection = get_database_connection()
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO USER_ENTITY (NAME, EMAIL, GENDER, STATUS) 
            VALUES (:name, :email, :gender, :status)
        """, {'name': user.name, 'email': user.email, 'gender': user.gender, 'status': user.status})

        connection.commit()
        cursor.close()
        connection.close()

    def get_users(self):
        connection = get_database_connection()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT ID, NAME, EMAIL, GENDER, STATUS FROM USER_ENTITY
        """)

        users = []
        for row in cursor.fetchall():
            user = User(row[0], row[1], row[2], row[3], row[4])
            users.append(user)

        cursor.close()
        connection.close()

        return users

    def get_user(self, identifier):
        connection = get_database_connection()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT ID, NAME, EMAIL, GENDER, STATUS FROM USER_ENTITY WHERE ID = :id
        """, {'id': identifier})

        row = cursor.fetchone()
        if row:
            user = User(row[0], row[1], row[2], row[3], row[4])
        else:
            user = None

        cursor.close()
        connection.close()

        return user

    def get_user_by_email(self, email):
        connection = get_database_connection()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT ID, NAME, EMAIL, GENDER, STATUS FROM USER_ENTITY WHERE EMAIL = :email
        """, {'email': email})

        row = cursor.fetchone()
        if row:
            user = User(row[0], row[1], row[2], row[3], row[4])
        else:
            user = None

        cursor.close()
        connection.close()

        return user

    def update_user(self, identifier, user):
        connection = get_database_connection()
        cursor = connection.cursor()

        cursor.execute("""
            UPDATE USER_ENTITY SET NAME = :name, EMAIL = :email, GENDER = :gender, STATUS = :status 
            WHERE ID = :id
        """, {'name': user.name, 'email': user.email, 'gender': user.gender, 'status': user.status, 'id': identifier})

        connection.commit()
        cursor.close()
        connection.close()

    def update_user_by_email(self, email, user):
        connection = get_database_connection()
        cursor = connection.cursor()

        cursor.execute("""
            UPDATE USER_ENTITY SET NAME = :name, EMAIL = :email, GENDER = :gender, STATUS = :status 
            WHERE EMAIL = :email
        """, {'name': user.name, 'email': user.email, 'gender': user.gender, 'status': user.status})

        connection.commit()
        cursor.close()
        connection.close()

    def delete_user(self, identifier):
        connection = get_database_connection()
        cursor = connection.cursor()

        cursor.execute("""
            DELETE FROM USER_ENTITY WHERE ID = :id
        """, {'id': identifier})

        connection.commit()
        cursor.close()
        connection.close()

    def delete_user_by_email(self, email):
        connection = get_database_connection()
        cursor = connection.cursor()

        cursor.execute("""
            DELETE FROM USER_ENTITY WHERE EMAIL = :email
        """, {'email': email})

        connection.commit()
        cursor.close()
        connection.close()
from typing import List

import oracledb
from .ports.out.UserPort import UserPort
from src.infrastructure.database.oracle_db import get_database_connection
from src.domain.model.User import User

class UserAdapter(UserPort):

        def create_user(self, user: User) -> int:
            connection = get_database_connection()
            cursor = connection.cursor()
            try:
                sql = """
                    INSERT INTO USER_ENTITY (NAME, EMAIL, GENDER, STATUS) 
                    VALUES (:name, :email, :gender, :status)
                    RETURNING ID INTO :id
                """
                # The variable to capture the returned ID
                id_var = cursor.var(oracledb.NUMBER)
                cursor.execute(sql, {
                    'name': user.name, 
                    'email': user.email, 
                    'gender': user.gender, 
                    'status': user.status,
                    'id': id_var
                })
                # Get the actual ID from the cursor
                user_id = id_var.getvalue()[0]  # Assuming the ID is the first element in a list
                connection.commit()
                return user_id
            except Exception as e:
                print(f"Error inserting user: {e}")
                return None
            finally:
                cursor.close()
                connection.close()

        def get_user(self, user_id: int) -> User:
            connection = get_database_connection()
            try:
                with connection.cursor() as cursor:
                    cursor.execute("""
                        SELECT ID, NAME, EMAIL, GENDER, STATUS
                        FROM USER_ENTITY
                        WHERE ID = :id
                    """, {'id': user_id})
                    row = cursor.fetchone()
                    if row:
                        return User(id=row[0], name=row[1], email=row[2], gender=row[3], status=row[4])
                    return None
            finally:
                connection.close()

        def get_user_by_email(self, email: str) -> User:
            connection = get_database_connection()
            try:
                with connection.cursor() as cursor:
                    cursor.execute("""
                        SELECT ID, NAME, EMAIL, GENDER, STATUS
                        FROM USER_ENTITY
                        WHERE EMAIL = :email
                    """, {'email': email})
                    row = cursor.fetchone()
                    if row:
                        return User(id=row[0], name=row[1], email=row[2], gender=row[3], status=row[4])
                    return None
            finally:
                connection.close()

        def update_user(self, user_id: int, user: User):
            connection = get_database_connection()
            try:
                with connection.cursor() as cursor:
                    cursor.execute("""
                        UPDATE USER_ENTITY
                        SET NAME = :name, EMAIL = :email, GENDER = :gender, STATUS = :status
                        WHERE ID = :id
                    """, {
                        'id': user_id,
                        'name': user.name,
                        'email': user.email,
                        'gender': user.gender,
                        'status': user.status
                    })
                    connection.commit()
            finally:
                connection.close()

        def delete_user(self, user_id: int):
            connection = get_database_connection()
            try:
                with connection.cursor() as cursor:
                    cursor.execute("""
                        DELETE FROM USER_ENTITY
                        WHERE ID = :id
                    """, {'id': user_id})
                    connection.commit()
            finally:
                connection.close()

        def get_users(self) -> List[User]:
            connection = get_database_connection()
            try:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT ID, NAME, EMAIL, GENDER, STATUS FROM USER_ENTITY")
                    return [
                        User(id=row[0], name=row[1], email=row[2], gender=row[3], status=row[4])
                        for row in cursor
                    ]
            finally:
                connection.close()

        def delete_user_by_email(self, email: str):
            connection = get_database_connection()
            try:
                with connection.cursor() as cursor:
                    cursor.execute("""
                        DELETE FROM USER_ENTITY
                        WHERE EMAIL = :email
                    """, {'email': email})
                    connection.commit()
            finally:
                connection.close()

        def update_user_by_email(self, email: str, user: User):
            connection = get_database_connection()
            try:
                with connection.cursor() as cursor:
                    cursor.execute("""
                        UPDATE USER_ENTITY
                        SET NAME = :name, EMAIL = :email, GENDER = :gender, STATUS = :status
                        WHERE EMAIL = :email
                    """, {
                        'name': user.name,
                        'email': email,
                        'gender': user.gender,
                        'status': user.status
                    })
                    connection.commit()
            finally:
                connection.close()
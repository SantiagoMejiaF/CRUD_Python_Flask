from infrastructure.adapters.out.database.mappers import UserDatabaseMapper
from infrastructure.database.oracle_db import get_database_connection

class UserRepository:
    def create_user(self, user_data: dict) -> int:
        connection = get_database_connection()
        cursor = connection.cursor()
        try:
            sql = """
                INSERT INTO USER_TABLE (NAME, EMAIL, GENDER, STATUS) 
                VALUES (:name, :email, :gender, :status)
                RETURNING ID INTO :id
            """
            cursor.execute(sql, {
                'name': user_data['name'],
                'email': user_data['email'],
                'gender': user_data['gender'],
                'status': user_data['status'],
                'id': user_data['id']
            })
            user_id = cursor.fetchone()[0]
            connection.commit()
            return user_id
        except Exception as e:
            print(f"Error inserting user: {e}")
            return None
        finally:
            cursor.close()
            connection.close()

    def get_user_by_id(self, user_id: int) -> dict:
        connection = get_database_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT ID, NAME, EMAIL, GENDER, STATUS
                    FROM USER_TABLE
                    WHERE ID = :id
                """, {'id': user_id})
                row = cursor.fetchone()
                if row:
                    return UserDatabaseMapper.map_row_to_user_dict(row)
                return None
        finally:
            connection.close()

    def update_user(self, user_id: int, user_data: dict) -> None:
        connection = get_database_connection()
        cursor = connection.cursor()
        try:
            sql = """
                UPDATE USER_TABLE
                SET NAME = :name, EMAIL = :email, GENDER = :gender, STATUS = :status
                WHERE ID = :id
            """
            cursor.execute(sql, {
                'id': user_id,
                'name': user_data['name'],
                'email': user_data['email'],
                'gender': user_data['gender'],
                'status': user_data['status']
            })
            connection.commit()
        except Exception as e:
            print(f"Error updating user: {e}")
        finally:
            cursor.close()
            connection.close()

    def delete_user(self, user_id: int) -> None:
        connection = get_database_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("""
                DELETE FROM USER_TABLE
                WHERE ID = :id
            """, {'id': user_id})
            connection.commit()
        except Exception as e:
            print(f"Error deleting user: {e}")
        finally:
            cursor.close()
            connection.close()

    def get_all_users(self) -> list:
        connection = get_database_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT ID, NAME, EMAIL, GENDER, STATUS FROM USER_TABLE")
                rows = cursor.fetchall()
                return [UserDatabaseMapper.map_row_to_user_dict(row) for row in rows]
        finally:
            connection.close()
from src.database import get_database_connection
from src.domain.model.User import User
from src.infrastructure.ports.out.UserPort import UserPort


class UserAdapter(UserPort):

    def save_user(self, user: User):
        database = get_database_connection()
        cursor = database.cursor()
        sql = "INSERT INTO USER_ENTITY (NAME, EMAIL, GENDER, STATUS) VALUES (:1, :2, :3, :4)"
        cursor.execute(sql, (user.name, user.email, user.gender, user.status))
        database.commit()
        cursor.close()

    def update_user(self, user_id: int, user: User):
        database = get_database_connection()
        cursor = database.cursor()
        sql = """
               UPDATE USER_ENTITY
               SET NAME = :1, EMAIL = :2, GENDER = :3, STATUS = :4
               WHERE ID = :5
           """
        cursor.execute(sql, (user.name, user.email, user.gender, user.status, user_id))
        database.commit()
        cursor.close()

    def delete_user(self, user_id: int):
        database = get_database_connection()
        cursor = database.cursor()
        sql = "DELETE FROM USER_ENTITY WHERE ID = :1"
        cursor.execute(sql, (user_id,))
        database.commit()
        cursor.close()

    def find_user_by_id(self, user_id: int) -> User:
        database = get_database_connection()
        cursor = database.cursor()
        sql = "SELECT ID, NAME, EMAIL, GENDER, STATUS FROM USER_ENTITY WHERE ID = :1"
        cursor.execute(sql, (user_id,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return User(id=row[0], name=row[1], email=row[2], gender=row[3], status=row[4])
        else:
            return None

    def find_all(self) -> list:
        database = get_database_connection()
        cursor = database.cursor()
        sql = "SELECT ID, NAME, EMAIL, GENDER, STATUS FROM USER_ENTITY"
        cursor.execute(sql)
        rows = cursor.fetchall()
        cursor.close()
        return [User(id=row[0], name=row[1], email=row[2], gender=row[3], status=row[4]) for row in rows]

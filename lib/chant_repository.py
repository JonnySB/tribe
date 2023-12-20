from lib.chant import Chant
from lib.user import User


class ChantRepository:
    def __init__(self, connection):
        self._connection = connection

    # When this method is called, all chants are returned as chant objects
    def all(self):
        rows = self._connection.execute(
            "SELECT chants.id AS chant_id, message, date_created, "
            "users.id AS user_id, email, password_hash, name, username "
            "FROM chants "
            "LEFT OUTER JOIN users ON chants.user_id = users.id "
            "ORDER BY date_created DESC;"
        )
        chant_user_list = []
        for row in rows:
            chant_user_list.append(
                [
                    Chant(
                        row["chant_id"],
                        row["message"],
                        row["date_created"],
                        row["user_id"],
                    ),
                    User(
                        row["user_id"],
                        row["email"],
                        row["password_hash"],
                        row["name"],
                        row["username"],
                    ),
                ]
            )

        return chant_user_list

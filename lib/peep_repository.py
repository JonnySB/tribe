from lib.peep import Peep
from lib.user import User


class PeepRepository:
    def __init__(self, connection):
        self._connection = connection

    # When this method is called, all peeps are returned as peep objects
    def all(self):
        rows = self._connection.execute(
            "SELECT peeps.id AS peep_id, message, date_created, "
            "users.id AS user_id, email, password, name, username "
            "FROM peeps "
            "LEFT OUTER JOIN users ON peeps.user_id = users.id "
            "ORDER BY date_created DESC;"
        )
        peep_user_list = []
        for row in rows:
            peep_user_list.append(
                [
                    Peep(
                        row["peep_id"],
                        row["message"],
                        row["date_created"],
                        row["user_id"],
                    ),
                    User(
                        row["user_id"],
                        row["email"],
                        row["password"],
                        row["name"],
                        row["username"],
                    ),
                ]
            )

        return peep_user_list

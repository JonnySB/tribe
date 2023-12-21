from lib.user import User


class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    # When the all method is called
    # returns a list of all users as user objects
    def all(self):
        rows = self._connection.execute("SELECT * FROM users")
        users = []
        for row in rows:
            users.append(
                User(
                    row["id"],
                    row["email"],
                    row["password_hash"],
                    row["name"],
                    row["username"],
                )
            )
        return users

    # When passed a user object,
    # A corresponding database record is created
    # And a user object with updated ID is returned
    def add(self, user):
        rows = self._connection.execute(
            "INSERT INTO users (email, password_hash, name, username) \
            VALUES (%s, %s, %s, %s) RETURNING id;",
            [user.email, user.password_hash, user.name, user.username],
        )
        user.id = rows[0]["id"]
        return user

    def get_user(self, id):
        rows = self._connection.execute("SELECT * FROM users WHERE id = %s", [id])
        row = rows[0]
        return User(
            row["id"], row["email"], row["password_hash"], row["name"], row["username"]
        )

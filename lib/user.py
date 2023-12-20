from passlib.hash import bcrypt


class User:
    def __init__(self, id, email, password, name, username):
        self.id = id
        self.email = email
        self.password_hash = self._hash_password(password)
        self.name = name
        self.username = username

    def __eq__(self, other):
        return all(
            [
                self.id == other.id,
                self.email == other.email,
                self.name == other.name,
                self.username == other.username,
            ]
        )

    def __repr__(self):
        return f"User({self.id}, {self.email}, {self.name}, {self.username})"

    def _hash_password(self, password):
        return bcrypt.hash(password)

    def _is_password(self, password):
        return bcrypt.verify(password, self.password_hash)

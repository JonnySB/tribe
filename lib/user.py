import bcrypt


class User:
    def __init__(self, id, email, password, name, username):
        self.id = id
        self.email = email
        self.password_hash = self._hash_password(password)
        self.name = name
        self.username = username

    def __eq__(self, other):
        # Note, password not included due to hashing
        return all(
            [
                self.id == other.id,
                self.email == other.email,
                self.name == other.name,
                self.username == other.username,
            ]
        )

    def __repr__(self):
        # Note, password hash not included in representation
        return f"User({self.id}, {self.email}, {self.name}, {self.username})"

    def _hash_password(self, password):
        password_bytes = password.encode("utf-8")
        salt = bcrypt.gensalt()
        password_hash = bcrypt.hashpw(password_bytes, salt)
        return password_hash

    def is_password(self, test_password):
        test_password_bytes = test_password.encode("utf-8")
        return bcrypt.checkpw(test_password_bytes, self.password_hash)

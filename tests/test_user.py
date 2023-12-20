from passlib.hash import bcrypt
from lib.user import User


# test user constructs properly when passed an id, email, password,
# name and username.
def test_construct_user():
    user = User(1, "test@example.com", "password123", "Joe Blogs", "joey-the-blog")

    assert user.id == 1
    assert user.email == "test@example.com"
    assert bcrypt.verify("password123", user.password_hash)
    assert user.name == "Joe Blogs"
    assert user.username == "joey-the-blog"


def test_eq():
    user1 = User(1, "test@example.com", "password123", "Joe Blogs", "joey-the-blog")
    user2 = User(1, "test@example.com", "password123", "Joe Blogs", "joey-the-blog")
    assert user1 == user2


def test_repr():
    user = User(1, "test@example.com", "password123", "Joe Blogs", "joey-the-blog")
    assert str(user) == "User(1, test@example.com, Joe Blogs, joey-the-blog)"

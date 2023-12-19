from lib.user import User
from lib.user_repository import UserRepository


# When I call the method UserRepository#all
# A list of all users is returned
def test_get_all(db_connection):
    db_connection.seed("seeds/tribe.sql")
    user_repository = UserRepository(db_connection)
    rows = user_repository.all()

    assert rows == [
        User(1, "alice.smith@example.com", "password", "Alice Smith", "alicesmith_23"),
        User(2, "bob.johnson@example.com", "password", "Bob Johnson", "bobjohn89"),
        User(
            3, "elena.garcia@example.com", "password", "Elena Garcia", "elenagarcia23"
        ),
        User(4, "maxwell.lee@example.com", "password", "Maxwell Lee", "maxwell_l"),
        User(5, "sophie.patel@example.com", "password", "Sophie Patel", "sophiep_123"),
    ]


# When I call the method UserRepository#create
# And pass a user object along with it
# A new record is created in the database
# And a user object with updated ID is returned
def test_create_user(db_connection):
    db_connection.seed("seeds/tribe.sql")
    user_repository = UserRepository(db_connection)

    user = User(None, "test@example.com", "password", "Joe blogs", "joe-the-blog")
    user = user_repository.add(user)

    assert user.id == 6

    rows = user_repository.all()

    assert rows == [
        User(1, "alice.smith@example.com", "password", "Alice Smith", "alicesmith_23"),
        User(2, "bob.johnson@example.com", "password", "Bob Johnson", "bobjohn89"),
        User(
            3, "elena.garcia@example.com", "password", "Elena Garcia", "elenagarcia23"
        ),
        User(4, "maxwell.lee@example.com", "password", "Maxwell Lee", "maxwell_l"),
        User(5, "sophie.patel@example.com", "password", "Sophie Patel", "sophiep_123"),
        User(6, "test@example.com", "password", "Joe blogs", "joe-the-blog"),
    ]

from lib.peep_repository import PeepRepository
from lib.peep import Peep
from lib.user import User
from datetime import datetime


# test whether a list of peeps with the corresponding user is returned
def test_get_all_peeps_with_associated_user(db_connection):
    db_connection.seed("seeds/chitter.sql")
    peep_repository = PeepRepository(db_connection)

    rows = peep_repository.all()

    assert rows == [
        [
            Peep(10, "Chasing dreams!", datetime(2023, 12, 10, 22, 0, 0), 5),
            User(
                5, "sophie.patel@example.com", "password", "Sophie Patel", "sophiep_123"
            ),
        ],
        [
            Peep(9, "Having a productive day.", datetime(2023, 12, 9, 20, 10, 0), 4),
            User(4, "maxwell.lee@example.com", "password", "Maxwell Lee", "maxwell_l"),
        ],
        [
            Peep(
                8,
                "Learning something new every day.",
                datetime(2023, 12, 8, 18, 45, 00),
                3,
            ),
            User(
                3,
                "elena.garcia@example.com",
                "password",
                "Elena Garcia",
                "elenagarcia23",
            ),
        ],
        [
            Peep(7, "Exploring new ideas.", datetime(2023, 12, 7, 16, 0, 00), 2),
            User(2, "bob.johnson@example.com", "password", "Bob Johnson", "bobjohn89"),
        ],
        [
            Peep(6, "Coding non-stop!", datetime(2023, 12, 6, 14, 30, 0), 1),
            User(
                1, "alice.smith@example.com", "password", "Alice Smith", "alicesmith_23"
            ),
        ],
        [
            Peep(5, "Enjoying the weekend.", datetime(2023, 12, 5, 13, 0, 0), 5),
            User(
                5, "sophie.patel@example.com", "password", "Sophie Patel", "sophiep_123"
            ),
        ],
        [
            Peep(4, "Working on a new project.", datetime(2023, 12, 4, 11, 20, 0), 4),
            User(4, "maxwell.lee@example.com", "password", "Maxwell Lee", "maxwell_l"),
        ],
        [
            Peep(3, "Just saying hi!", datetime(2023, 12, 3, 10, 15, 0), 3),
            User(
                3,
                "elena.garcia@example.com",
                "password",
                "Elena Garcia",
                "elenagarcia23",
            ),
        ],
        [
            Peep(2, "Feeling great today.", datetime(2023, 12, 2, 9, 45, 0), 2),
            User(2, "bob.johnson@example.com", "password", "Bob Johnson", "bobjohn89"),
        ],
        [
            Peep(1, "Hello!", datetime(2023, 12, 1, 8, 30, 0), 1),
            User(
                1, "alice.smith@example.com", "password", "Alice Smith", "alicesmith_23"
            ),
        ],
    ]

from lib.peep import Peep
from datetime import datetime


## Test that peep constructs properly
def test_peep_constructor():
    peep = Peep(
        2,
        "This is a peep",
        datetime(2023, 12, 5, 12, 53, 0),
        1,
    )
    assert peep.id == 2
    assert peep.message == "This is a peep"
    assert peep.date_created == datetime(2023, 12, 5, 12, 53, 0)
    assert peep.user_id == 1


# test that two peeps with identical attributes are found equal
def test_peep_eq():
    peep1 = Peep(
        2,
        "This is a peep",
        datetime(2023, 12, 5, 12, 53, 0),
        1,
    )
    peep2 = Peep(
        2,
        "This is a peep",
        datetime(2023, 12, 5, 12, 53, 0),
        1,
    )
    assert peep1 == peep2


# test peep is printed nicely as a string
def test_peep_repr():
    peep = Peep(
        2,
        "This is a peep",
        datetime(2023, 12, 5, 12, 53, 0),
        1,
    )
    assert str(peep) == "Peep(2, This is a peep, 2023-12-05 12:53:00, 1)"

from lib.chant import Chant
from datetime import datetime


## Test that chant constructs properly
def test_chant_constructor():
    chant = Chant(
        2,
        "This is a chant",
        datetime(2023, 12, 5, 12, 53, 0),
        1,
    )
    assert chant.id == 2
    assert chant.message == "This is a chant"
    assert chant.date_created == datetime(2023, 12, 5, 12, 53, 0)
    assert chant.user_id == 1


# test that two chants with identical attributes are found equal
def test_chant_eq():
    chant1 = Chant(
        2,
        "This is a chant",
        datetime(2023, 12, 5, 12, 53, 0),
        1,
    )
    chant2 = Chant(
        2,
        "This is a chant",
        datetime(2023, 12, 5, 12, 53, 0),
        1,
    )
    assert chant1 == chant2


# test chant is printed nicely as a string
def test_chant_repr():
    chant = Chant(
        2,
        "This is a chant",
        datetime(2023, 12, 5, 12, 53, 0),
        1,
    )
    assert str(chant) == "Chant(2, This is a chant, 2023-12-05 12:53:00, 1)"

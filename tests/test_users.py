import pytest

from users import phoner, registration


def test_registration():
    users = []
    registration(users, "Анна", "+7 (900) 123-45-67")
    assert users[0]["phone"] == "+79001234567"


def test_registration_bad_phone():
    users = []
    with pytest.raises(ValueError):
        registration(users, "Пётр", "12345")


def test_registration_duplicate_name():
    users = []
    registration(users, "Анна", "89001234567")
    with pytest.raises(ValueError):
        registration(users, "анна", "89005554433")


def test_phoner():
    users = []
    registration(users, "Иван", "8-912-555-44-33")
    assert phoner(users, "Иван") == "89125554433"
    assert phoner(users, "Пётр") is None

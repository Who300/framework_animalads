from datetime import date

import pytest

from ads import create_ad, delete_ad, stat_counter, searcher
from users import registration


def make_data():
    users = []
    ads = []
    registration(users, "Анна", "89001234567")
    create_ad(ads, users, "Анна", "Кошка", "Парк Горького", date(2026, 9, 20))
    create_ad(ads, users, "Анна", "Собака", "ул. Ленина", date(2026, 9, 22))
    return users, ads


def test_create_ad_unregistered():
    users, ads = make_data()
    with pytest.raises(ValueError):
        create_ad(ads, users, "Пётр", "Попугай", "Двор", date(2026, 9, 21))


def test_searcher():
    _, ads = make_data()
    assert len(searcher(ads, "парк")) == 1


def test_delete_ad():
    _, ads = make_data()
    assert delete_ad(ads, 1, "Анна")
    assert len(ads) == 1


def test_delete_foreign_ad():
    _, ads = make_data()
    assert not delete_ad(ads, 1, "Иван")


def test_stat_counter():
    _, ads = make_data()
    assert stat_counter(ads) == {"кошка": 1, "собака": 1}

import re
from datetime import date

users = []
ads = []

def find_user(name):
    for user in users:
        if user[0] == name:
            return user
    return None

def registration(name, phone):
    cleaned = re.sub(r'[\s\-\(\)]', '', phone)
    pattern = re.compile(r'^(?:\+7|7|8)?(9\d{9})$')
    if not pattern.match(cleaned):
        print(f"Некорректный номер телефона: {phone}")
        return False
    if find_user(name):
        print(f"Пользователь {name} уже зарегистрирован")
        return False
    users.append([name, cleaned])
    print(f"Пользователь {name} зарегистрирован")
    return True

def get_phone(name):
    user = find_user(name)
    if user:
        print(f"Телефон пользователя {name}: {user[1]}")
        return user[1]
    print(f"Пользователь {name} не найден")
    return None


def create_ad(name, animal, place, found_date):
    if not find_user(name):
        print(f"Нельзя создать объявление: {name} не зарегистрирован")
        return False
    ads.append([name, animal, place, found_date])
    print(f"Объявление от {name} создано")
    return True


def get_ads(name):
    found = False
    for ad in ads:
        if ad[0] == name:
            print(f"{ad[1]}, найдено: {ad[2]}, дата: {ad[3]}")
            found = True
    if not found:
        print(f"У пользователя {name} нет объявлений")


registration("Анна", "+7 (900) 123-45-67")
registration("Иван", "8-912-555-44-33")
registration("Пётр", "12345")

get_phone("Анна")
get_phone("Пётр")

create_ad("Анна", "Рыжая кошка", "Парк Горького", date(2026, 9, 20))
create_ad("Анна", "Белая собака", "ул. Ленина, 10", date(2026, 9, 22))
create_ad("Пётр", "Попугай", "Двор дома 5", date(2026, 9, 21))

get_ads("Анна")
get_ads("Иван")

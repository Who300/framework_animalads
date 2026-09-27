from utils import phone_cleaner, next_id


def find_user(users: list[dict], name: str) -> dict | None:
    return next(
        (user for user in users if user["name"].lower() == name.lower()),
        None,
    )


def registration(users: list[dict], name: str, phone: str) -> dict:
    cleaned = phone_cleaner(phone)
    if find_user(users, name):
        raise ValueError(f"Пользователь {name} уже зарегистрирован")
    user = {"id": next_id(users), "name": name, "phone": cleaned}
    users.append(user)
    return user


def phoner(users: list[dict], name: str) -> str | None: #найти телефончик пользователя
    user = find_user(users, name)
    if user is None:
        return None
    return user["phone"]

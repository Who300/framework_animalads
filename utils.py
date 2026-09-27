import re
from datetime import date, datetime

PHONE_PATTERN = re.compile(r"^(?:\+7|7|8)?(9\d{9})$") #формат рос телефона
DATE_FORMAT = "%d.%m.%Y"


def phone_cleaner(phone: str) -> str:
    cleaned = re.sub(r"[\s\-\(\)]", "", phone)
    if not PHONE_PATTERN.match(cleaned):
        raise ValueError(f"Некорректный номер телефона: {phone}")
    return cleaned


def next_id(items: list[dict]) -> int:
    return max((item["id"] for item in items), default=0) + 1


def input_text(prompt: str) -> str:
    """Запросить непустую строку."""
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("Значение не может быть пустым")


def input_int(prompt: str) -> int:
    """Запросить целое число."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Введите целое число")


def input_date(prompt: str) -> date:
    """Запросить дату в формате ДД.ММ.ГГГГ."""
    while True:
        try:
            return datetime.strptime(input(prompt), DATE_FORMAT).date()
        except ValueError:
            print("Введите дату в формате ДД.ММ.ГГГГ, например 20.09.2026")

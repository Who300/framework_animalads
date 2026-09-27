from collections.abc import Iterator
from datetime import date

from users import find_user
from utils import next_id


def create_ad(
    ads: list[dict],
    users: list[dict],
    author: str,
    animal: str,
    place: str,
    found_date: date,
) -> dict:

    if find_user(users, author) is None:
        raise ValueError(f"Пользователь {author} не зарегистрирован")
    if found_date > date.today():
        raise ValueError("Дата находки не может быть в будущем")

    ad = {
        "id": next_id(ads),
        "author": author,
        "animal": animal,
        "place": place,
        "found_date": found_date.isoformat(),
    }
    ads.append(ad)
    return ad


def delete_ad(ads: list[dict], ad_id: int, author: str) -> bool:
    for ad in ads:
        if ad["id"] == ad_id and ad["author"].lower() == author.lower():
            ads.remove(ad)
            return True
    return False


def author_ads(ads: list[dict], author: str) -> Iterator[dict]:
    """Генератор: отдаёт объявления указанного автора."""
    for ad in ads:
        if ad["author"].lower() == author.lower():
            yield ad


def searcher(ads: list[dict], query: str) -> list[dict]:
    query = query.lower()
    return [
        ad for ad in ads
        if query in ad["animal"].lower() or query in ad["place"].lower()
    ]


def date_sorter(ads: list[dict]) -> list[dict]:
    return sorted(ads, key=lambda ad: ad["found_date"], reverse=True)


def stat_counter(ads: list[dict]) -> dict[str, int]:
    stats: dict[str, int] = {}
    for ad in ads:
        animal = ad["animal"].lower()
        stats[animal] = stats.get(animal, 0) + 1
    return stats


def format_ad(ad: dict) -> str:
    """Вернуть объявление в виде строки."""
    found = date.fromisoformat(ad["found_date"]).strftime("%d.%m.%Y")
    return (f"№{ad['id']} | {ad['animal']} | {ad['place']} | "
            f"{found} | автор: {ad['author']}")

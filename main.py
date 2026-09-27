"""Точка запуска: меню системы объявлений."""

import inspect

import ads as ads_module
from ads import (author_ads, create_ad, date_sorter, delete_ad, format_ad,
                 searcher, stat_counter)
from storage import ADS_FILE, USERS_FILE, load_data, save_data
from users import phoner, registration
from utils import input_date, input_int, input_text

MENU = """
=== Объявления о найденных животных ===
1. Зарегистрироваться
2. Показать все объявления
3. Создать объявление
4. Найти объявление
5. Объявления пользователя
6. Связаться с автором
7. Удалить объявление
8. Статистика
9. Справка по функциям
0. Выход"""


def show_ads(ads: list[dict]) -> None:
    if not ads:
        print("Объявлений нет")
        return
    for ad in ads:
        print(format_ad(ad))


def show_stat(ads: list[dict]) -> None:
    stats = stat_counter(ads)
    print(f"Всего объявлений: {len(ads)}")
    for animal, count in sorted(stats.items(), key=lambda item: -item[1]):
        print(f"  {animal}: {count}")


def helper() -> None:
    for name, func in inspect.getmembers(ads_module, inspect.isfunction):
        if func.__module__ == ads_module.__name__:
            print(f"{name}{inspect.signature(func)}")
            print(f"    {func.__doc__}")


def registrator(users: list[dict]) -> None:
    name = input_text("Имя: ")
    phone = input_text("Телефон: ")
    try:
        registration(users, name, phone)
    except ValueError as error:
        print(error)
        return
    save_data(USERS_FILE, users)
    print(f"Пользователь {name} зарегистрирован")


def ad_creator(ads: list[dict], users: list[dict]) -> None:
    author = input_text("Ваше имя: ")
    animal = input_text("Какое животное нашли: ")
    place = input_text("Где нашли: ")
    found_date = input_date("Дата находки (ДД.ММ.ГГГГ): ")
    try:
        ad = create_ad(ads, users, author, animal, place, found_date)
    except ValueError as error:
        print(error)
        return
    save_data(ADS_FILE, ads)
    print(f"Объявление №{ad['id']} создано")


def contacter(users: list[dict]) -> None:
    name = input_text("Имя автора: ")
    phone = phoner(users, name)
    if phone is None:
        print(f"Пользователь {name} не найден")
    else:
        print(f"Телефон пользователя {name}: {phone}")


def ad_remover(ads: list[dict]) -> None:
    author = input_text("Ваше имя: ")
    ad_id = input_int("Номер объявления: ")
    if delete_ad(ads, ad_id, author):
        save_data(ADS_FILE, ads)
        print(f"Объявление №{ad_id} удалено")
    else:
        print("Объявление не найдено или принадлежит другому автору")


def main() -> None:
    users = load_data(USERS_FILE)
    ads = load_data(ADS_FILE)

    while True:
        print(MENU)
        choice = input("Выберите действие: ").strip()
        if choice == "1":
            registrator(users)
        elif choice == "2":
            show_ads(date_sorter(ads))
        elif choice == "3":
            ad_creator(ads, users)
        elif choice == "4":
            show_ads(searcher(ads, input_text("Что ищем: ")))
        elif choice == "5":
            show_ads(list(author_ads(ads, input_text("Имя автора: "))))
        elif choice == "6":
            contacter(users)
        elif choice == "7":
            ad_remover(ads)
        elif choice == "8":
            show_stat(ads)
        elif choice == "9":
            helper()
        elif choice == "0":
            print("До свидания!")
            break
        else:
            print("Нет такого пункта меню")


if __name__ == "__main__":
    main()

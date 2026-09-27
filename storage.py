import json
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"
USERS_FILE = DATA_DIR / "users.json"
ADS_FILE = DATA_DIR / "ads.json"


def load_data(filename: Path) -> list[dict]:
    try:
        with open(filename, encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"Файл {filename.name} не найден, начинаем с пустого списка")
        return []
    except json.JSONDecodeError:
        print(f"Файл {filename.name} повреждён, начинаем с пустого списка")
        return []
    if not isinstance(data, list):
        print(f"В файле {filename.name} неверный формат данных")
        return []
    return data


def save_data(filename: Path, data: list[dict]) -> bool:
    try:
        filename.parent.mkdir(exist_ok=True)
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    except OSError as error:
        print(f"Не удалось сохранить {filename.name}: {error}")
        return False
    return True

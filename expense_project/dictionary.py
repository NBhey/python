import json

FILE_PATH = 'dictionary.json'


def load_dict(path: str) -> dict[str, str]:
    """Загружает словарь английский -> русский, в случае отсутствия файла или некорректного JSON
    возвращает пустой словарь
    """
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except json.JSONDecodeError:
        print('Неверный формат json, возвращен пустой словарь')
        return {}
    except FileNotFoundError:
        print('Такого файла не существует, возвращен пустой словарь')
        return {}


def save_dict(path: str, data: dict[str, str]) -> None:
    """Сохраняет новый словарь """
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


dictionary = load_dict(FILE_PATH)
english_word = input('Введите английское слово: ').lower().strip()

if english_word in dictionary:
    print(dictionary[english_word])
else:
    new_english_word = input('Введите перевод этого слова: ').lower().strip()
    dictionary[english_word] = new_english_word

save_dict(FILE_PATH, dictionary)

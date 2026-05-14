FILE_PATH = 'log.txt'


def load_entries(path: str) -> list[str]:
    """Загрузить список записей из файла. Если файла нет — пустой список."""
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return [line.rstrip() for line in file]
    except FileNotFoundError:
        return []


def save_entries(path: str, entries: list[str]) -> None:
    """Перезаписать файл текущим списком записей, по одной на строку."""
    with open(path, 'w', encoding='utf-8') as file:
        for entry in entries:
            file.write(entry + '\n')


deal_list = load_entries(FILE_PATH)
deal = input('Введите запись: ')
deal_list.append(deal)
save_entries(FILE_PATH, deal_list)

for index, entry in enumerate(deal_list, start=1):
    print(f'{index}. {entry}')

import json

FILE_PATH = 'expenses.json'


def format_expense(expense: dict) -> str:
    """Форматирует расход в строку для вывода."""
    return f'- {expense["category"]}, {expense["amount"]} руб, {expense["description"]}'


def matches_filters(expense: dict, *, limit: int | float, category: str | None) -> bool:
    """Проверяет соответствие расхода категории и лимиту."""
    return (category is None or expense['category'] == category) and expense['amount'] >= limit


def filter_expenses(expenses: list, *, limit: int | float = 0, category: str | None = None) -> list:
    """Возвращает расходы с суммой не меньше limit и указанной category."""
    return [
        expense for expense in expenses
        if matches_filters(expense, limit=limit, category=category)
    ]


def group_by_category(expenses: list) -> dict[str, int | float]:
    """Группирует расходы по категории, считая сумму в каждой."""
    totals = {}
    for expense in expenses:
        totals[expense['category']] = totals.get(expense['category'], 0) + expense['amount']
    return totals


def read_int(prompt: str) -> int:
    """Запрашивает у пользователя целое число, повторяя при некорректном вводе."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print('Это не целое число. Попробуйте ещё раз.')
            print()


def load_expenses(path: str) -> list:
    """Загружает список расходов. На отсутствие файла или битый JSON — пустой список."""
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print('Файл расходов не найден, начинаю с пустого списка.')
        return []
    except json.JSONDecodeError:
        print('Файл расходов повреждён, начинаю с пустого списка.')
        return []


def save_expenses(path: str, expenses: list) -> None:
    """Сохраняет список расходов в JSON-файл."""
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(expenses, file, ensure_ascii=False, indent=2)


def create_new_expense() -> dict:
    """Запрашивает у пользователя данные для нового расхода."""
    category = input('Категория расхода: ').strip()
    amount = read_int('Потраченная сумма: ')
    description = input('Описание: ').strip()
    return {'category': category, 'amount': amount, 'description': description}


def show_expenses_report(expenses: list) -> None:
    """Печатает отчёт по расходам выше порога и сводку по категориям."""
    limit = read_int('Введите порог в рублях: ')
    matched_expenses = filter_expenses(expenses, limit=limit)

    if not matched_expenses:
        print('Расходов выше порога не найдено')
    else:
        matched_total = sum(expense['amount'] for expense in matched_expenses)
        all_total = sum(expense['amount'] for expense in expenses)
        print(f'Расходы от {limit} руб:')
        formatted_expenses = [format_expense(expense) for expense in matched_expenses]
        print('\n'.join(formatted_expenses))
        print()
        print(f'Найдено: {len(matched_expenses)} шт.')
        print(f'Общая сумма: {matched_total} руб')
        print(f'Выше порога: {(matched_total * 100 / all_total):.2f}% от всех трат')

    print()
    print('=== Сводка по категориям ===')
    totals = group_by_category(expenses)
    category_summaries = [f'- {category}: {amount} руб' for category, amount in totals.items()]
    print('\n'.join(category_summaries))


expenses = load_expenses(FILE_PATH)
command = input('Команда (add или report): ').strip().lower()

if command == 'add':
    new_expense = create_new_expense()
    expenses.append(new_expense)
    save_expenses(FILE_PATH, expenses)
    print('Расход добавлен.')
elif command == 'report':
    if not expenses:
        print('Расходов пока нет. Добавьте первый через команду add.')
    else:
        show_expenses_report(expenses)
else:
    print('Неизвестная команда. Доступны: add, report.')

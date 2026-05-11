def format_expense(expense: dict) -> str:
    """Форматирует расход в строку для вывода."""
    return f'- {expense["category"]}, {expense["amount"]} руб, {expense["description"]}'


def matches_filters(expense: dict, *, limit: int | float, category: str | None) -> bool:
    """Проверяет соответствие расхода категории и лимита"""
    return (category is None or expense['category'] == category) and expense["amount"] >= limit


def filter_expenses(expenses: list, *, limit: int | float = 0, category: str | None = None) -> list:
    """Возвращает расходы с суммой не меньше limit и указанной category."""
    return [
        expense for expense in expenses if matches_filters(expense, limit=limit, category=category)
    ]


def group_by_category(expenses: list) -> dict[str, float | int]:
    """Суммирует расходы категорий"""
    totals = {}
    for expense in expenses:
        category = expense['category']
        amount = expense['amount']
        totals[category] = totals.get(category, 0) + amount

    return totals


def read_limit() -> int:
    """Запрашивает у пользователя порог в рублях, повторяя при некорректном вводе"""

    while True:
        try:
            return int(input('Введите порог в рублях: '))
        except ValueError:
            print('Это не целое число. Попробуйте ещё раз.')
            print()


limit = read_limit()

expenses = [
    {"category": "еда", "amount": 500, "description": "обед в кафе"},
    {"category": "транспорт", "amount": 60, "description": "метро"},
    {"category": "развлечения", "amount": 1500, "description": "кино"},
    {"category": "еда", "amount": 1200, "description": "ужин"},
    {"category": "транспорт", "amount": 350, "description": "такси"},
    {"category": "еда", "amount": 200, "description": "кофе"},
]

matched_expenses = filter_expenses(expenses, limit=limit)

if not expenses:
    print('Расходы отсутствуют')
elif not matched_expenses:
    print('Расходов выше порога не найдено')
else:
    matched_total = sum(expense['amount'] for expense in matched_expenses)
    all_total = sum(expense['amount'] for expense in expenses)
    print(f'Расходы от {limit} руб:')
    formatted_expenses = [
        format_expense(expense)
        for expense in matched_expenses
    ]
    print('\n'.join(formatted_expenses))
    print()
    print(f'Найдено: {len(matched_expenses)} шт.')
    print(f'Общая сумма: {matched_total} руб')
    print(f'Выше порога: {(matched_total * 100 / all_total):.2f}% от всех трат')

if expenses:
    print()
    print('=== Сводка по категориям ===')
    totals = group_by_category(expenses)
    category_summaries = [f'- {category}: {amount} руб' for category, amount in totals.items()]
    print('\n'.join(category_summaries))

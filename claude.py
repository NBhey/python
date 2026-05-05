def format_expense(expense: dict) -> str:
    """Форматирует расход в строку для вывода."""
    return f'- {expense["category"]}, {expense["amount"]} руб, {expense["description"]}'


def calculate_total(expenses: list) -> float:
    """Считает сумму поля amount по списку расходов."""
    total = 0
    for expense in expenses:
        total += expense["amount"]
    return total


def matches_filters(expense: dict, *, limit: int | float, category: str | None) -> bool:
    """ Проверяет соответствие расхода категории и лимита"""
    return (category is None or expense['category'] == category) and expense["amount"] >= limit


def filter_expenses(expenses: list, *, limit: int | float = 0, category: str | None = None) -> list:
    """Возвращает расходы с суммой не меньше limit и указанной category."""
    return [
        expense for expense in expenses if matches_filters(expense, limit=limit, category=category)
    ]


def analyze_expenses(expenses: list, *, limit: int | float = 0, category: str | None = None) -> tuple[
    list, float, float]:
    """Анализирует расходы за один проход.

    Args:
        expenses: список словарей расходов.
        limit: минимальная сумма расхода для попадания в выборку.
        category: если задана — оставлять только расходы этой категории.

    Returns:
        (matched_expenses, matched_total, all_total) —
        отфильтрованные расходы, их сумма и общая сумма всех расходов.
    """

    all_total = 0
    matched_total = 0
    matched_expenses = []

    for expense in expenses:
        amount = expense["amount"]
        all_total += amount
        if amount >= limit and (category is None or expense['category'] == category):
            matched_expenses.append(expense)
            matched_total += amount

    return matched_expenses, matched_total, all_total


def group_by_category(expenses: list) -> dict[str, float | int]:
    """Суммирует расходы категорий"""
    totals = {}
    for expense in expenses:
        category = expense['category']
        amount = expense['amount']
        totals[category] = totals.get(category, 0) + amount

    return totals


limit = int(input('Введите порог в рублях: '))

expenses = [
    {"category": "еда", "amount": 500, "description": "обед в кафе"},
    {"category": "транспорт", "amount": 60, "description": "метро"},
    {"category": "развлечения", "amount": 1500, "description": "кино"},
    {"category": "еда", "amount": 1200, "description": "ужин"},
    {"category": "транспорт", "amount": 350, "description": "такси"},
    {"category": "еда", "amount": 200, "description": "кофе"},
]

matched_expenses, matched_total, all_total = analyze_expenses(expenses, limit=limit)

if not matched_expenses:
    print('Расходов выше порога не найдено')
else:
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

print('=== Сводка по категориям ===')
totals = group_by_category(expenses)
category_summaries = [f'- {category}: {amount} руб' for category, amount in totals.items()]
print('\n'.join(category_summaries))

def format_expense(*, expense: dict) -> str:
    """Форматирует расход в строку для вывода."""
    return f'- {expense["category"]}, {expense["amount"]} руб, {expense["description"]}'


limit = int(input('Введите порог в рублях: '))

expenses = [
    {"category": "еда", "amount": 500, "description": "обед в кафе"},
    {"category": "транспорт", "amount": 60, "description": "метро"},
    {"category": "развлечения", "amount": 1500, "description": "кино"},
    {"category": "еда", "amount": 1200, "description": "ужин"},
    {"category": "транспорт", "amount": 350, "description": "такси"},
    {"category": "еда", "amount": 200, "description": "кофе"},
]

all_expenses = 0
total_expenses = 0

matched_expenses = []

for expense in expenses:
    all_expenses += expense["amount"]
    if expense["amount"] >= limit:
        matched_expenses.append(expense)
        total_expenses += expense["amount"]

if not matched_expenses:
    print()
    print('Расходов выше порога не найдено')
else:
    print(f'Расходы от {limit} руб:')
    for expense in matched_expenses:
        print(format_expense(expense=expense))
    print()
    print(f'Найдено: {len(matched_expenses)} шт.')
    print(f'Общая сумма: {total_expenses} руб')
    print(f'Выше порога: {(total_expenses * 100 / all_expenses):.2f}% от всех трат')

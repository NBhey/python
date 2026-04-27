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

print(f'Расходы от {limit} руб:')

for expense in expenses:
    all_expenses += expense["amount"]
    if expense["amount"] >= limit:
        print(f'- {expense["category"]}, {expense["amount"]}, {expense["description"]}')
        total_expenses += expense["amount"]

print(f'''\nНайдено: 3 расхода
Общая сумма: {total_expenses} руб''')

print(f'Выше порога: {(total_expenses * 100 / all_expenses):.2f}% от всех трат')

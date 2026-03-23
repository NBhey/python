# print('Привет, Яндекс!')
#
# name = input('Как вас зовут? ')
# print(f'Привет, {name}')
#
# info=input('Three time')
#
# print(info,info,info, sep='\n')
# print(f"{2 ** 0.5:.0f}")
#
# number = input('Число ')
# summa = 38 * 2.5
# print(int(int(number) - summa) )

# cost = input('цена товара за единицу веса:')
# weight = input('вес товара: ')
# money = input('количество денег у покупателя ')
#
# result = int(money) - int(cost)  * int(weight)
# print(result)

# product = input()
# cost = input()
# weight = input()
# money = input()
# print('Чек')
# print(f'{product} - {weight}кг - {cost}руб/кг')
# print(f'Итого: {int(weight) * int(cost)}руб')
# print(f'Внесено: {money}руб')
# print(f'Сдача: {int(money) - int(weight) * int(cost)}руб')
#
# print(f"Чек\n{product} - {weight}кг - {cost}руб/кг\nИтого: {int(weight) * int(cost)}руб\nВнесено: {money}руб\n"
#       f"Сдача: {int(money) - int(weight) * int(cost)}руб")

# repeat = int(input())
# print('Купи слона!\n' * repeat)

# repeat = int(input())
# text = input()
#
# print(f'Я больше никогда не буду писать "{text}"!\n' * repeat)
#
# children = int(input())
# time = int(input())
#
# print((children // 2) * time)

name = input()
number = int(input())

group = number // 100
bed = ((number % 100) - number % 10) // 10
number_children = number % 10

print(f"Группа №{group}.\n{number_children}. {name}.\nШкафчик: {number}.\nКроватка: {bed}.")


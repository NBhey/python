# print('Как Вас зовут?')
# name = input()
# print(f'Здравствуйте, {name}!')
# print('Как дела?')
# deal = input()
# if deal == 'хорошо':
#     print('Я за Вас рада!')
# else:
#     print('Всё наладится!')
#
# speed_Petya = int(input())
#
# speed_Vasya = int(input())
#
# if speed_Petya > speed_Vasya:
#     print('Петя')
# else:
#     print('Вася')

# speed_Petya = int(input())
#
# speed_Vasya = int(input())
# speed_Tolya = int(input())
#
# if speed_Petya > speed_Vasya and speed_Petya > speed_Tolya:
#     print('Петя')
# elif speed_Tolya > speed_Vasya and speed_Tolya > speed_Petya:
#     print('Петя')
# else:
#     print('Вася')

petya = int(input())
vasya = int(input())
tolya = int(input())

if petya > vasya and petya > tolya:
    print('1. Петя')
elif vasya > petya and vasya > tolya:
    print('1. Вася')
else:
    print('1. Толя')

if (petya > vasya and petya < tolya) or (petya > tolya and petya < vasya):
    print('2. Петя')
elif (petya < vasya and vasya < tolya) or (petya > vasya and vasya > tolya):
    print('2. Вася')
else:
    print('2. Толя')

if petya < vasya and petya < tolya:
    print('3. Петя')
elif vasya < petya and vasya < tolya:
    print('3. Вася')
else:
    print('3. Толя')

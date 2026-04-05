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

# petya = int(input())
# vasya = int(input())
# tolya = int(input())
#
# if petya > vasya and petya > tolya:
#     print('1. Петя')
# elif vasya > petya and vasya > tolya:
#     print('1. Вася')
# else:
#     print('1. Толя')
#
# if (petya > vasya and petya < tolya) or (petya > tolya and petya < vasya):
#     print('2. Петя')
# elif (petya < vasya and vasya < tolya) or (petya > vasya and vasya > tolya):
#     print('2. Вася')
# else:
#     print('2. Толя')
#
# if petya < vasya and petya < tolya:
#     print('3. Петя')
# elif vasya < petya and vasya < tolya:
#     print('3. Вася')
# else:
#     print('3. Толя')

# petya_apple = 7
# vasya_apple = 6
#
# petya_apple = petya_apple - 3 + 2
# vasya_apple = vasya_apple + 3 + 5 - 2
#
# N = int(input())
# M = int(input())
#
# petya_apple = petya_apple + N
# vasya_apple = vasya_apple + M
#
# if petya_apple > vasya_apple:
#     print('Петя')
# else:
#     print('Вася')

# year = int(input())
#
# if year / 4 == year // 4 and year / 100 != year // 100:
#     print('YES')
# elif year / 4 == year // 4 and year / 100 == year // 100 and year / 400 == year // 400:
#     print('YES')
# else:
#     print('NO')

number = input()
palindrome_number = number[3] + number[2] + number[1] + number[0]

if number == palindrome_number:
    print('YES')
else:
    print('NO')

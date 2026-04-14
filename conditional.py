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

# number = input()
# palindrome_number = number[3] + number[2] + number[1] + number[0]
#
# if number == palindrome_number:
#     print('YES')
# else:
#     print('NO')

# area_string = input()
#
# if 'зайка' in area_string:
#     print('YES')
# else:
#     print('NO')

# name_1 = input()
# name_2 = input()
# name_3 = input()
#
# print(min(name_1, name_2, name_3))

# number = input()
#
# little_sum = int(number[2]) + int(number[1])
# big_sum = int(number[0]) + int(number[1])
#
# if little_sum > big_sum:
#     print(str(little_sum) + str(big_sum))
# else:
#     print(str(big_sum) + str(little_sum))

#
# number = input()
#
# max_num = max(int(number[2]), int(number[1]), int(number[0]))
# min_num = min(int(number[2]), int(number[1]), int(number[0]))
#
# check_first_num = number[0] not in str(max_num) and number[0] not in str(min_num)
# check_second_num = number[1] not in str(max_num) and number[1] not in str(min_num)
# check_third_num = number[2] not in str(max_num) and number[2] not in str(min_num)
#
# if check_first_num:
#     stable = number[0]
# elif check_second_num:
#     stable = number[1]
# else:
#     stable = number[2]
#
# if max_num + min_num == int(stable) * 2:
#     print("YES")
# else:
#     print("NO")


# a = int(input())
# b = int(input())
# c = int(input())
#
# if a + b > c and a + c > b and b + c > a:
#     print('YES')
# else:
#     print('NO')

# elf = input()
# dwarf = input()
# human = input()
#
# if elf[0] == dwarf[0] and elf[0] == human[0]:
#     print(elf[0])
# else:
#     print(elf[1])

# number = int('787')
#
# last_number = number % 10
# first_number = (number - last_number) // 100
# second_number = (number - first_number * 100 - last_number) // 10
#
# max_num = max(first_number, second_number, last_number)
# min_num = min(first_number, second_number, last_number)
#
# if str(max_num) in str(first_number):
#     n = max(second_number, last_number)
# elif str(max_num) in str(second_number):
#     n = max(first_number, last_number)
# else:
#     n = max(first_number, second_number)
#
# result_max = str(max_num) + str(n)
#
# if str(min_num) in str(first_number):
#     m = min(second_number, last_number)
# elif str(min_num) in str(second_number):
#     m = min(first_number, last_number)
# else:
#     m = min(first_number, second_number)
#
# result_min = str(min_num) + str(m)
#
# if int(result_min[0]) == 0:
#     result_min = result_min[1] + result_min[0]
#
# print(result_min, result_max)

# number_1 = 31
# number_2 = 11
#
# number_1_first = number_1 // 10
# number_1_second = number_1 % 10
#
# number_2_first = number_2 // 10
# number_2_second = number_2 % 10
#
# max_num = max(number_1_first, number_1_second, number_2_first, number_2_second)
# min_num = min(number_1_first, number_1_second, number_2_first, number_2_second)
#
# number_average = ((number_1_first + number_1_second + number_2_first + number_2_second) - max_num - min_num) % 10
#
# print(str(max_num) + str(number_average) + str(min_num))

# petya = int(input())
# vasya = int(input())
# tolya = int(input())
#
# if petya > vasya and petya > tolya:
#     first_place = petya
#     name_first = "Петя"
# elif petya > vasya and petya < tolya:
#     second_place = petya
#     name_second = "Петя"
# elif petya < vasya and petya > tolya:
#     second_place = petya
#     name_second = "Петя"
# else:
#     third_place = petya
#     name_third = "Петя"
#
# if vasya > petya and vasya > tolya:
#     first_place = vasya
#     name_first = "Вася"
# elif petya > vasya and vasya > tolya:
#     second_place = vasya
#     name_second = "Вася"
# elif petya < vasya and vasya < tolya:
#     second_place = vasya
#     name_second = "Вася"
# else:
#     third_place = vasya
#     name_third = "Вася"
#
# if tolya > petya and vasya < tolya:
#     first_place = tolya
#     name_first = "Толя"
# elif petya > tolya and vasya < tolya:
#     second_place = tolya
#     name_second = "Толя"
# elif tolya < vasya and petya < tolya:
#     second_place = tolya
#     name_second = "Толя"
# else:
#     third_place = tolya
#     name_third = "Толя"
#
# print(f"{'':8}{name_first:^8}{'':8}")
# print(f"{name_second:^8}{'':8}{'':8}")
# print(f"{'':8}{'':8}{name_third:^8}")
# print(f"{'II':^8}{'I':^8}{'III':^8}")
# from math import sqrt
#
# a = 3.5
# b = -2.4
# c = -7.3
#
# if a == 0:
#     if b == 0 and c == 0:
#         print('Infinite solutions')
#     elif b == 0:
#         print('No solution')
#     else:
#         print(f'{(-c / b):.2f}')
# else:
#     D = (b ** 2) - 4 * a * c
#     if D > 0:
#         x_1 = (-b + sqrt(D)) / (2 * a)
#         x_2 = (-b - sqrt(D)) / (2 * a)
#         print(f'{min(float(x_1), float(x_2)):.2f}', f'{max(float(x_1), float(x_2)):.2f}')
#     elif D == 0:
#         x = (-b) / (2 * a)
#         print(f'{float(x):.2f}')
#     else:
#         print("No solution")

# a = 6
# b = 3
# c = 4
#
# if a ** 2 > b ** 2 + c ** 2:
#     print("велика")
# elif b ** 2 > a ** 2 + c ** 2:
#     print('велика')
# elif c ** 2 > a ** 2 + b ** 2:
#     print('велика')
# elif a ** 2 == b ** 2 + c ** 2:
#     print("100%")
# elif b ** 2 == a ** 2 + c ** 2:
#     print('100%')
# elif c ** 2 == a ** 2 + b ** 2:
#     print('100%')
# elif a ** 2 < b ** 2 + c ** 2:
#     print('крайне мала')
# elif b ** 2 < a ** 2 + c ** 2:
#     print('крайне мала')
# elif c ** 2 < a ** 2 + b ** 2:
#     print('крайне мала')

from math import sqrt

x = float(input())
y = float(input())

if x ** 2 + y ** 2 > 100:
    print('Вы вышли в море и рискуете быть съеденным акулой!')
else:
    parabola = ((x + 1) ** 2 - 36) / 4

    danger = (
            (-7 <= x <= -4 and parabola <= y <= (5 * x + 35) / 3) or
            (-4 <= x <= 0 and parabola <= y <= 5) or
            (0 <= x <= 5 and parabola <= y <= sqrt(25 - x ** 2))
    )

    if danger:
        print('Опасность! Покиньте зону как можно скорее!')
    else:
        print('Зона безопасна. Продолжайте работу.')

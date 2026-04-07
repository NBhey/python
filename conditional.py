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

elf = input()
dwarf = input()
human = input()

if elf[0] == dwarf[0] and elf[0] == human[0]:
    print(elf[0])
else:
    print(elf[1])

# while (row := input()) != 'Три!':
#     print('Режим ожидания...')
# print('Ёлочка, гори!')

# count = 0
#
# while (text := input()) != 'Приехали!':
#     if 'зайка' in text:
#         count += 1
# print(count)

# num_1 = int(input())
# num_2 = int(input())
#
# for num in range(num_1, num_2 + 1):
#     print(num, end=' ')

# num_1 = int(input())
# num_2 = int(input())
#
# if num_1 < num_2:
#     for num in range(num_1, num_2 - 1, -1):
#         print(num, end=' ')
# else:
#     for num in range(num_1, num_2 + 1):
#         print(num, end=' ')

# total = 0
#
# while (cost := float(input())) != 0:
#     if cost >= 500:
#         total += cost - cost * 0.1
#     else:
#         total += cost
# print(total)

# number_1 = int(input())
# number_2 = int(input())
#
# while number_2 % number_1 != 0:
#     head_number = number_1
#     number_1 = number_2 % number_1
#     number_2 = head_number
# print(number_1)


# number_1 = int(input())
# number_2 = int(input())
#
# save_number_1 = number_1
# save_number_2 = number_2
#
# while number_2 % number_1 != 0:
#     head_number = number_1
#     number_1 = number_2 % number_1
#     number_2 = head_number
#
# print(save_number_1 * save_number_2 // number_1)

# text = input()
# repeat = int(input())
#
# for i in range(repeat):
#     print(text)

# number = int(input())
# result = 1
#
# for i in range(1, number + 1):
#     result *= i
# print(result)

# x = 0
# y = 0
#
# while (target := input()) != 'СТОП':
#     step = int(input())
#     match target:
#         case 'СЕВЕР':
#             x += step
#         case 'ВОСТОК':
#             y += step
#         case 'ЮГ':
#             x -= step
#         case 'ЗАПАД':
#             y -= step
#
# print(x)
# print(y)

# number = int(input())
# result = 0
#
# while number > 0:
#     last_digit = number % 10
#     result += last_digit
#     number //= 10
# print(result)

# number = int(input())
# result = 0
#
# while number != 0:
#     last_number = number % 10
#     if last_number > result:
#         result = last_number
#     number //= 10
#
# print(result)

# number = int(input())
# counter = 0
#
# for divisor in range(1, number + 1):
#     if number % divisor == 0:
#         counter += 1
#
# if counter == 2:
#     print('YES')
# else:
#     print('NO')

# repeat = int(input())
# counter = 0
# for i in range(repeat):
#     string = input()
#     if 'зайка' in string:
#         counter += 1
#
# print(counter)

input_1 = 123454321  # 1234
copy_input_1 = input_1

palindrome_input_1 = 0

while input_1 != 0:
    number = input_1 % 10
    palindrome_input_1 += number
    palindrome_input_1 *= 10
    input_1 = input_1 // 10

print(palindrome_input_1 // 10 == copy_input_1)

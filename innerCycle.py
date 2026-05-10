# size = int(input())
#
# for i in range(1, size + 1):
#     for j in range(1, size + 1):
#         print(j * i, end=" ")
#     print(sep='\n')

# size = int(input())
#
# for i in range(1, size + 1):
#     for j in range(1, size + 1):
#         print(f'{j} * {i} = {i * j}')

# limit = int(input())
#
# counter = 0
# for i in range(1, limit + 1):
#     for j in range(counter, counter + i):
#         counter += 1
#         print(counter, end=" ")
#         if counter == limit:
#             break
#     if counter == limit:
#         break
#     print()

# number = int(input())
# total = 0
# for i in range(1, number + 1):
#     user_number = int(input())
#     while user_number > 0:
#         total += user_number % 10
#         user_number //= 10
#
# print(total)

# repeat_cycle = int(input())
# repeat_counter = 0
#
# rabbit_in_area = True
# rabbit_counter = 0
#
# while repeat_counter != repeat_cycle:
#     area = input()
#     if area == 'зайка' and rabbit_in_area:
#         rabbit_in_area = False
#         rabbit_counter += 1
#     if area == 'ВСЁ':
#         rabbit_in_area = True
#         repeat_counter += 1
#
# print(rabbit_counter)

n = int(input())

gcd = int(input())

for _ in range(n - 1):
    number = int(input())

    a = gcd
    b = number

    while b != 0:
        a, b = b, a % b

    gcd = a

print(gcd)

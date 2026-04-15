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

num_1 = int(input())
num_2 = int(input())

if num_1 < num_2:
    for num in range(num_1, num_2 - 1, -1):
        print(num, end=' ')
else:
    for num in range(num_1, num_2 + 1):
        print(num, end=' ')

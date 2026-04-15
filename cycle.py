# while (row := input()) != 'Три!':
#     print('Режим ожидания...')
# print('Ёлочка, гори!')

count = 0

while (text := input()) != 'Приехали!':
    if 'зайка' in text:
        count += 1
print(count)

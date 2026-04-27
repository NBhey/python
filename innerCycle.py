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

number = int(input())
total = 0
for i in range(1, number + 1):
    user_number = int(input())
    while user_number > 0:
        total += user_number % 10
        user_number //= 10

print(total)

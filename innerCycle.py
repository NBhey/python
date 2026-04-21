size = int(input())
start = 1

for i in range(1, size + 1):
    for j in range(1, size + 1):
        print(j * i, end=" ")
    print(sep='\n')

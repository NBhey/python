with open('log.txt', 'a', encoding='utf-8') as file:
    file.write(input('Введите запись: ') + '\n')

with open('log.txt', 'r', encoding='utf-8') as file:
    for index, line in enumerate(file, start=1):
        print(f'{index}. {line.rstrip()}')

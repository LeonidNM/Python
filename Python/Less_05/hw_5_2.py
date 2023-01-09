# 2. Создать текстовый файл (не программно), 
# сохранить в нём несколько строк, 
# выполнить подсчёт строк и слов в каждой строке.

with open('test.txt') as read_file:
    all_read_lines = read_file.readlines()
    for num, line in enumerate(all_read_lines):
        print(f'\tВ строке {num + 1}: {len(line.split())} слов(а)')
    print(f'\tВсего: {len(all_read_lines)} строк(и)\n')
    
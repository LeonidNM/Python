# 5. Программа запрашивает у пользователя строку чисел, разделённых пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter.
# Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введён после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def num_sum():
    res = 0
    while True:
        numbers = input('Введите последовательность чисел через пробел: ').split()
        for num in numbers:
            try:
                if num == '*' or num == '@' or num == '#' or num == '$' or num == '%' or num == '^' or num == '&':
                    print(f'{res}. Программа завершена')
                    return
                else:
                    res += int(num)
            except ValueError:
                continue
        print(res)

num_sum()

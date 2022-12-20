# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369

number = int(input('Введите число: '))
n_1 = int('%s' % number)
n_2 = int('%s%s' % (number, number))
n_3 = int('%s%s%s' % (number, number, number))
print(n_1 + n_2 + n_3)

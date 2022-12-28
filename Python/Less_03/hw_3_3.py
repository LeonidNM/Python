# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(number_1, number_2, number_3):
    sum_number = [number_1, number_2, number_3]
    sum_number.remove(min(number_1, number_2, number_3))
    print('Сумма двух наибольших чисел равна: {}'.format(sum(sum_number)))

my_func(int(input('Введите первое число: ')),
        int(input('Введите второе число: ')),
        int(input('Введите третье число: ')))

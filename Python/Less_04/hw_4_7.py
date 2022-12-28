# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор. Функция вызывается следующим образом: for el in fact(n).
# Она отвечает за получение факториала числа.
# В цикле нужно выводить только первые n чисел, начиная с 1! и до n!.

from math import factorial
from itertools import count

fac_num = int(input('Укажите число для вычисления факториала: '))

def fac_gen(fac_num):
    for i in count(fac_num):
        yield factorial(i)

def fac_print(fac_num):
    gen = fac_gen(fac_num)
    x = 0
    for i in gen:
        if x < 5:
            print(i)
            x += 1
        else:
            break

fac_print(fac_num)

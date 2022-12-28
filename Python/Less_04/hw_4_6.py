# 6. Реализовать два небольших скрипта:
# итератор, генерирующий целые числа, начиная с указанного;
# итератор, повторяющий элементы некоторого списка, определённого заранее.

from itertools import count, cycle

space_num = int(input('Условно бесконечный генератор чисел. Введите число: '))
lst_sn = []

for i in count(space_num):
    print(i, end=' ')
    lst_sn.append(i)
    if len(lst_sn) > 10:
        break

spase_lst = input('\nУсловно бесконечный повтор введенных значений. Введите значения через пробел: ').split()
lst_sl = []
for value in cycle(spase_lst):
    print(value, end=' ')
    lst_sl.append(value)
    if len(lst_sl) > 10:
        break

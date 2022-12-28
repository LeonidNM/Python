# 2. Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.

ent_list = [int(i) for i in input('Введите числа (через пробел): ').split()]
res_list = [number for i, number in enumerate(ent_list) if i > 0 and ent_list[i] > ent_list[i - 1]]
print(res_list)

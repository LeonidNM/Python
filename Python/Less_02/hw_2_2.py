# 2. Для списка реализовать обмен значений соседних элементов.
# Т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

element_count = int(input('Введите количество элементов списка: '))
my_list = [0]
i = 0
element = 0
while i < element_count:
    i += 1
    my_list.append(i)

for el in range(int((len(my_list) - 1) / 2)):
    my_list[element], my_list[element + 1] = my_list [element + 1], my_list[element]
    element += 2
print(my_list)

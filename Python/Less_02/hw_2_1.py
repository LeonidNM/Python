# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

type_list = [11,
             7/6,
             [1, 2, '200'],
             {'books': '1984'},
             (1, 2),
             None,
             -30,
             'True',
             True,
             9.5,
             '2',
             frozenset('1'),
             'cat',
             set('1')]
for i in range (len(type_list)) :
    print(f'Элемент № {i} ({type_list[i]}) имеет тип: {type(type_list[i])}')

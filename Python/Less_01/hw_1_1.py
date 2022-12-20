#1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран

str_var = 'Текст'
int_var = 666
float_var = 4.13
list_var = [1, 2, 'Список']
dict_var = {1: 'А', 2: 'Б', 3: 'В'}

print(str_var)
print(int_var)
print(float_var)
for i in list_var:
    print(i)
print(dict_var)

try:
    num_1 = int(input('Введите целое число: '))
    num_2 = float(input('Введите дробное число: '))
    sum = num_1 + num_2
    print('Сумма введенных чисел равна: ', sum)
except ValueError:
    try:
        num_1 = int(input('Введите целое число: '))
        num_2 = float(input('Введите дробное число. Дробь указывается после точки: '))
        sum = num_1 + num_2
        print('Сумма введенных чисел равна: ', sum)
    except ValueError:
        print('Пока, неудачник!')

first_name = input('Введите имя: ')
last_name = input('Введите фамилию: ')
print('С какого района {} {}?'.format(first_name, last_name))

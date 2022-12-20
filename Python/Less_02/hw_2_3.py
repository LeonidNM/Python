# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

# Решение через list

seasons_list = ['Зима', 'Весна', 'Лето', 'Осень']
month = int(input('Введите номер месяца: '))
while True:
    if month > 12 or month <= 0:
        month = int(input('Введите номер месяца от 1 to 12: '))
        continue
    if month == 12 or (month >= 1 and month < 3):
        print(seasons_list[0])
        break
    elif month >= 3 and month < 6:
        print(seasons_list[1])
        break
    elif month >= 6 and month < 9:
        print(seasons_list[2])
        break
    else:
        print(seasons_list[3])
        break

# Решение через dict
seasons_dict = {'Зима':  [12, 1, 2],
              'Весна': [3, 4, 5],
              'Лето':  [6, 7, 8],
              'Осень': [9, 10, 11]}
month_num = int(input('Введите номер месяца: '))
if month_num in range(1, 13):
    for i in seasons_dict.items():
        if month_num in i[1]:
             print(i[0])
else:
    print('Введен некорректный номер месяца')

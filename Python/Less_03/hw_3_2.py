# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

# 1 вариант

first_name = input('Имя: ')
last_name = input('Фамилия: ')
birth = input('Год рождения: ')
city = input('Город: ')
email = input('Электронная почта: ')
phone = input('Телефон: ')

def personal_info(first_name, last_name, birth, city, email, phone):
    print(f'{first_name} {last_name}, {birth} г.р., г. {city}, e-mail: {email}, телефон: {phone}')

personal_info(first_name, last_name, birth, city, email, phone)
personal_info('Иван', 'Петров', 1937, 'Урюпинск', 'Нет', 6661313)

# 2 вариант

def pers_info():
    first_name = input('Имя: ')
    last_name = input('Фамилия: ')
    birth = input('Год рождения: ')
    city = input('Город: ')
    email = input('Электронная почта: ')
    phone = input('Телефон: ')
    print(f'{first_name} {last_name}, {birth} г.р., г. {city}, e-mail: {email}, nелефон: {phone}')

pers_info()

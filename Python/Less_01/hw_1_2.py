#2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк

sec = int(input('Введите время в секундах: '))
while sec > 86399:
    print('Укажите время в секундах (не более 86399)')
    sec = int(input('Введите время в секундах: '))
hh = sec//3600
hh_form = (hh) if hh > 10 else ('0' + str(hh))
min = (sec % 3600)//60
min_form = (min) if min > 10 else ('0' + str(min))
ss = (sec % 3600) % 60
ss_form = (ss) if ss > 10 else ('0' + str(ss))
print(f'Время: {hh_form}:{min_form}:{ss_form}')

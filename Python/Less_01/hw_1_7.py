# 7. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров. Программа должна принимать значения параметров a и b и  выводить одно натуральное число — номер дня

a = float(input('Укажите, сколько километров пробежал спортсмен в первый день: '))
b = float(input('Укажите целевой результат, км: '))
day = 1
if a > b:
    print(day)
while a < b:
    a *= 1.1
    day += 1
print(f'Целевой результат будет достигнут на {day} день')

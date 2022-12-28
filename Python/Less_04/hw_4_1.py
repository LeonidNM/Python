# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
# Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
# Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.

hours_work = int(input('Укажите количество отработанных часов: '))
work_pay = float(input('Укажите стоимость 1 часа работы в у.е.: '))

def okl_calc(hours_work, work_pay):
    okl = hours_work * work_pay
    return okl

def pay_calc(bonus):
    pay = okl_calc(hours_work, work_pay) + bonus
    return pay

def bonus_calc(bonus_1):
    razm_bon = okl_calc(hours_work, work_pay) * bonus_1
    pay = okl_calc(hours_work, work_pay) + razm_bon
    return pay

try:
    bonus = float(input('Укажите размер премии в у.е или нажмите enter: '))
    print(pay_calc(bonus))
except:
    bonus_1 = float(input('Укажите размер премии (доля от оклада): '))
    print(bonus_calc(bonus_1))

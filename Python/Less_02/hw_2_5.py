# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением
# должен разместиться после них.

rate_list = [10, 10, 7, 5, 4, 3, 3, 2, 1]
print(rate_list)
new_rate = int(input('Введите число: '))
inserted = False

while not inserted:
    try:
        if new_rate < 0:
            new_rate = int(input('Введите число равное нулю или больше нуля: '))
            continue
        elif new_rate > max(rate_list):
            rate_list.insert(0, new_rate)
            break
        elif new_rate < min(rate_list):
            rate_list.append(new_rate)
            break
        for i, el in enumerate(rate_list):
            if rate_list[-1] == new_rate:
                rate_list.append(new_rate)
                inserted = True
                break
            elif el == new_rate and el != rate_list[i + 1]:
                rate_list.insert(i + 1, new_rate)
                inserted = True
                break
    except ValueError:
        print('Должно быть положительное число')

print(rate_list)



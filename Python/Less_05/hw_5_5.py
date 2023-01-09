# 5. Создать (программно) текстовый файл, 
# записать в него программно набор чисел, разделённых пробелами. 
# Программа должна подсчитывать сумму чисел в файле и выводить её 
# на экран.

import random

with open('dz_5.txt', 'w') as f:
    for i in range(3):
        f.write(' '.join([str(x) for x in random.sample(range(1, 10), random.randint(0, 5))]))

total = 0
with open('dz_5.txt', 'r') as f:
    for line in f:
        total += sum([int(x) for x in line.split()])
    print(total)
    
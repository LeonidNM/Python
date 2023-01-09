# 7. Создать вручную и заполнить несколькими строками 
# текстовый файл, в котором каждая строка будет содержать данные 
# о фирме: название, форма собственности, выручка, издержки.
# Необходимо построчно прочитать файл, 
# вычислить прибыль каждой компании, а также среднюю прибыль. 
# Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь 
# с фирмами и их прибылями, а также словарь со средней прибылью. 
# Если фирма получила убытки, также добавить её в словарь 
# (со значением убытков).
# Итоговый список сохранить в виде json-объекта в соответствующий файл.

import json
from pprint import pprint

def gen_file(file_path, sample):
    with open(file_path, 'w') as f:
        for t in sample:
            f.write(' '.join(map(str, t)))
            f.write('\n')

def calc_profit(sample_file, res_file):
    res = []
    res_dict = {}
    positive_profit_count = 0
    total_profit = 0

    with open(sample_file, 'r') as f:
        for line in f:
            firm, _, rev, exp = line[:-1].split()
            profit = int(rev) - int(exp)
            if profit > 0:
                total_profit += profit
                positive_profit_count += 1
            res_dict[firm] = profit
    avr_profit = total_profit / positive_profit_count if positive_profit_count else 0
    res.append(res_dict)
    res.append({'Average profit': avr_profit})

    with open(res_file, 'w', encoding='UTF-8') as f:
        json.dump(res, f)

sample_file = 'firm.txt'
res_file = 'firm.json'
sample_exp = [('ABC', 'OOO', 10000, 5000),
            ('StroyGas', 'AO', 5000, 10000),
            ('Roga_I_Kopyta', 'AO', 10000, 10000),
            ('Gambs', 'IP', 5000, 3000),
            ('Gigantskie_Rasteniya', 'OOO', 3000, 5000),
            ('IDR', 'AG', 10000, 5000),
            ('Folk_Geselshaft_Boisen_und_C', 'Gmbh', 20000, 7000),
            ('Smith_and_Castrakis', 'LLC', 8000, 20000)]

gen_file(sample_file, sample_exp)
calc_profit(sample_file, res_file)
with open(res_file, 'r') as f:
    js = json.load(f)
    pprint(js, width=1)

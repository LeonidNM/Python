# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую 
# построчно данные. 
# При этом английские числительные должны заменяться на русские. 
# Новый блок строк должен записываться в новый текстовый файл.

en_ru = {'One' : 'Один',
         'Two' : 'Два', 
         'Three' : 'Три', 
         'Four' : 'Четыре'}

f_en = open('file_en.txt', 'r')
text_en = f_en.read()
text_ru = text_en
for en, ru in en_ru.items():
    text_ru = text_ru.replace(en, ru)
with open('file_ru.txt', 'w') as f_ru:
    f_ru.write(text_ru)

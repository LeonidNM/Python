# 6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text

word = input('Введите слово с маленькой буквы: ')

def int_func(word):
    return word.title()

print(int_func(word))

# 3. Создайте собственный класс-исключение, 
# который должен проверять содержимое списка на наличие только чисел. 
# Проверить работу исключения на реальном примере. 
# Запрашивать у пользователя данные и заполнять список необходимо 
# только числами. Класс-исключение должен контролировать типы 
# элемента. Вносить его в список, только если введено число. 
# Класс-исключение должен не позволить пользователю ввести текст 
# (не число) и отобразить соответствующее сообщение. 
# При этом работа скрипта не должна завершаться.

class ErrorType(Exception):
    def __init__(self):
        pass


class TypeCheck:
    def __init__(self):
        self.num_lst = []

    def check_val(self):
        while True:
            try:
                try:
                    user_val = int(input('Введите число: '))
                    self.num_lst.append(user_val)
                    print(self.num_lst)
                    ex = input('Нажмите клавишу S для завершения, или любую другую, чтобы продолжить ').lower()
                    if ex == 's':
                        print(self.num_lst)
                        break
                except ValueError:
                    raise ErrorType
            except ErrorType:
                print('Это не число')
                ex = input('Нажмите клавишу S для завершения, или любую другую, чтобы продолжить ').lower()
                if ex == 's':
                    print(self.num_lst)
                    break

tc = TypeCheck()
tc.check_val()

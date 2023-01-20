# 2. Создайте собственный класс-исключение, 
# обрабатывающий ситуацию деления на ноль. 
# Проверьте его работу на данных, вводимых пользователем. 
# При вводе нуля в качестве делителя программа должна корректно 
# обработать эту ситуацию и не завершиться с ошибкой.


class ZeroError(Exception):
    def __init__(self):
        pass
    
    
class DivNull:
    def div(self):  
        try:
            try:
                num_1 = int(input('Введите делимое: '))
                num_2 = int(input('Введите делитель: '))
                print(num_1 / num_2)
            except:
                raise ZeroError()
        except ZeroError:
            print('Делить на ноль нельзя')
            self.div()
            
            
        
d = DivNull()
d.div()

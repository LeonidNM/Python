# 7. Реализовать проект «Операции с комплексными числами». 
# Создайте класс «Комплексное число». 
# Реализуйте перегрузку методов сложения и умножения комплексных чисел. 
# Проверьте работу проекта. Для этого создаёте экземпляры класса 
# (комплексные числа), выполните сложение и умножение созданных 
# экземпляров. Проверьте корректность полученного результата.

class MyCompNumb:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, oth):
        a = self.a + oth.a
        b = self.b + oth.b
        return MyCompNumb(a, b)

    def __mul__(self, oth):
        a = (self.a * oth.a) - (self.b * oth.b)
        b = (self.a * oth.b) + (self.b * oth.a)
        return MyCompNumb(a, b)

    def __str__(self):
        return f'{self.a} + {self.b}i'


if __name__ == '__main__':
    c_1 = MyCompNumb(2, 5)
    c_2 = MyCompNumb(3, 6)
    c_3 = c_1 + c_2
    c_4 = c_1 * c_2

    print(f'c_1 = {c_1}')         
    print(f'c_2 = {c_2}')         
    print(f'c_1 + c_2 = {c_3}')    
    print(f'c_1 * c_2 = {c_4}')

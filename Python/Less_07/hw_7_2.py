# 2. Реализовать проект расчёта суммарного расхода ткани 
# на производство одежды. 
# Основная сущность (класс) этого проекта — одежда, 
# которая может иметь определённое название. 
# К типам одежды в этом проекте относятся пальто и костюм. 
# У этих типов одежды существуют параметры: размер (для пальто) 
# и рост (для костюма). 
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды 
# использовать формулы: для пальто (V/6.5 + 0.5), 
# для костюма (2*H + 0.3). 
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. 
# Проверить на практике полученные на этом уроке знания: 
# реализовать абстрактные классы для основных классов проекта, 
# проверить на практике работу декоратора @property.

class Textil:

    def __init__(self, param):
        self.param = param
        
    
    @property
    def full_consum(self):
        print('Всего: {:.2f}'.format((self.param / 6.5 + 0.5) + (2 * self.param + 0.3)))
        

class Coat(Textil):
    def consum(self):
        print('Для пальто: {:.2f}'.format(self.param / 6.5 + 0.5))


class Costume(Textil):
    def consum(self):
        print('Для костюма: {:.2f}'.format(2 * self.param + 0.3))
    
 
coat = Coat(57)
costume = Costume(175)
coat.consum()
costume.consum()
coat.full_consum
costume.full_consum

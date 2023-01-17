# 3. Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), 
# income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, 
# содержащий элементы: оклад и премия, например, {"wage": wage, 
# "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени
# сотрудника (get_full_name) и дохода с учётом премии 
# (get_total_income);
# проверить работу примера на реальных данных: 
# создать экземпляры класса Position, передать данные, 
# проверить значения атрибутов, вызвать методы экземпляров.

class Worker:
    def __init__(self, 
                 name: str, 
                 surname: str, 
                 position: str, 
                 wage: int, 
                 bonus: int):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        print(sum(self._income.values()))


lohankin = Position('Васисуалий', 
                    'Лоханкин', 
                    'Мыслитель', 
                    22500, 
                    25000)
print(lohankin.position)
lohankin.get_full_name()
lohankin.get_total_income()

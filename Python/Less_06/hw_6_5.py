# 5. Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). 
# Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), 
# Handle (маркер);
# в каждом классе реализовать переопределение метода draw. 
# Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, 
# что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки', self.title)


class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки ручкой', self.title)


class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки карандашом', self.title)


class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки маркером', self.title)


s = Stationery('канцелярскими принадлежностями')
s.draw()

p = Pen('(гелевой)')
p.draw()

pncl = Pencil('(простым)')
pncl.draw()

h = Handle('(черным)')
h.draw()

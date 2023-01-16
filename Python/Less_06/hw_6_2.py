# 2. Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании
# экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, 
# необходимого для покрытия всей дороги;
# использовать формулу: длина*ширина*масса асфальта 
# для покрытия одного кв. метра дороги асфальтом, 
# толщиной в 1 см*число см толщины полотна;
# проверить работу метода.

class Road:
    _length: int
    _width: int

    def __init__(self, _length, _width, weight, depth):
        self._length = _length
        self._width = _width
        self.weight = weight
        self.depth = depth

    def mass(self):
        l = self._length
        wd = self._width
        w = self.weight
        d = self.depth
        total = l * wd * w * d / 1000
        print(f'{l} м * {wd} м * {w} кг * {d} см = ', total, 'т')


r = Road(20, 5000, 25, 5)
r.mass()
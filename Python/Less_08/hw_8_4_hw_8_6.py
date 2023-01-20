# 4. Начните работу над проектом «Склад оргтехники». 
# Создайте класс, описывающий склад. А также класс «Оргтехника», 
# который будет базовым для классов-наследников. 
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). 
# В базовом классе определите параметры, общие для приведённых типов. 
# В классах-наследниках реализуйте параметры, уникальные для
# каждого типа оргтехники.

# 4. Начните работу над проектом «Склад оргтехники». 
# Создайте класс, описывающий склад. А также класс «Оргтехника», 
# который будет базовым для классов-наследников. 
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). 
# В базовом классе определите параметры, общие для приведённых типов. 
# В классах-наследниках реализуйте параметры, уникальные для 
# каждого типа оргтехники.

# 6. Продолжить работу над вторым заданием. 
# Реализуйте механизм валидации вводимых пользователем данных. 
# Например, для указания количества принтеров, 
# отправленных на склад, нельзя использовать строковый тип данных.

class Warehouse:
    __storage = []
    __summary = {}

    def push(self, equipment):
        self.__storage.append(equipment)
        if self.__summary.get(equipment.type_tech) is not None:
            self.__summary[equipment.type_tech] += 1
        else:
            self.__summary.setdefault(equipment.type_tech, 1)

    def rep_tech(self):
        for item in self.__storage:
            print(item)

    def rep_total(self):
        for k, v in self.__summary.items():
            print(f'{k}: {v} шт')


class OfficeEquipment:
    def __init__(self, 
                 type_tech: str, 
                 model: str, 
                 cost: float, 
                 sn: str):
        self.type_tech = str(type_tech)
        self.model = str(model)
        self.cost = float(cost)
        self.sn = str(sn)

    def __str__(self):
        return f'{self.type_tech} {self.model}'
    

class Printer(OfficeEquipment):
    def __init__(self, 
                 model: str, 
                 cost: float, 
                 is_colorful: bool, 
                 sn: str):
        self.is_colorful = is_colorful
        super().__init__('Принтер', model, cost, sn)


class Scanner(OfficeEquipment):
    def __init__(self, 
                 model: str, 
                 cost: float, 
                 dpi: str, 
                 sn: str):
        self.dpi = dpi
        super().__init__('Сканер', model, cost, sn)


class Copier(OfficeEquipment):
    def __init__(self, 
                 model: str, 
                 cost: float, 
                 is_colorful: bool, 
                 dpi: str,  
                 sn: str):
        self.is_colorful = is_colorful
        self.dpi = dpi
        super().__init__('МФУ', model, cost, sn)


if __name__ == '__main__':
    p_1 = Printer('HP Laser 107a', 6600, False, 'FG64855SFG5')
    s_1 = Scanner('Epson Perf V19', 5010, '4800x4800', '65482321FF5')
    s_2 = Scanner('Canon LiDE 300', 4700.45, '2400x2400', '31313131FFF')
    c_1 = Copier('Canon PIXMA MG2540S', 2299.73, True, '4800x600', 'FG8#HHHF')
    c_2 = Copier('HP LaserJet M132nw', 14604.20, False, '1200x1200', '9BB654848554')

    w = Warehouse()
    w.push(p_1)
    w.push(s_1)
    w.push(s_2)
    w.push(c_1)
    w.push(c_2)

    w.rep_tech()
    w.rep_total()
    
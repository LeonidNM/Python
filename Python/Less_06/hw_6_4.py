# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, 
# color, name, is_police (булево). А также методы: go, stop, 
# turn(direction), которые должны сообщать, что машина поехала, 
# остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, 
# WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, 
# который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. 
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) 
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. 
# Выполните доступ к атрибутам, выведите результат. 
# Вызовите методы и покажите результат.

class Car:
    def __init__(self, 
                 speed: int, 
                 color: str, 
                 name: str,
                 is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    
    def police(self):
        if self.is_police:
            print('Полицейский автомобиль')
        else:
            print('Гражданский автомобиль')
    
    def go(self):
        print('Автомобиль поехал')

    def stop(self):
        print('Автомобиль остановился')

    def turn(self):
        print('Автомобиль повернул')
        
    def show_speed(self):
        print(f'Скорость {self.speed} км/ч')
        
    def auto_info(self):
        print('Автомобиль', self.color, self.name)


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    
    def show_speed(self):
        if self.speed > 60:
            lim = self.speed - 60
            print(f'{self.speed} км/ч. Превышение скорости на {lim} км/ч')
        else:
            print(f'{self.speed} км/ч')
    

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    
    def show_speed(self):
        if self.speed > 40:
            lim = self.speed - 40
            print(f'{self.speed} км/ч. Превышение скорости на {lim} км/ч')
        else:
            print(f'{self.speed} км/ч')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


t_c = TownCar(65, 'Желтый', 'Лада Калина', False)
t_c.auto_info()
t_c.police()
t_c.go()
t_c.turn()
t_c.show_speed()
t_c.stop()

s_c = SportCar(100, 'Красный', 'Запорожец', False)
s_c.auto_info()
s_c.police()
s_c.go()
s_c.turn()
s_c.show_speed()
s_c.stop()

w_c = WorkCar(50, 'Коричневый', 'Барбухайка', False)
w_c.auto_info()
w_c.police()
w_c.go()
w_c.turn()
w_c.show_speed()
w_c.stop()

p_c = PoliceCar(120, 'Желтый', 'УАЗ', True)
p_c.auto_info()
p_c.police()
p_c.go()
p_c.turn()
p_c.show_speed()
p_c.stop()

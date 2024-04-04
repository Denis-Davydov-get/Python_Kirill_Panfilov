# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании экземпляра.
# У класса должно быть два метода, возвращающие длину окружности и её площадь.
import math


class Circle:

    def __init__(self, radius) -> None:
        self.radius = radius

    def dlina(self):
        return 2 * self.radius * math.pi

    def area(self):
        return math.pi * (self.radius ** 2)


a = Circle(3)
print(a.dlina())
print(a.area())

class Rectangle:
    def __init__(self, width, height=None):
        '''Конструктор класса. Принимает ширину и высоту прямоугольника.
        Если высота не указана (по умолчанию None), то считается, что прямоугольник является квадратом,
        и высота устанавливается равной ширине.
        @ width - ширина прямоугольника
        @ height - высота прямоугольника'''
        self.width = width
        self.height = height if height else width

    def perimeter(self):
        '''Метод для вычисления периметра прямоугольника. Возвращает целое число - значение периметра'''
        return (self.width + self.height) * 2

    def area(self):
        '''Метод для вычисления площади прямоугольника. Возвращает целое число - значение площади'''
        return self.width * self.height

    def __add__(self, other):
        '''Магический метод, который определяет операцию сложения (+) для двух прямоугольников.
        Принимает другой прямоугольник other. Создает новый прямоугольник,
        который представляет собой объединение исходных прямоугольников по периметру.
        Новая ширина и высота вычисляются также на основе объединения. Возвращает новый прямоугольник.'''
        x = self.width + other.width
        y = self.height + other.height
        return Rectangle(x, y)

    def __sub__(self, other):
        '''Магический метод, который определяет операцию вычитания (-) одного прямоугольника из другого.
        Принимает вычитаемый прямоугольник other. Создает новый прямоугольник, представляющий разницу
        периметров исходных прямоугольников, и вычисляет высоту на основе этой разницы.
        Новая ширина вычисляется также на основе разницы. Возвращает новый прямоугольник'''
        x = self.width - other.width
        y = self.height - other.height
        return Rectangle(x, y)

    def __lt__(self, other):
        '''Магический метод, который определяет операцию "меньше" (<) для двух прямоугольников.
        Принимает другой прямоугольник other. Возвращает True, если площадь первого прямоугольника меньше площади второго,
        иначе False.'''
        area_self = self.height * self.height
        area_other = other.height * other.height
        if area_self < area_other:
            return True
        else:
            return False

    def __eq__(self, other):
        area_self = self.height * self.height
        area_other = other.height * other.height
        if area_self == area_other:
            return True
        else:
            return False

    def __le__(self, other):
        '''Магический метод, который определяет операцию "меньше или равно" (<=) для двух прямоугольников.
        Принимает другой прямоугольник other. Возвращает True, если площадь первого прямоугольника меньше
        или равна площади второго, иначе False.'''
        area_self = self.height * self.height
        area_other = other.height * other.height
        if area_self <= area_other:
            return True
        else:
            return False

    def __str__(self):
        '''Магический метод, возвращающий строковое представление прямоугольника.
        Возвращает строку, описывающую ширину и высоту прямоугольника в виде:
        Прямоугольник со сторонами 2 и 3,
        где первое число - это ширина, а второе - высота.'''
        return (f'Прямоугольник со сторонами {self.width} и {self.height}')

    def __repr__(self):
        '''Магический метод, возвращающий строковое представление прямоугольника,
        которое может быть использовано для создания нового объекта такого же класса с теми же атрибутами.'''
        return (f'Rectangle({self.width}, {self.height})')


rect1 = Rectangle(4, 5)
rect2 = Rectangle(3, 3)

print(rect1)  # Прямоугольник со сторонами 4 и 5
print(rect2)  # Прямоугольник со сторонами 3 и 3

print(rect1.perimeter())  # 18
print(rect1.area())  # 20
print(rect2.perimeter())  # 12
print(rect2.area())  # 9

rect_sum = rect1 + rect2
rect_diff = rect1 - rect2

print(rect_sum)  # Прямоугольник со сторонами 7 и 8
print(rect_diff)  # Прямоугольник со сторонами 1 и 2

print(rect1 < rect2)  # False
print(rect1 == rect2)  # False
print(rect1 <= rect2)  # False

print(repr(rect1))  # Rectangle(4, 5)
print(repr(rect2))  # Rectangle(3, 3)

# Ваш ответ:
#
# Прямоугольник со сторонами 4 и 5
# Прямоугольник со сторонами 3 и 3
# 18
# 25
# 12
# 9
# Прямоугольник со сторонами 7 и 8
# Прямоугольник со сторонами 1 и 2
# False
# False
# False
# Rectangle(4, 5)
# Rectangle(3, 3)

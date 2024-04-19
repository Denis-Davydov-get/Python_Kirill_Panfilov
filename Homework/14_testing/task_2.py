import unittest


class NegativeValueError(ValueError):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


class Rectangle:

    def __init__(self, width, height=None):
        if width <= 0:
            raise NegativeValueError(f'Ширина должна быть положительной, а не {width}')
        self._width = width
        if height is None:
            self._height = width
        else:
            if height <= 0:
                raise NegativeValueError(f'Высота должна быть положительной, а не {height}')
            self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            raise NegativeValueError(f'Ширина должна быть положительной, а не {value}')

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            raise NegativeValueError(f'Высота должна быть положительной, а не {value}')

    def perimeter(self):
        return 2 * (self._width + self._height)

    def area(self):
        return self._width * self._height

    def __add__(self, other):
        width = self._width + other._width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self._width - other._width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)


# Введите ваше решение ниже
class Test(unittest.TestCase):
    def test_width(self):
        rectangle = Rectangle(5)
        self.assertEqual(rectangle.width, 5)

    def test_height(self):
        rectangle = Rectangle(3, 4)
        self.assertEqual(rectangle.height, 4)

    def test_perimeter(self):
        rectangle = Rectangle(5)
        self.assertEqual(rectangle.perimeter(), 20)

    def test_area(self):
        rectangle = Rectangle(3, 4)
        self.assertEqual(rectangle.area(), 12)

    def test_addition(self):
        r1 = Rectangle(5)
        r2 = Rectangle(3, 4)
        self.assertEqual(r1 + r2, Rectangle(8, 8))


if __name__ == '__main__':
    unittest.main()
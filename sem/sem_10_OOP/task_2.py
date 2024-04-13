

class Rectangle:

    def __int__(self, length, width):
        self.length = length
        self.width = width

    def square(self, length, width):
        return length * width

    def perimeter(self, length, width):
        return (length + width) * 2

x = Rectangle()
print(x.perimeter(4,4))
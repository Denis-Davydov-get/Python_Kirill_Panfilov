class Animal:
    def __init__(self, name):
        self.name = name


class Bird(Animal):
    def __init__(self, name, wingspan):
        '''
        Class Птицы
        @ wingspan - размах крыльев
        '''
        self.wingspan = wingspan
        super().__init__(name)

    def wing_length(self):
        '''
           Расчет длины крыла
       '''
        return self.wingspan / 2


class Fish(Animal):
    def __init__(self, name, max_depth):
        '''
        Class Рыбы
        @ max_depth - максимальная глубина обитания
        '''
        self.max_depth = max_depth
        super().__init__(name)

    def depth(self):
        if self.max_depth < 10:
            return "Мелководная рыба"
        elif self.max_depth > 100:
            return "Глубоководная рыба"
        else:
            return "Средневодная рыба"


class Mammal(Animal):
    def __init__(self, name, weight):
        self.weight = weight
        super().__init__(name)

    def category(self):
        if self.weight < 1:
            return "Малявка"
        elif self.weight > 200:
            return "Гигант"
        else:
            return "Обычный"


class AnimalFactory(Mammal, Fish, Bird):

    def create_animal(animal_type, *args):
        if animal_type == 'Bird':
            return Bird(args[0], args[1])
        elif animal_type == 'Fish':
            return Fish(args[0], args[1])
        elif animal_type == 'Mammal':
            return Mammal(args[0], args[1])
        raise ValueError("Недопустимый тип животного")




import random


class InvalidNameError(Exception):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Invalid name: {self.name}. Name should be a non-empty string.'


class InvalidAgeError(Exception):
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return f'Invalid age: {self.age}. Age should be a positive integer.'


class InvalidIdError(Exception):
    def __init__(self, id_user):
        self.id_user = id_user

    def __str__(self):
        return f'Invalid id: {self.id_user}. Id should be a 6-digit positive integer between 100000 and 999999.'


class Person:
    def __init__(self, last_name, first_name, patronymic, age):
        if len(last_name) == 0 or not isinstance(last_name, str):
            raise InvalidNameError(last_name)
        if len(first_name) == 0 or not isinstance(first_name, str):
            raise InvalidNameError(first_name)
        if len(patronymic) == 0 or not isinstance(patronymic, str):
            raise InvalidNameError(patronymic)
        if age <= 0 or not isinstance(age, int):
            raise InvalidAgeError(age)
        self.last_name = last_name
        self.first_name = first_name
        self.patronymic = patronymic
        self.age = age

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.patronymic} {self.age}'

    def __repr__(self):
        return f'{self.last_name} {self.first_name} {self.patronymic} {self.age}'

    def birthday(self):
        return self.age + 1

    def get_age(self):
        return self.age


class Employee(Person):
    def __init__(self, last_name, first_name, patronymic, age, id_user=None):
        super().__init__(last_name, first_name, patronymic, age)
        if 100000 < id_user > 999999:
            self.id_user = id_user
        else:
            raise InvalidIdError(id_user)

    def __str__(self):
        return f'{self.id_user}, {self.last_name} {self.first_name} {self.patronymic} {self.age}'

    def __repr__(self):
        return f'{self.id_user}, {self.last_name} {self.first_name} {self.patronymic} {self.age}'

    def get_level(self):
        list_num = [int(number) for number in str(self.id_user)]
        return sum(list_num) % 7


if __name__ == '__main__':
    # 1
    # person = Person("", "John", "Doe", 30)
    # __main__.InvalidNameError: Invalid name: . Name should be a non-empty string.
    # 2
    # person = Person("Alice", "Smith", "Johnson", -5)
    # __main__.InvalidAgeError: Invalid age: -5. Age should be a positive integer.
    # 3
    # employee = Employee("Bob", "Johnson", "Brown", 40, 12345)
    # __main__.InvalidIdError: Invalid id: 12345. Id should be a 6-digit positive integer between 100000 and 999999.
    # 4
    person = Person("Alice", "Smith", "Johnson", 25)
    print(person.get_age())
    # 25

import pytest


class Person:
    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int):
        self.last_name = last_name.capitalize()
        self.first_name = first_name.capitalize()
        self.patronymic = patronymic.capitalize()
        self._age = age

    def full_name(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'

    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age


class Employee(Person):
    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int, position: str, salary: float):
        super().__init__(last_name, first_name, patronymic, age)
        self.position = position.title()
        self.salary = salary

    def raise_salary(self, percent: float):
        self.salary *= (1 + percent / 100)

    def __str__(self):
        return f'{self.full_name()} ({self.position})'


# Введите ваше решение ниже

def test_employee_full_name():
    r1 = Employee("Ivanov", "Ivan", "ivanovich", 30, "manager", 50000)
    assert r1.full_name() == "Ivanov Ivan Ivanovich"


def test_employee_birthday():
    r1 = Employee("Ivanov", "Ivan", "ivanovich", 30, "manager", 50000)
    r1.birthday()
    assert r1.get_age() == 31


def test_employee_raise_salary():
    r1 = Employee("Ivanov", "Ivan", "Ivanovich", 30, "manager", 50000)
    r1.raise_salary(10)
    assert r1.salary == 55000.0


def test_employee_str():
    r1 = Employee("Ivanov", "Ivan", "Ivanovich", 30, "manager", 50000)
    assert r1.__str__() == "Ivanov Ivan Ivanovich (Manager)"


def test_employee_last_name_title():
    r1 = Employee("Ivanov", "Ivan", "ivanovich", 30, "manager", 50000)
    assert r1.last_name == "Ivanov"


if __name__ == "__main__":
    pytest.main()

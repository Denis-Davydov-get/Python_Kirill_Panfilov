# �������� ����� � ������� ����������� � �������� ������ ����������:
# ? ������ ������,
# ? ������ �������.
class MyAppException(Exception):
    def __init__(self, message: str):
        self.msg = message

    def __str__(self):
        return f'������ ����������! {self.msg}'


class MyValueError(MyAppException):
    def __init__(self, value: int):
        super().__init__(f'�������� ��������: {value}')


class MyLevelError(MyAppException):
    def __init__(self, level: int):
        super().__init__(f'������ �������: {level}')

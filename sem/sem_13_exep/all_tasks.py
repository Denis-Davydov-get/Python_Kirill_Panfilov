"""������� �1
�������� �������, ������� ����������� �������� ������ ��
������������ �� ��� ���, ���� �� �� ����� ����� ���
������������ �����.
������������� �� �������� ������ ��� ����������.
"""


def num_input():
    while True:
        try:
            num = float(input("������� ����� ��� ������������ �����: "))
            if num == int(num):
                return int(num)
            return num
        except ValueError:
            print("������� �� �����! ���������� ��� ���")


print(num_input())


"""������� �2
�������� ������� ������ get ��� �������.
������ ������ ������� ������� ��������� ���� �
�������� �� ���������.
��� ��������� � ��������������� ����� ������� ������
���������� ��������� ��������.
���������� ������ ����� ��������� ����������.
"""
data_dict = {1: "one", 2: "two"}


def get_dict(dictionary: dict, key, default=None):
    try:
        return dictionary[key]
    except KeyError:
        return default


print(get_dict(data_dict, 1))  # one
print(get_dict(data_dict, 4))  # None
print(get_dict(data_dict, 5, default="������ ����� ���"))  # ������ ����� ���


"""������� �3
�������� ����� � ������� ����������� � �������� ������ ����������:
? ������ ������,
? ������ �������.
"""


class MyAppException(Exception):
    def __init__(self, message: str):
        self.msg = message

    def __str__(self):
        return f"������ ����������! {self.msg}"


class MyValueError(MyAppException):
    def __init__(self, value: int):
        super().__init__(f"�������� ��������: {value}")


class MyLevelError(MyAppException):
    def __init__(self, level: int):
        super().__init__(f"������ �������: {level}")


"""������� �4
���������� ������ �� �������� 8 ��� ������������ ������,
��� � ����������� ����� ����������� ���, ������
������������� � ������� ������� (�� 1 �� 7) ��������
���������� � JSON ����.
�������� ����� ������������, ������� ������ ��� ������ �
��������� ����������.
�������� �������� �������, ������� ��������� ����������
�� JSON ����� � ��������� ��������� �������������.
"""
import json
import os


class User:
    def __init__(self, name: str, u_id: str, u_lvl: int):
        self.name = name
        self.id = u_id
        self.lvl = u_lvl

    def __hash__(self):
        return hash(self.name + self.id)

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self.__hash__() == other.__hash__()

    def __repr__(self):
        return f"{self.name} (ID: {self.id}, ������� �������: {self.lvl})"


def input_name(message: str) -> str:
    return input(message)


def input_lvl(message: str, error_message: str, limits: tuple[int, int]) -> str:
    while True:
        level = input(message)
        if level.isdigit() and limits[0] <= int(level) <= limits[1]:
            return level
        print(error_message)


def input_id(
    message: str, error_message: str, id_is_exists: str, id_list: list[str]
) -> str:
    while True:
        user_id = input(message)
        if user_id.isdigit():
            if user_id not in id_list:
                return user_id
            else:
                print(id_is_exists)
        else:
            print(error_message)


def input_users(file_name: str) -> None:
    if os.path.exists(file_name):
        with open(file_name, "r", encoding="UTF-8") as file:
            users_dict = json.load(file)
    else:
        users_dict = {}
    users_id_list = [u_id for users in users_dict.values() for u_id in users]
    while True:
        user_name = input_name("������� ��� ������������: ")
        if not user_name:
            break
        user_id = input_id(
            "������� ID ������������: ",
            "ID ������ �������� ������������� �� ����!",
            "������������ � ����� ID ��� ����������!",
            users_id_list,
        )
        user_level = input_lvl(
            "������� ������� ������� ������������ �� 1 �� 7: ",
            "����� ������ ����� �� 1 �� 7!",
            (1, 7),
        )
        # users_levels_list = sorted(users_dict, key=lambda x: int(x))
        # users_dict = {user_lvl: users_dict[user_lvl] for user_lvl in users_levels_list}
        if user_level in users_dict:
            users_dict[user_level][user_id] = user_name
        else:
            users_dict[user_level] = {user_id: user_name}
        with open(file_name, "w", encoding="UTF-8") as file:
            json.dump(users_dict, file, indent=4, ensure_ascii=False, sort_keys=True)
        users_id_list.append(user_id)


def make_user_from_json(file_name: str):
    result = set()
    with open(file_name, "r", encoding="UTF-8") as json_file:
        users_data = json.load(json_file)
    for lvl, user in users_data.items():
        for u_id, name in user.items():
            result.add(User(name, u_id, lvl))
    return result


input_users("user_list.json")
print(make_user_from_json("user_list.json"))


"""������� �5 + ������� �6
���������� ������ 3 � 4. �������� ����� �������, �������
����� ��������� ������:
�������� ������ (������� �� ������� 4)
���� � ������� - ������� ������� ��� � id ������������. ���
�������� ������� ������������ � ��������� �����������
���������� ����� �������� �� ��������� �������������.
���� ������ ������������ ���, ��������� ����������
�������. � ���� ������������ ����, �������� ��� ������� ��
��������� �������������.
���������� ������������. ���� ������� ������������
������, ��� ��� �������, ��������� ���������� ������
�������.
"""
import json

from main import User

# from app_exception import *  # �� �������� ��� ������ ��������� ���� � ���������� ����������


class Company:
    _company = None
    _file_name = None

    def __new__(cls, name: str = None, db_file: str = "user_list.json"):
        if cls._company is None:
            cls._company = super().__new__(cls)
            cls._company.name = name
            cls._file_name = db_file
            cls._company._logged_in = None
        return cls._company

    def __init__(self, *args, **kwargs):
        self._logged_in: User | None = None

    @property
    def users_list(self):
        result = set()
        for lvl, user in self._load_json().items():
            for u_id, name in user.items():
                result.add(User(name, u_id, lvl))
        return result

    @classmethod
    def _load_json(cls):
        with open(cls._file_name, "r", encoding="UTF-8") as json_file:
            return json.load(json_file)

    @classmethod
    def _save_json(cls, data: dict):
        with open(cls._file_name, "w", encoding="UTF-8") as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)

    def _add_new_user(self, new_user: User):
        users_data = self._load_json()
        if str(new_user.lvl) in users_data:
            users_data[str(new_user.lvl)][new_user.id] = new_user.name
        else:
            users_data[str(new_user.lvl)] = {new_user.id: new_user.name}
        self._save_json(users_data)

    def login(self, name: str, u_id: str):
        login_user = User(name, u_id, 0)
        if login_user in self.users_list:
            for user in self.users_list:
                if user == login_user:
                    print(
                        f"������������, {user.name}!\n����������� ������ �������! ��� ������� �������: {user.lvl}"
                    )
                    self._logged_in = user
                    return user.lvl
        raise MyAccessError(name, u_id)

    def logout(self):
        print(f"�� ��������, {self._logged_in.name}! �� ����� ������!")
        self._logged_in = None

    def new_user(self, user_name: str, u_id: str, new_lvl: int):
        if self._logged_in:
            if new_lvl < int(self._logged_in.lvl):
                raise MyLevelError(self._logged_in.lvl, new_lvl)
            new_user = User(user_name, u_id, new_lvl)
            if new_user in self.users_list:
                raise MyIDError(u_id)
            self._add_new_user(new_user)
        else:
            raise MyLoginError()


if __name__ == "__main__":
    a = Company("GB")
    a.login("������", "45")
    a.new_user("�����", "727", 3)
    a.logout()
    a.new_user("����", "234", 6)


"""������ ��������� ���������� ��� ������ 5/6"""

class MyAppException(Exception):
    def __init__(self, message: str):
        self.msg = message

    def __str__(self):
        return f"������ ����������! {self.msg}"


class MyAccessError(MyAppException):
    def __init__(self, name: str, u_id: str):
        super().__init__(
            f"������������ � ����� ������ ({name}) � ID({u_id}) �� ����������!"
        )


class MyLevelError(MyAppException):
    def __init__(self, my_level: int, new_level: int):
        super().__init__(
            f"������ �������! ������� ������� ������ ������������ ({new_level}) ������ ������ ������ ({my_level})"
        )


class MyIDError(MyAppException):
    def __init__(self, u_id: str):
        super().__init__(f"������������ � ����� ID ({u_id}) ��� ����������!")


class MyLoginError(MyAppException):
    def __init__(self):
        super().__init__(f"������������ �� �����������!")
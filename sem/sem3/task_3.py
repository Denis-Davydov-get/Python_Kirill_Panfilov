# Пользователь вводит данные. Сделайте проверку данных
# и преобразуйте если возможно в один из вариантов ниже:
# ✔ Целое положительное число
# ✔ Вещественное положительное или отрицательное число
# ✔ Строку в нижнем регистре, если в строке есть хотя бы одна заглавная буква
# ✔ Строку в нижнем регистре в остальных случаях


def search_type(var_1):
    if isinstance(var_1, int):
        return 'type - {var_1} - int'
    elif isinstance(var_1, float):
        return 'type - {var_1} - float'
    elif isinstance(var_1, str):
        return 'type - {var_1} - str'
    elif isinstance(var_1, bool):
        return 'type - {var_1} - bool'
    else:
        return 'Вы ничего не ввели'

list_1 = ['text', 69, 69.12, False]

for _ in list_1:
    print(search_type(_))
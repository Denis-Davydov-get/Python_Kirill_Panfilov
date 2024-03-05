# ✔ Напишите программу, которая получает целое число и возвращает его двоичное, восьмеричное строковое представление.
# ✔ Функции bin и oct используйте для проверки своего результата, а не для решения.
# Дополнительно:
# ✔ Попробуйте избежать дублирования кода
# в преобразованиях к разным системам счисления
# ✔ Избегайте магических чисел
# ✔ Добавьте аннотацию типов где это возможно
#
# BIN = 2
# OCT = 8
#
# number = 46
# print(bin(number))
# string = ""
# while number != 0:
#     string = str(number % BIN) + string
#     number //= BIN
#
# print('0b' + string)
#
#
BIN = 2
OCT = 8
number = 46


def num_to_base(orig_number, base):
    result = ''
    while orig_number != 0:
        result = str(orig_number % base) + result
        orig_number //= base
    return result


print('0b' + num_to_base(number, BIN))
print(bin(number))
print('0o' + num_to_base(number, OCT))
print(oct(number))

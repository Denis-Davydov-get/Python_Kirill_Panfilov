# Вы работаете над разработкой программы для проверки корректности даты, введенной пользователем.
# На вход будет подаваться дата в формате "день.месяц.год".
# Ваша задача - создать программу, которая проверяет, является ли введенная дата корректной или нет.
# Ваша программа должна предоставить ответ "True" (дата корректна) или "False" (дата некорректна)
# в зависимости от результата проверки.
# Input:
# date_to_prove = 15.4.2023
#
# Output:
# True
test_list = ['15.4.2023', '0.5.2022', '12.0.2022', '12.5.-2022', '29.2.2020', '12.5.2022', '28.2.2021', '31.12.9999',
             '32.5.2022', '12.13.2022', '29.2.2021', '30.2.2020']
# date_to_prove = '15.4.2023' # -> True
# date_to_prove = '0.5.2022' # -> False
# date_to_prove = '12.0.2022' # -> False
# date_to_prove = '12.5.-2022' # -> False
# date_to_prove = '29.2.2020' # -> True
# date_to_prove = '12.5.2022' # -> True
# date_to_prove = '28.2.2021'  # -> True //
# date_to_prove = '31.12.9999' #-> True
# date_to_prove = '32.5.2022' #-> False
# date_to_prove = '12.13.2022' #-> False
# date_to_prove = '29.2.2021' #-> False
date_to_prove = '30.2.2020' #-> False

def _year_funс(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False


def true_data(data):
    day, month, year = [int(el) for el in data.split('.')]
    month_30 = (4, 6, 9, 11)
    month_31 = (1, 3, 5, 7, 8, 10, 12)
    if year > 9999 or 0 >= year or month > 12 or month <= 0:
        return False
    if month in month_30:
        if 0 < day < 31:
            return True
        return False
    elif month in month_31:
        if 0 < day < 32:
            return True
        return False
    elif month == 2:
        if _year_funс(year):  # если високосный
            if 0 < day <= 29:
                return True
            return False
        if _year_funс(year) == False and 0 < day <= 28:
            return True
        return False
    else:
        if 0 < day < 30:
            return True
        return False


# print(true_data(date_to_prove))
# for i in test_list:
#     print(f'{i}, {true_data(i)}')


# Эталонное решение
# from sys import argv
#
# def is_leap(year: int) :
#     return not (year % 4 != 0 or (year % 100 == 0 and year % 400 != 0))
#
# def valid(full_date: str) :
#     date, month, year = (int(item) for item in full_date.split('.'))
#     if year < 1 or year > 9999 or month < 1 or month > 12 or date < 1 or date > 31:
#         return False
#     if month in (4, 6, 9, 11) and date > 30:
#         return False
#     if month == 2 and is_leap(year) and date > 29:
#         return False
#     if month == 2 and not is_leap(year) and date > 28:
#         return False
#     return True
#
# if len(argv) > 1:
#     print(valid(argv[1]))
# else:
#     print(valid(date_to_prove ))


# import datetime
# try:
#     datetime.datetime.strptime(date_to_prove, "%d.%m.%Y").date()
#     print(True)
# except Exception:
#     print(False)
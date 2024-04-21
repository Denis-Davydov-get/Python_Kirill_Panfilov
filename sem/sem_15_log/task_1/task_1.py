# Напишите программу, которая использует модуль logging для
# вывода сообщения об ошибке в файл.
# Например отлавливаем ошибку деления на ноль.


import logging

logging.basicConfig(filename='errors.log', level=logging.ERROR, encoding='utf8')


def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError as e:
        # Логирование ошибки деления на ноль
        logging.error(f"Ошибка деления на ноль: {e}")
        return None


result = divide_numbers(10, 0)
print(result)

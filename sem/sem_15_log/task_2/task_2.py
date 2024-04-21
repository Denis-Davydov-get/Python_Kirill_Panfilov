# На семинаре про декораторы был создан логирующий декоратор.
# Он сохранял аргументы функции и результат её работы в файл.
# Напишите аналогичный декоратор, но внутри используйте модуль logging.

import logging

logging.basicConfig(filename='history.log', level=logging.INFO, encoding='utf8')


def logg(func):
    def wrapper(*args, **kwargs):
        logging.info(f'{func.__name__} {args} {kwargs}')
        result = func(*args, **kwargs)
        logging.info(f'{func.__name__}: {result}')
        return result

    return wrapper


@logg
def tes(a, b):
    return a + b


print(tes(5, 4))

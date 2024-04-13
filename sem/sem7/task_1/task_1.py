# ✔ Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.
import random

MIN_NUM = -1000
MAX_NUM = 1000


def random_pairs_of_numbers(num, name_file):
    with open(name_file, 'a', encoding='utf-8') as f:
        for _ in range(num):
            int_num = random.randint(MIN_NUM, MAX_NUM)
            float_num = random.uniform(MIN_NUM, MAX_NUM)
            f.write(f'{int_num} | {float_num}\n')


random_pairs_of_numbers(100, 'test.txt')
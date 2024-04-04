import csv
import json
import random


def generate_csv_file(file_name, rows):
    '''
    Генерирует по три случайны числа в каждой строке, от 100-1000 строк, и записывать их в CSV-файл
    @ file_name (строка) - имя файла, в который будут записаны данные.
    @ rows(целое число) - количество строк (записей) данных, которые нужно сгенерировать.
    '''
    with open(file_name, 'w', encoding='utf-8') as f:
        file_writer = csv.writer(f, delimiter=",", lineterminator="\r")
        for i in range(rows):
            file_writer.writerow([str(random.randint(100, 1000)),
                                  str(random.randint(100, 1000)),
                                  str(random.randint(100, 1000))])


def save_to_json(func):
    def generate_json_file(*args):
        data = []
        with open(args[0], 'r', encoding='utf-8') as f:
            for line in f:
                a, b, c = map(int, line.split(','))
                result = func(a, b, c)
                data.append({'parameters': [a, b, c], 'result': result})
        with open('results.json', 'w') as f:
            json.dump(data, f)

    return generate_json_file


@save_to_json
def find_roots(a, b, c):
    '''
    Находит корни квадратного уравнения вида
    input:
    @ a, b, c (целые числа) - коэффициенты квадратного уравнения.
    output:
    None, если уравнение не имеет корней (дискриминант отрицателен).
    Одно число, если уравнение имеет один корень (дискриминант равен нулю).
    Два числа (корни), если уравнение имеет два корня (дискриминант положителен).
    '''
    res = b ** 2 - 4 * a * c
    if res < 0:
        return None
    elif res < 0:
        return res
    else:
        return res


generate_csv_file("input_data.csv", 101)
find_roots("input_data.csv")

with open("results.json", 'r', encoding='utf-8') as f:
    data = json.load(f)

if 100 <= len(data) <= 1000:
    print(True)
else:
    print(f"Количество строк в файле не находится в диапазоне от 100 до 1000.")

print(len(data) == 101)

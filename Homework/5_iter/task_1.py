"""
Напишите функцию get_file_info, которая принимает на вход строку - абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
Пример использования.
На входе:
file_path = "C:/Users/User/Documents/example.txt"
file_path = '/home/user/data/file.py'
file_path = 'D:/myfile.txt'
file_path = 'C:/Projects/project1/code/script.py'
file_path = '/home/user/docs/my.file.with.dots.txt'
file_path = 'file_in_current_directory.txt'

На выходе:
('C:/Users/User/Documents/', 'example', '.txt')
"""

# эталонное решение
def get_file_info(file_path):
    file_name = file_path.split("/")[-1]  # обращение к последнему элементу списка, после разделения /
    file_extension = file_name.split(".")[-1]
    # обращение к последнему элементу списка после разделения '.', который текст
    path = file_path[:-len(file_name)]  # убираем из исходной строки количество знаков исходя из имени файлов
    return path, file_name[:-len(file_extension) - 1], "." + file_extension


# решение с использованием модуля os
import os


def split_path(path: str) -> tuple[str]:
    return os.path.split(path)[0], *os.path.split(path)[-1].split('.')
# но не универасльное, так как если несколько точек то разобьет по много слов


print(split_path('C:/Projects/project1/code/script.py'))
# Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# ○ имя файла без расширения или название каталога,
# ○ расширение, если это файл,
# ○ флаг каталога,
# ○ название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя логирование.
from collections import namedtuple
import argparse
import os
import logging

FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
#
logging.basicConfig(filename='logs.log',
                    level=logging.INFO,
                    format=FORMAT,
                    datefmt='%d/%m/%Y %I:%M:%S',
                    encoding='utf-8')
logger = logging.getLogger(__name__)

# Создаем parser для ввода через консоль
parser = argparse.ArgumentParser(description='Содержимое папки')
parser.add_argument('path', type=str, help='enter path for parse, type "str"')
args = parser.parse_args()
# Создаем именованные списки для заполнения для файлов и директорий
Tuple_path_file = namedtuple('Tuple_path_file', ['name', 'extension', 'directory', 'parents_directory'])
Tuple_path_dir = namedtuple('Tuple_path_dir', ['name_directory', 'directory_flag', 'parents_directory'])


def parse_str(path_input: str) -> namedtuple:
    '''Проверят файл или папка на входе и логирует в файл, в формате namedtuple '''
    if os.path.exists(path_input):
        if os.path.isfile(path_input):
            name_file = os.path.basename(path_input).split(".")[0]
            extension = path_input.split(".")[-1]
            directory = os.path.isdir(path_input)
            parents_directory = os.path.dirname(path_input).split("\\")[-1]
            path_tuple_file = Tuple_path_file(name_file, extension, directory, parents_directory)
            logger.info(f'{path_tuple_file}')
            return path_tuple_file

        elif os.path.isdir(path_input):
            name_directory = os.path.basename(path_input)
            directory_flag = os.path.isdir(path_input)
            parents_directory = os.path.dirname(path_input).split("\\")[-1]
            path_tuple_dir = Tuple_path_dir(name_directory, directory_flag, parents_directory)
            logger.info(f'{path_tuple_dir}')
            return path_tuple_dir
    else:
        raise TypeError(logger.error(f'folder {path_input} not found'))


if __name__ == '__main__':
    # path_input = input('Input the path of your file: ')
    # parse_str(path_input)
    parse_str(args.path) # запуск через терминал

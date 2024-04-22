# Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# ○ имя файла без расширения или название каталога,
# ○ расширение, если это файл,
# ○ флаг каталога,
# ○ название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя логирование.
import sys
from collections import namedtuple
import os
import logging
import json
from typing import Type

logging.basicConfig(filename='logs.txt', filemode='a+', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)

# def split_list(var_str, n):

def new_json_file(dict_path: dict):
    '''takes a dictionary and writes it to a json file'''
    with open("list_dir.json", 'w', encoding='utf-8') as f:
        f.write(json.dumps(dict_path, indent=4, ensure_ascii=False))
    logger.info(f'{path_input} dictionary placed in file: list_dir.json.')
def file_or_dir(input_path: str) -> bool:
    '''Checks a file or directory as input'''
    if os.path.isfile(input_path):
        True
    elif os.path.isdir(input_path):
        False

def parse_path(input_path: str) -> Type[tuple]:
    '''They check the file or folder at the input and return the dictionary '''
    isfile = namedtuple([str], ['file', 'dir'])
    for root, folders, files in os.walk(input_path):
        for folder in folders:
            isfile[folder] = [files]
        return isfile
    logger.info(f'{path_input} all files placed in the dictionary.')





if __name__ == '__main__':
    # path_input = input('Input the path of your file: ')
    path_input = os.getcwd()
    print(path_input)
    # new_json_file(parse_path(path_input))


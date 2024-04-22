# Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# ○ имя файла без расширения или название каталога,
# ○ расширение, если это файл,
# ○ флаг каталога,
# ○ название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя логирование.

from collections import namedtuple
import os
import logging
import json

logging.basicConfig(filename='logs.txt', filemode='a+', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)

path_input = input('Input the path of your file: ')

def parse_str(path_input:str):
    '''Проверят файл или папка в вводе и кладет все в json файл, в виде словаря '''
    dict_path = {}
    for root, folders, files in os.walk(path_input):
        for folder in folders:
            dict_path[folder] = [files]
    with open("list_dir.json", 'w', encoding='utf-8') as f:
        f.write(json.dumps(dict_path, f, indent=4, ensure_ascii=False))
    logger.info(f'{path_input} all files are parsed.')


def file_or_dir(input_path: str):
    if os.path.isfile(input_path):
        logger.info(f'{input_path} is not a directory.')
    elif os.path.isdir(input_path):


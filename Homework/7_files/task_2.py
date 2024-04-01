"""Пакет для работы с файлами 1
Из созданных на уроке и в рамках домашнего задания функций, соберите пакет для работы с файлами.
Создайте файл __init__.py и запишите в него функцию rename_files
"""
import os

func_rename = """
import os

def rename_files(desired_name="new_file_",
                num_digits=3,
                source_ext="doc",
                target_ext="txt",
                ):
    os.chdir('test_folder')
    num = 0
    for name in os.listdir():
        if name.endswith(source_ext):
            num+=1
            new_name = f'{desired_name}{str(num).zfill(num_digits)}.{target_ext}'
            os.rename(name, new_name)
"""

name_list = [name.split(".")[0] for name in os.listdir() if os.path.isfile(name) and name != "__init__.py"]

with open("__init__.py", "w", encoding="utf-8") as f:
    f.write(f"__all__ = {name_list}\n")
    f.write(func_rename)

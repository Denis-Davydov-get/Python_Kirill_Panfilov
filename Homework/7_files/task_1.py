"""Функция группового переименования файлов
Напишите функцию группового переименования файлов в папке test_folder под названием rename_files.
Она должна:
a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется
порядковый номер.
b. принимать параметр количество цифр в порядковом номере.
c. принимать параметр расширение исходного файла. Переименование должно работать только для этих
файлов внутри каталога.
d. принимать параметр расширение конечного файла.
e. принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы
с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано.
Далее счётчик файлов и расширение. (!!! ЭТО УСЛОВНИЕ ТЕСТАМИ НЕ ПРОВЕРЯЕТСЯ!!!)
f. Папка test_folder доступна из текущей директории
"""
# Input:
# rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc")
# Output:
# new_file_008.doc, test.doc, new_file_004.doc, new_file_005.doc, new_file_007.doc, new_file_001.doc,
#  new_file_006.doc, new_file_003.doc, new_file_002.doc, new_file_009.doc, new_file_010.doc

import os
def rename_files(
    desired_name="new_file_",
    num_digits=3,
    source_ext="doc",
    target_ext="txt",
):
    os.chdir("test_folder")
    num = 0
    for name in os.listdir():
        if name.endswith(source_ext):
            num += 1
            new_name = f"{desired_name}{str(num).zfill(num_digits)}.{target_ext}"
            os.rename(name, new_name)

rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc")
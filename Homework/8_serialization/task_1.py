# Вам необходимо написать функцию traverse_directory(directory),
# которая будет выполнять обход директории и возвращать результаты в виде списка словарей.
import csv
import json
import os
import pickle
# Информация о директории добавляется в список results в виде словаря {'Path': path, 'Type': 'Directory', 'Size': size}.
from pathlib import Path

# После этого результаты должны быть сохранены в трех различных файлах (JSON, CSV и Pickle)
# с помощью функций save_results_to_json, save_results_to_csv и save_results_to_pickle.
# Файлы добавляются в список results в том порядке, в котором они встречаются при рекурсивном обходе директорий.
# При этом сначала добавляются файлы, а затем директории.
#
# Для каждого файла (name в files), сначала создается полный путь к файлу (path = os.path.join(root, name)),
# и затем получается размер файла (size = os.path.getsize(path)).
# Информация о файле добавляется в список results в виде словаря {'Path': path, 'Type': 'File', 'Size': size}.
#
# Затем, для каждой директории (name в dirs), также создается полный путь к директории (path = os.path.join(root, name))
# , и вызывается функция get_dir_size(path), чтобы получить размер всей директории с учетом ее содержимого.

path = Path(__file__).parents[1]


def get_dir_size(directory: str) -> float:
    folder_size = 0
    for dir_path, _, file_names in os.walk(directory):
        for file in file_names:
            folder_size += os.path.getsize(os.path.join(dir_path, file))
    return folder_size


def traverse_directory(directory: str):
    results = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            path = os.path.join(root, file)
            size = os.path.getsize(path)
            results.append({'Path': path, 'Type': 'File', 'Size': size})
        for dir in dirs:
            path = os.path.join(root, dir)
            size = get_dir_size(path)
            results.append({'Path': path, 'Type': 'Directory', 'Size': size})
    return results


def save_results_to_json(dict):
    with open('path_file.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(traverse_directory(dict), indent=3, ensure_ascii=False))


def save_results_to_csv(results, filename):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Path', 'Type', 'Size'])
        for result in results:
            writer.writerow([result['Path'], result['Type'], result['Size']])


def save_results_to_pickle(dict):
    res = pickle.dumps(dict, protocol=pickle.DEFAULT_PROTOCOL)
    with open('my_dict.pickle', 'wb') as f:
        pickle.dump(res, f)


def main():
    directory = input('Введите директорию: ')
    print('1. JSON', '2. CSV', '3. Pickle', end="\n")
    format = int(input('Выберите формат сохранения результатов: '))
    if format == 1:
        save_results_to_json(traverse_directory(directory), 'results.json')
    elif format == 2:
        save_results_to_csv(traverse_directory(directory), 'results.csv')
    elif format == 3:
        save_results_to_pickle(traverse_directory(directory), 'results.pickle')


if __name__ == '__main__':
    main()

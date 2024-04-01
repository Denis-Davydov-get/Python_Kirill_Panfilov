import os
import json
import csv
import pickle
from pathlib import Path


# Ваша задача - написать программу, которая принимает на вход директорию
# и рекурсивно обходит эту директорию и все вложенные директории.
# Результаты обхода должны быть сохранены в нескольких форматах: JSON, CSV и Pickle.


def get_dir_size(path):
    total_size = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            size = os.path.getsize(os.path.join(root, file))
            total_size += size
        for dir in dirs:
            total_size += get_dir_size(os.path.join(root, dir))
    return total_size


def traverse_directory(directory):
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

def save_results_to_json(results):
    with open('result.json', 'w') as f:
        json.dump(results, f)


def save_results_to_csv(results):
    with open('result.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Path', 'Type', 'Size'])
        for result in results:
            writer.writerow([result['Path'], result['Type'], result['Size']])


def save_results_to_pickle(results):
    with open('result.pickle', 'wb') as f:
        pickle.dump(results, f)

# directory = Path(__file__).parents[1]
directory = os.getcwd()
save_results_to_json(traverse_directory(directory))
save_results_to_csv(traverse_directory(directory))
save_results_to_pickle(traverse_directory(directory))


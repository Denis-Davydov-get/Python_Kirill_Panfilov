import os

name_list = [name.split(".")[0] for name in os.listdir() if os.path.isfile(name) and name != "__init__.py"]

function_names = [
    "def get_dir_size",
    "def save_results_to_json",
    "def save_results_to_csv",
    "def save_results_to_pickle",
    "def traverse_directory",
]

with open("__init__.py", "w", encoding="utf-8") as f:
    f.write(f"__all__ = {function_names}\n")
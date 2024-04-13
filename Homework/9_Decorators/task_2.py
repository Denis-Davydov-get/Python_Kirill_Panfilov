data = ["save_to_json", "find_roots", "generate_csv_file"]

with open("__init__.py", "w", encoding="utf-8") as f:
    f.write(f'__all__ = {data}')

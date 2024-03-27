__all__ = ['task_1', 'task_2']

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

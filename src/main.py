import os
import shutil
from shutil import SameFileError

import time
from datetime import datetime

base_destination = f"..\\"
target_destination = f".\\test"
extensions_and_folders = {
    "py": {".py", ".pyc"},
    "exe": {".exe"}
}


def flatten(s):
    return [item for sublist in s for item in sublist]


for root, dirs, files in os.walk(base_destination, topdown=False):
    # print(files)

    for file in files:

        if any(file.endswith(dict_val) for dict_val in flatten(list(extensions_and_folders.values()))):
            file_path = f"{root}\\{file}"
            creation_date = "{:%Y_%m_%d}".format(datetime.fromtimestamp(os.path.getctime(file_path)))

            print(f"{file_path} _________________ {creation_date}")

            try:
                os.makedirs(f"{target_destination}\\{creation_date}\\", exist_ok=True)
                shutil.copy2(file_path, f"{target_destination}\\{creation_date}\\")
            except SameFileError:
                pass

import os
import shutil
from shutil import SameFileError

import time
from datetime import datetime


target_destination = ".\\test\\"


for root, dirs, files in os.walk("..\\", topdown=False):
    # print(files)

    for file in files:
        if file.endswith(".py"):
            file_path = f"{root}\\{file}"
            creation_date = "{:%Y_%m_%d}".format(datetime.fromtimestamp(os.path.getctime(file_path)))

            print(f"{file_path} _________________ {creation_date}")

            try:
                os.makedirs(f"{target_destination}{creation_date}\\", exist_ok=True)
                shutil.copy2(file_path, f"{target_destination}{creation_date}\\")
            except SameFileError:
                pass

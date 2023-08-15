import os
import shutil
from shutil import SameFileError

# import time
from datetime import datetime

# my imports
import config
from helper_functions import flatten, get_keys_from_value


def photo_sort(base_destination, target_destination):
    for root, dirs, files in os.walk(base_destination, topdown=True):
        # print(files)

        for file in files:
            file_path = f"{root}\\{file}"
            file_extension = f".{file_path.split('.')[-1]}"
            creation_date = "{:%Y_%m_%d}".format(datetime.fromtimestamp(os.path.getctime(file_path)))
            extension_dict_key = get_keys_from_value(file_extension)

            if file_extension in flatten(list(config.extensions_and_folders.values())):
                for dict_key in extension_dict_key:
                    copy_location = f"{target_destination}\\{creation_date}\\{dict_key}\\"

                    print(f"File path: {file_path} \n"
                          f"Copying to: {copy_location} \n"
                          f"Creation date: {creation_date} \n"
                          f"File extension: {file_extension} \n"
                          f"Dict key copying to: {dict_key} \n"
                          f"Dict keys for extension: {extension_dict_key} \n\n")

                    try:
                        os.makedirs(copy_location, exist_ok=True)
                        shutil.copy2(file_path, copy_location)
                    except SameFileError:
                        pass

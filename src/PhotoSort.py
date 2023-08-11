import os

for root, dirs, files in os.walk("..\\", topdown=False):
    # print(files)

    for file in files:
        if file.endswith(".py"):
            print(f"{file} | {root} ")

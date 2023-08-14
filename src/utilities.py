import shutil

target_destination = ".\\test\\"


def atomic_delete(destination=target_destination):
    try:
        shutil.rmtree(destination)
    except FileNotFoundError:
        print("Lack of folder to delete")


atomic_delete()

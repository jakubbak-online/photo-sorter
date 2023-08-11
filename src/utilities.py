import shutil

target_destination = ".\\test\\"


def atomic_delete(destination=target_destination):
    shutil.rmtree(destination)


atomic_delete()

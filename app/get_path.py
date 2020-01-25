import os


def get_path():
    os.chdir("files")
    path = os.getcwd()
    os.chdir("../")
    return path
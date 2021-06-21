import os


def print_ext(path, ext):
    if os.path.isdir(path):
        for file in os.listdir(path):
            if file.endswith(ext) and os.path.isfile(path + os.sep + file):
                print('{}{:>20}'.format(path, file))
    else:
        print('Podana ścieżka nie jest katalogiem')

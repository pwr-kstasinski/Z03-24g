import os
import re
import sys


def build_tree(path: str, line_start: str = "") -> str:
    path = path.replace("\\", "/")
    files_and_folders = os.listdir(path)
    if len(files_and_folders) == 0:
        return ""
    res = ""
    last = files_and_folders[-1]
    for f in files_and_folders:
        line_middle = "└───" if f == last else "├───"
        res += line_start + line_middle + f + "\n"
        dir_path = path + "/" + f
        if os.path.isdir(dir_path):
            line_start_update = "    " if f == last else "│" + "   "
            res += build_tree(dir_path, line_start + line_start_update)
    return res


def main(argv):
    path = argv[0] if len(argv) > 0 else "."
    if os.path.isdir(path):
        print(build_tree(path))
    else:
        print("Not directory error")


if __name__ == '__main__':
    main(sys.argv[1:])

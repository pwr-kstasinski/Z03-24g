import re
import sys
from os import listdir
from typing import Optional

EXTENSION_FORMAT_ERROR = "Bad extension format detected. Extension should look like: .txt"
ARGUMENT_NOT_PASSED = "Argument is null"


def list_files_in_path_with_extension(path: str, extension: str) -> Optional[str]:
    if path is None or extension is None:
        print(ARGUMENT_NOT_PASSED)
        return None
    if not extension.startswith('.'):
        print(EXTENSION_FORMAT_ERROR)
        return None
    files_and_folders = listdir(path)
    pattern = r'^$'
    if extension == ".*":
        pattern = r'^.*\..*$'
    else:
        pattern = fr'^.*{extension}$'
    files_with_extension = filter(lambda f: re.match(pattern, f), files_and_folders)
    files_listed = "\n".join(files_with_extension)
    return files_listed


def main(argv):
    path = argv[0] if len(argv) > 0 else "."
    extension = argv[1] if len(argv) > 1 else ".*"
    print(list_files_in_path_with_extension(path, extension))


if __name__ == '__main__':
    main(sys.argv[1:])

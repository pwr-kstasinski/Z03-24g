from pathlib import Path


# tworzymy generator który rekursywnie dodaje prefixy by zachować odpowiednie wcięcia
space = '    '
branch = '│   '
notlast = '├── '
last = '└── '


def tree(dir_path: Path, prefix: str = ''):
    contents = list(dir_path.iterdir())
    pointers = [notlast] * (len(contents) - 1) + [last]
    for pointer, path in zip(pointers, contents):
        yield prefix + pointer + path.name
        if path.is_dir():
            extension = branch if pointer == notlast else space
            yield from tree(path, prefix+extension)


def print_tree(path: Path):
    for line in tree(path):
        print(line)

import sys
from typing import List


def sort(numbers: List[int]) -> List[int]:
    result = []
    while len(numbers):
        number = min(numbers)
        result.append(number)
        numbers.remove(number)
    return result


def main(argv):
    numbers = list(map(lambda x: int(x), argv))
    # sorted_numbers = sorted(numbers)
    sorted_numbers = sort(numbers)
    print(sorted_numbers)


if __name__ == '__main__':
    main(sys.argv[1:])

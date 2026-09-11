import sys

def random_number(array: list[int]) -> None:
    unique_set = set(array[1:])
    result = sorted(unique_set)

    for item in result:
        print(item)

array = []

for line in sys.stdin:
    array.append(int(line.strip()))

random_number(array)
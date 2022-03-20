from typing import Final

FILE_NAME: Final = "input.txt"


def read_pattern_in_file():
    with open(FILE_NAME, 'r') as f:
        return [[int(num) for num in line.split(' ')] for line in f if line.strip() != ""]

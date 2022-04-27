from typing import Final

PATTERN_FILE_NAME: Final = "input_pattern.txt"
MATRIX_FILE_NAME: Final = "input_matrix.txt"


def read_pattern_in_file():
    try:
        with open(PATTERN_FILE_NAME, 'r') as f:
            return [[int(num) for num in line.split(' ')] for line in f if line.strip() != ""]
    except:
        print("An error occurred while reading the", PATTERN_FILE_NAME, "file.")


def read_matrix_in_file():
    try:
        with open(MATRIX_FILE_NAME, 'r') as f:
            return [[int(num) for num in line.split(' ')] for line in f if line.strip() != ""]
    except:
        print("An error occurred while reading the", MATRIX_FILE_NAME, "file.")

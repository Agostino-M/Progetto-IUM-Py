from file_manager import read_pattern_in_file
from algorithm import rotate_matrix, print_matrix, find_pattern


def main():
    # the map we need to search
    matrix = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0, 0],
        [1, 0, 0, 0, 1, 0, 0]
    ]

    pattern = read_pattern_in_file()
    print_matrix(pattern)

    found = find_pattern(matrix, pattern)
    attempt = 0
    while not found and attempt < 3:
        pattern = rotate_matrix(pattern)
        found = find_pattern(matrix, pattern)
        print("A:", attempt)
        print_matrix(pattern)
        attempt += 1

    print(found)
    if found:
        print("Attempt: ", attempt)


# print_matrix(rotate_matrix(pattern))


if __name__ == "__main__":
    main()

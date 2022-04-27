from file_manager import read_pattern_in_file, read_matrix_in_file
from algorithm import rotate_matrix, print_matrix, find_pattern


def main():
    # get the original matrix
    matrix = read_matrix_in_file()

    # get the pattern to compare with the matrix
    pattern = read_pattern_in_file()
    # print_matrix(pattern)

    found = find_paCreattern(matrix, pattern)
    attempt = 0
    while not found and attempt < 3:
        pattern = rotate_matrix(pattern)
        found = find_pattern(matrix, pattern)
        # print("Attempt: ", attempt)
        # print_matrix(pattern)
        attempt += 1

    print("Found: ", found)
    if found:
        print("Attempt: ", attempt)


if __name__ == "__main__":
    main()

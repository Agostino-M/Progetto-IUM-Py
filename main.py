from algorithm import rotate_matrix, print_matrix


def main():
    # the map we need to search
    matrix = [
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0],
        [0, 1, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ]

    # the pattern we need to find
    pattern = [
        [0, 0, 1, 0, 0],
        [0, 1, 1, 1, 0],
        [1, 0, 0, 0, 1]
    ]

    print_matrix(rotate_matrix(pattern))


if __name__ == "__main__":
    main()

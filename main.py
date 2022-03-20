from algorithm import rotate_matrix, print_matrix, find_pattern_in_matrix


def main():
    # the map we need to search
    matrix = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 0]
    ]

    # the pattern we need to find
    pattern = [
        [0, 0, 1, 0, 0],
        [0, 1, 1, 1, 0],
        [1, 0, 0, 0, 1]
    ]

    found = find_pattern_in_matrix(matrix, pattern)
    attempt = 0
    while not found and attempt < 3:
        pattern = rotate_matrix(pattern)
        found = find_pattern_in_matrix(matrix, pattern)
        print("found:", found)
        print("A:", attempt)
        print_matrix(pattern)

        attempt += 1

    print(found)
    if found:
        print("Attempt: ", attempt)


# print_matrix(rotate_matrix(pattern))


if __name__ == "__main__":
    main()

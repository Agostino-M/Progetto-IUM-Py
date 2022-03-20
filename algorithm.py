import numpy as np


# old search
def explore(matrix, pattern, i, j):
    for row in pattern:
        for count, item in enumerate(row):
            if matrix[i + count][j] != item:
                return False
        j += 1
    return True


# old search
def find_pattern_in_matrixxx(matrix, pattern):
    for i, row in enumerate(matrix):
        for j, item in enumerate(row):

            if item == pattern[0][0] and len(matrix) - i >= len(pattern) and len(row) - j >= len(pattern[0]):
                print("----Explore ", i, j)
                if explore(matrix, pattern, i, j):
                    return True
    return False


def find_pattern_in_matrix(matrix, pattern):
    for i in range(len(matrix) - len(pattern)):
        for j in range(len(matrix[0]) - len(pattern[0]) + 1):
            submatrix = True
            for k in range(len(pattern)):
                for l in range(len(pattern[0])):
                    if matrix[i + k][j + l] == pattern[k][l]:
                        print("a[", (i + k), "][", (j + l), "] = b[", k, "][", l, "]")
                    else:
                        submatrix = False

            if submatrix:
                return True
    return False


# new search
def find_pattern(matrix, pattern):
    stop = False
    result = False
    for i in range(len(matrix)):
        if stop:
            break
        for j in range(len(matrix[0])):
            if (len(matrix) - i) < len(pattern):
                stop = True
                break
            if (len(matrix[0]) - j) < len(pattern[0]):
                break
            slice_matrix = np.array(matrix)[i:i + len(pattern), j:j + len(pattern[0])]
            result = is_identical(slice_matrix, np.array(pattern))
            if result:
                stop = True
                break
    return result


def is_identical(a, b):
    rows, cols = len(a), len(a[0])
    return all([a[i][j] == b[i][j] for j in range(cols) for i in range(rows)])


def rotate_matrix(matrix):
    transposed = transpose_matrix(matrix)
    matrix = np.copy(transposed)
    reverse = reverse_matrix(matrix)
    matrix = np.copy(reverse)
    return matrix


def transpose_matrix(matrix):
    matrix = list(zip(*matrix))
    return matrix


def reverse_matrix(matrix):
    m = len(matrix)
    n = len(matrix[0])

    for i in range(m):
        start = 0
        end = n - 1

        while start < end:
            matrix[i][start], matrix[i][end] = matrix[i][end], matrix[i][start]
            start += 1
            end -= 1

    return matrix


def print_matrix(matrix):
    print()
    for i in range(len(matrix)):
        print()
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=" ")
    print()

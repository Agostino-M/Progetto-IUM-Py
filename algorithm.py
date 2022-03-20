import numpy as np


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

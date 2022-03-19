import numpy as np


def explore(matrix, pattern, i, j):
    for row in pattern:
        for count, item in enumerate(row):
            if matrix[i + count][j] != item:
                return False
        j += 1
    return True


def find_pattern_in_matrix(matrix, pattern):
    for i, row in enumerate(matrix):
        for j, item in enumerate(row):

            if item == pattern[0][0] and len(matrix) - i >= len(pattern) and len(row) - j >= len(pattern[0]):
                if explore(matrix, pattern, i, j):
                    return True
    return False


def rotate_matrix(matrix):
    trasposed = transpose_matrix(matrix)
    matrix = np.copy(trasposed)
    matrix = reverse_matrix(matrix)
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

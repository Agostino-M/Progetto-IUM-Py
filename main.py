
from algorithm import find_pattern_in_matrix

# the map we need to search
matrix = [
    [1, 1, 0, 0, 1, 1, 10],
    [1, 1, 1, 0, 0, 1, 0],
    [1, 1, 0, 1, 1, 1, 0],
    [1, 1, 1, 0, 1, 1, 0]
]

# the pattern we need to find
pattern = [
    [10, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

print(find_pattern_in_matrix(matrix, pattern))

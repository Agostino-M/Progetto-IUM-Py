def explore(matrix, pattern, i, j):
    """
    for each column in the pattern we have to find
    compare it with what is present in the map (matrix)
    """
    for row in pattern:
        for count, item in enumerate(row):

            # compare the map with the pattern value we're up to
            # if it doesn;t match, return False and stop
            if matrix[i + count][j] != item:
                return False
        j += 1
    return True


def find_pattern_in_matrix(matrix, pattern):
    for i, row in enumerate(matrix):
        for j, item in enumerate(row):

            # if we have found the start of the pattern, then start exploring
            if item == pattern[0][0] and len(matrix) - i >= len(pattern) and len(row) - j >= len(pattern[0]):
                if explore(matrix, pattern, i, j):
                    return "FOUND IT!"


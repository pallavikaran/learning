"""
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example 1:
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4

1 0 1 0 0
1 0|1|1|1|
1 1|1|1|1|
1 0 0 1 0

Example 2:
Input: matrix = [["0","1"],["1","0"]]
Output: 1

0 |1|
|1|0

Example 3:
Input: matrix = [["0"]]
Output: 0
"""


def maximal_square(matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """
    if not matrix:
        return 0

    m = len(matrix) # row
    n = len(matrix[0]) # col
    temp_matrix = [[0] * n for i in range(0, m)] # dynamic matrix
    max_side = 0

    for row in range(0, m):
        for col in range(0, n):
            if matrix[row][col] == 1 or matrix[row][col] == "1": # if cell is having 1
                # check if it's an edge cell
                if row == 0 or col == 0:
                    temp_matrix[row][col] = 1
                # if not an edge cell calculate max top, left top and left cells
                else:
                    temp_matrix[row][col] = min(
                        temp_matrix[row - 1][col], # top
                        temp_matrix[row - 1][col - 1], # top left
                        temp_matrix[row][col - 1], # left
                    ) + 1 # +1 is for adding the actual cell from which we are calculating top, left, top-left

                max_side = max(max_side, temp_matrix[row][col])

    return max_side * max_side # area is side square


matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(maximal_square(matrix))

matrix = [["0","1"],["1","0"]]
print(maximal_square(matrix))


matrix = [["0"]]
print(maximal_square(matrix))


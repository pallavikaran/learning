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

    m = len(matrix)  # row
    n = len(matrix[0])  # col
    min_element_value_matrix = [[0] * n for i in range(0, m)]  # matrix that computes for each (row, col) what is the min value around it's top, left and top-left
    max_side = 0

    for row in range(0, m):
        for col in range(0, n):
            if matrix[row][col] == 1 or matrix[row][col] == "1":  # if cell is having 1
                # check if it's an edge cell, i.e left, top and top-left does not exist
                if row == 0 or col == 0:
                    min_element_value_matrix[row][col] = 1
                # if not an edge cell calculate max top, left top and left cells
                else:
                    # to form a bigger square top, top-left & left have to all be 1
                    min_element_value_matrix[row][col] = min(
                        min_element_value_matrix[row - 1][col],  # top
                        min_element_value_matrix[row - 1][col - 1],  # top left
                        min_element_value_matrix[row][col - 1],  # left
                    ) + 1  # +1 is for adding the actual cell from which we are calculating top, left, top-left. This is the sm,allest square

                max_side = max(max_side, min_element_value_matrix[row][col])

    return max_side * max_side # area is side square


matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(maximal_square(matrix))

matrix = [["0","1"],["1","0"]]
print(maximal_square(matrix))


matrix = [["0"]]
print(maximal_square(matrix))

"""
For each element in matrix, compute corresponding largest square side in min_element_value_matrix.
side * side is max area

matrix = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"]
]
min_element_value_matrix = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

Row 0:
(0,0): matrix[0][0] = "1" → first row → min_element_value_matrix[0][0] = 1 <- if row == 0 or col == 0
(0,1): "0" → min_element_value_matrix[0][1] = 0 <- skip hence default 0
(0,2): "1" → min_element_value_matrix[0][2] = 1 <- if row == 0 or col == 0
(0,3): "0" → min_element_value_matrix[0][3] = 0 <- skip hence default 0
(0,4): "0" → min_element_value_matrix[0][4] = 0 <- skip hence default 0
min_element_value_matrix = [
    [1, 0, 1, 0, 0]
    [0, 0, 0, 0, 0]
    [0, 0, 0, 0, 0]
    [0, 0, 0, 0, 0]
]    

Row 1:
(1,0): "1" → first column → dp[1][0] = 1 <- if row == 0 or col == 0
(1,1): "0" → dp[1][1] = 0 <- skip hence default 0
(1,2): "1" → min(1, 0, 0) + 1 = 1 <- else
(1,3): "1" → min(0, 1, 1) + 1 = 1 <- else
(1,4): "1" → min(0, 1, 0) + 1 = 1 <- else
min_element_value_matrix = [
    [1, 0, 1, 0, 0]
    [1, 0, 1, 1, 1]
    [0, 0, 0, 0, 0]
    [0, 0, 0, 0, 0]
]    

Row 2:
(2,0): "1" → first column → dp[2][0] = 1
(2,1): "1" → min(0, 1, 1) + 1 = 1
(2,2): "1" → min(1, 1, 0) + 1 = 1
(2,3): "1" → min(1, 1, 1) + 1 = 2
(2,4): "1" → min(1, 2, 1) + 1 = 2
min_element_value_matrix = [
    [1, 0, 1, 0, 0]
    [1, 0, 1, 1, 1]
    [1, 1, 1, 2, 2]
    [0, 0, 0, 0, 0]
]

Row 3:
(3,0): "1" → first column → dp[3][0] = 1
(3,1): "0" → dp[3][1] = 0
(3,2): "0" → dp[3][2] = 0
(3,3): "1" → min(2, 0, 1) + 1 = 1
(3,4): "0" → dp[3][4] = 0
min_element_value_matrix = [
    [1, 0, 1, 0, 0]
    [1, 0, 1, 1, 1]
    [1, 1, 1, 2, 2]
    [1, 0, 0, 1, 0]
]
"""
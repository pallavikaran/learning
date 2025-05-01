"""
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

1 → 2 → 3
        ↓
4 → 5   6
↑       ↓
7 ← 8 ← 9

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

1 → 2 → 3 → 4
            ↓
5 → 6 → 7   8
↑           ↓
9 ←10 ←11 ←12


Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""


def spiral_order(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    result = []
    if not matrix:
        return result

    # set boundaries of the matrix
    top_row_index = 0  # index of the topmost row you haven't processed yet
    bottom_row_index = len(matrix) - 1  # index of the bottommost row you haven't processed yet
    left_col_index = 0  # index of the leftmost column you haven't processed yet
    right_col_index = len(matrix[0]) - 1  # index of the rightmost column you haven't processed yet

    while top_row_index <= bottom_row_index and left_col_index <= right_col_index:
        # Traverse top row (left to right)  →
        for col in range(left_col_index, right_col_index + 1):
            result.append(matrix[top_row_index][col])
        top_row_index += 1

        # Traverse right column (top to bottom) ↓
        for row in range(top_row_index, bottom_row_index + 1):
            result.append(matrix[row][right_col_index])
        right_col_index -= 1

        # Traverse bottom row (right to left) ←
        if top_row_index <= bottom_row_index:
            for col in range(right_col_index, left_col_index - 1, -1):
                result.append(matrix[bottom_row_index][col])
            bottom_row_index -= 1

        # Traverse left column (bottom to top) ↑
        if left_col_index <= right_col_index:
            for row in range(bottom_row_index, top_row_index - 1, -1):
                result.append(matrix[row][left_col_index])
            left_col_index += 1

    return result


matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(spiral_order(matrix))

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(spiral_order(matrix))

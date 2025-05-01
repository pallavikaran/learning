"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

111     101
101  => 000
111     111

Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

0120      0000
3452  =>  0450
1315      0310

Constraints:
m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1

Follow up:
A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""


def set_zeroes(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    m = len(matrix) # len(matrix) = no of rows
    n = len(matrix[0]) # length(Row[0]) = no of cols

    # Create markers
    # We're using the first row/column to store marker zeros. If the first row/col originally had real 0s,
    # we’d lose that info so we save that info separately in flags to handle them in last step
    first_row_has_zero = False
    first_col_has_zero = False

    # Check if the first row needs to be zeroed
    for col_index in range(0, n):
        if matrix[0][col_index] == 0:
            first_row_has_zero = True
            break

        # Check if the first col needs to be zeroed
    for row_index in range(0, m):
        if matrix[row_index][0] == 0:
            first_col_has_zero = True
            break

            # Using markers, iterate through the remainder of the matrix(minus 1st row and 1st col)
    for row_index in range(1, m):
        for col_index in range(1, n):
            if matrix[row_index][col_index] == 0:
                # Adjust the marker rows and col with 0 if applicable.(1st row and 1st col)
                matrix[0][col_index] = 0
                matrix[row_index][0] = 0

    # [
    #     [1, 0, 1],   # first row shows column 1 needs to be zeroed
    #     [0, 0, 1],   # first column shows row 1 needs to be zeroed
    #     [1, 1, 1]
    # ]

    for row_index in range(1, m):
        for col_index in range(1, n):
            if matrix[0][col_index] == 0 or matrix[row_index][0] == 0: # if markers are set to 0
                # Adjust the non-marker rows and col with 0 if applicable.(minus 1st row and 1st col)
                matrix[row_index][col_index] = 0
    # [
    #     [1, 0, 1],
    #     [0, 0, 0],
    #     [1, 0, 1]
    # ]

    # iterate through marker row and columns to see if they are having original/real 0
    # For 0s in original/real first row
    if first_row_has_zero:
        for col_index in range(0, n):
            matrix[0][col_index] = 0

    # For 0s in original/real col row
    if first_col_has_zero:
        for row_index in range(0, m):
            matrix[row_index][0] = 0

    return matrix


matrix = [[1,1,1],[1,0,1],[1,1,1]]
print(set_zeroes(matrix))

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print(set_zeroes(matrix))

matrix = [[1,0]]
print(set_zeroes(matrix))

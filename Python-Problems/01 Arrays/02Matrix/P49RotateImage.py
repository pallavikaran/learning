"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

1 2 3       7 4 1
4 5 6  =>   8 5 2
7 8 9       9 6 3

Example 2:
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]


Constraints:
n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
"""

"""
1 2 3      1 4 7        7 4 1
4 5 6  =>  2 5 8   =>   8 5 2
7 8 9      3 6 9        9 6 3
Original   Transposed   Reversed
"""


def rotate_90(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    # 90 degree -> Transpose(row -> col, col-> rows) then Reverse matrix
    # 180 degree -> Reverse matrix twice
    # 360 degree -> Return original matrix

    # Transpose Matrix
    for row_itr in range(0, len(matrix)):
        for col_itr in range(row_itr + 1, len(matrix)):
            matrix[row_itr][col_itr], matrix[col_itr][row_itr] = matrix[col_itr][row_itr], matrix[row_itr][col_itr]

    # Reverse the matrix
    for row in matrix:
        row.reverse()

    return matrix


matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate_90(matrix))

matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
print(rotate_90(matrix))



"""
1 2 3       3 2 1
4 5 6  =>   6 5 4
7 8 9       9 8 9
Original    Reversed
"""


def rotate_180(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    # 90 degree -> Transpose(row -> col, col-> rows) then Reverse matrix
    # 180 degree -> Reverse matrix twice
    # 360 degree -> Return original matrix

    # Transpose Matrix
    for row_itr in range(0, len(matrix)):
        for col_itr in range(row_itr + 1, len(matrix)):
            matrix[row_itr][col_itr], matrix[col_itr][row_itr] = matrix[col_itr][row_itr], matrix[row_itr][col_itr]

    # Reverse the matrix
    for row in matrix:
        row.reverse()

    return matrix


matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate_180(matrix))

matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
print(rotate_180(matrix))


def rotate_360(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    # 90 degree -> Transpose(row -> col, col-> rows) then Reverse matrix
    # 180 degree -> Reverse matrix twice
    # 360 degree -> Return original matrix

    # Transpose Matrix
    for row_itr in range(0, len(matrix)):
        for col_itr in range(row_itr + 1, len(matrix)):
            matrix[row_itr][col_itr], matrix[col_itr][row_itr] = matrix[col_itr][row_itr], matrix[row_itr][col_itr]

    # Reverse the matrix
    for row in matrix:
        row.reverse()

    return matrix


matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate_360(matrix))

matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
print(rotate_360(matrix))

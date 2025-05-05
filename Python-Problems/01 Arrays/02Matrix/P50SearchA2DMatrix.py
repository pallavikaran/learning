"""
You are given an m x n integer matrix matrix with the following two properties:
Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.
You must write a solution in O(log(m * n)) time complexity.

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

1   3   5   7
10  11  16  20
23  30  34  60

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
"""

"""
Binary Search Strategy:
Treat the matrix as a virtual 1D array of length m * n.
For a given index k in the 1D view:
1. Row = k // n
2. Column = k % n
3. Apply binary search using these conversions.
"""


def search_matrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    if not matrix or not matrix[0]:
        return False

    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1 # Since indices are 0-based, the last index in this flattened array is m * n - 1

    while left <= right:
        mid = (left + right) // 2
        row, col = divmod(mid, n) # divmod(a, b) returns: (a // b, a % b) ex: row, col = divmod(6, 4)  # returns (1, 2)
        # mid // n gives the row index, mid % n gives the column index.
        mid_val = matrix[row][col]

        if mid_val == target:
            return True
        elif mid_val < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


print(search_matrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
print(search_matrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 17))

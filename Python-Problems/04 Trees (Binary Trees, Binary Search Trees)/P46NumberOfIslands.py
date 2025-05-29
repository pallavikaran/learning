"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""
"""
Row ↓ / Col →  0   1   2   3   4
            ┌───┬───┬───┬───┬───┐
        0   │ 1 │ 1 │ 0 │ 0 │ 0 │
            ├───┼───┼───┼───┼───┤
        1   │ 1 │ 1 │ 0 │ 0 │ 0 │
            ├───┼───┼───┼───┼───┤
        2   │ 0 │ 0 │ 1 │ 0 │ 0 │
            ├───┼───┼───┼───┼───┤
        3   │ 0 │ 0 │ 0 │ 1 │ 1 │
            └───┴───┴───┴───┴───┘

Island A → connected block of 1s:
  (0,0), (0,1)
  (1,0), (1,1)

Island B → standalone 1 at (2,2)

Island C → connected block at:
  (3,3), (3,4)
"""


def num_is_ilands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    # Edge case: empty grid
    if not grid:
        return 0

    # Get grid dimensions
    rows, cols = len(grid), len(grid[0])
    count = 0  # To count number of islands

    # Depth-First Search helper function
    def dfs(r, c):
        # Base case: if out of bounds or cell is water ('0'), stop
        if r < 0 or c < 0 or r >= rows or c >=cols or grid[r][c] == '0':
            return

            # Mark the current land cell as visited by converting it to water
        grid[r][c] = '0'

        # Recursively visit all 4 adjacent directions (up, down, left, right)
        dfs(r + 1, c)  # down
        dfs(r - 1, c)  # up
        dfs(r, c + 1)  # right
        dfs(r, c - 1)  # left

    # Loop through every cell in the grid
    for r in range(rows):
        for c in range(cols):
            # If the cell is land ('1'), it's a new island
            if grid[r][c] == '1':
                count += 1  # Increment island count
                dfs(r, c)  # Run DFS to mark the whole island as visited

    return count  # Return the total number of islands


grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]
print(num_is_ilands(grid))


grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]
print(num_is_ilands(grid))
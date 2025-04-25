"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

8     |         |
7     |~~~~~~~~~|~|
6     | |       | |
5     | |   |   | |
4     | |   | | | |
3     | |   | | | |
2     | | | | | | |
1     | | | | | | |
0   |_|_|_|_|_|_|_|
i = 0 1 2 3 4 5 6 7
Example 2:
Input: height = [1,1]
Output: 1
"""


def max_area(height):
    """
    :type height: List[int]
    :rtype: int
    """
    # This is a two pointer problem.
    # Left Pointer = starts from 0
    # right pointer = starts from len(height) - 1
    left_pointer = 0
    right_pointer = len(height) - 1
    max_area = 0  # water contained. length * breadth

    while left_pointer < right_pointer:
        area = min(height[left_pointer], height[right_pointer]) * (right_pointer - left_pointer)
        max_area = max(area, max_area)

        if height[left_pointer] < height[right_pointer]:
            left_pointer += 1
        else:
            right_pointer -= 1

    return max_area


height = [1,8,6,2,5,4,8,3,7]
print(max_area(height))

height = [1,1]
print(max_area(height))

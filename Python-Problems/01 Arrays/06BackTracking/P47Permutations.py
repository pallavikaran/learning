"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]

Constraints:
1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
"""
"""
Backtrack (remove the last number) and try the next one
"""


def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    result = []

    def back_tracking(path, used):
        if len(path) == len(nums): # Found one permutation sequence
            # add to list
            result.append(path[:])
            return

        for i in range(0, len(nums)):
            if not used[i]:
                path.append(nums[i])
                used[i] = True
                back_tracking(path, used) # backtrack from nums[i]
                # Remove last element after the path has been found and added to result
                path.pop()
                # Reset the flag to further iterate and backtrack
                used[i] = False

    # Call Backtracking method by passing inputs
    back_tracking([], [False] * len(nums))

    return result


nums = [1,2,3]
print(permute(nums))

nums = [0,1]
print(permute(nums))

nums = [1]
print(permute(nums))

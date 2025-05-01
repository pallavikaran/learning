"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1

Constraints:
1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.
"""
"""
XOR (exclusive OR) is a bitwise operator that compares two bits and returns:
1 if the bits are different
0 if the bits are the same
"""

def single_number(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    result = 0

    for num in nums:
        # Perform XOR
        result ^= num

    return result

nums = [2,2,1]
print(single_number(nums))

nums = [4,1,2,1,2]
print(single_number(nums))

nums = [1]
print(single_number(nums))
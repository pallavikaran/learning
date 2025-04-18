"""
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

Constraints:
n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
"""

def majority_element(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    temp_map = {}
    result = 0

    for num in nums:
        if num not in temp_map.keys():
            temp_map[num] = 1
        else:
            temp_map[num] = temp_map.get(num) + 1

    for k, v in temp_map.items():
        if result == 0:
            result = k
        elif v > temp_map[result]:
            result = k

    return result

nums = [3,2,3]
print(majority_element(nums))

nums = [2,2,1,1,1,2,2]
print(majority_element(nums))

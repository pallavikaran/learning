"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true
Explanation:
The element 1 occurs at the indices 0 and 3.

Example 2:
Input: nums = [1,2,3,4]
Output: false
Explanation:
All elements are distinct.

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Constraints:
1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""


def contains_duplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    nums_list = []
    if len(nums) > 0:
        for number in nums:
            if number not in nums_list:
                nums_list.append(number)
            else:
                return True

    return False


nums = [1,2,3,1]
print(contains_duplicate(nums))

nums = [1,2,3,4]
print(contains_duplicate(nums))

nums = [1,1,1,3,3,4,3,2,4,2]
print(contains_duplicate(nums))


def contains_duplicate_via_length(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    return len(nums) != len(set(nums))


nums = [1,2,3,1]
print(contains_duplicate_via_length(nums))

nums = [1,2,3,4]
print(contains_duplicate_via_length(nums))

nums = [1,1,1,3,3,4,3,2,4,2]
print(contains_duplicate_via_length(nums))

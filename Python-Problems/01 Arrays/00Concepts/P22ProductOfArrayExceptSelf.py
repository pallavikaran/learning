"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:
2 <= nums.length <= 105
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""


def product_except_self(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    all_product = 1
    zero_cnt = 0
    product_except_self_arr = [0] * (len(nums))

    for num in nums:
        if num != 0:
            all_product *= num
        else:
            zero_cnt += 1

    for i in range(0, len(nums)):
        if zero_cnt == 0:
            product_except_self_arr[i] = (all_product// nums[i])
        elif zero_cnt == 1 and nums[i] == 0:
            product_except_self_arr[i] = all_product
        elif zero_cnt == 1 and nums[i] != 0:
            product_except_self_arr[i] = 0
        elif zero_cnt > 1:
            return product_except_self_arr

    return product_except_self_arr


nums = [1,2,3,4]
print(product_except_self(nums))

nums = [-1,1,0,-3,3]
print(product_except_self(nums))

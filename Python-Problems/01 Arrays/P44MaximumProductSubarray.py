"""
Given an integer array nums, find a subarray that has the largest product, and return the product.
The test cases are generated so that the answer will fit in a 32-bit integer.

Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

Constraints:
1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any subarray of nums is guaranteed to fit in a 32-bit integer.
"""


def max_product(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # initializing with first element to avoid keeping 0 since it will multiply and make everything 0
    min_so_far = nums[0] # tracks min value so far vs incoming number
    max_so_far = nums[0] # tracks max value so far vs incoming number
    result = nums[0]

    for num in nums[1:]:
        if num < 0: # number is negative that means, we need to swap min and max to calculate correctly
            # - * - = +
            # + * - = -
            min_so_far, max_so_far = max_so_far, min_so_far

        min_so_far = min(num, min_so_far * num)
        max_so_far = max(num, max_so_far * num)

        result = max(result, max_so_far)

    return result


nums = [2,3,-2,4]
print(max_product(nums))

nums = [-2,0,-1]
print(max_product(nums))

nums = [2,3,-2,9]
print(max_product(nums))

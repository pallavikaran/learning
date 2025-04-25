"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Constraints:
3 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""


def three_sum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    result = []
    n = len(nums)
    # Step 1: Sort the array to avoid duplicates
    nums.sort() # asc

    for i in range(0, n - 2):  # Step 2: Set a pointer to iterate through until we reach the 3rd last number
        if i > 0 and nums[i] == nums[i-1]:
            continue # Skip duplicates for i

        left = i + 1  # A number after i (Num 2) since i is (Num 1)
        right = n - 1  # Last number in array (Num 3)

        while left < right:
            # Step 3: Check if the sum of 3 numbers is 0 then add to result
            total = nums[left] + nums[i] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1

                # skip duplicates for left and right WHILE they are same +1 -1
                # left
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                # right
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            # Adjust pointer based on total if not 0
            elif total < 0:
                left += 1  # increase left pointer to get closer to 0
            else:  # total > 0
                right -= 1  # decrease right pointer to get closer to 0

    return result


nums = [-1,0,1,2,-1,-4]
print(three_sum(nums))

nums = [0,1,1]
print(three_sum(nums))

nums = [0,0,0]
print(three_sum(nums))

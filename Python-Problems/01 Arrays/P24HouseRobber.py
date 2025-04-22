"""
THIS IS A SLIDING WINDOW PROBLEM
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.


Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 400
"""


def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    odd_house_profit = 0
    even_house_profit = 0

    for i in range(0, len(nums)):
        if (i % 2) == 0:
            even_house_profit += nums[i]
        else:
            odd_house_profit += nums[i]
    return max(odd_house_profit, even_house_profit)


nums = [1,2,3,1]
print(rob(nums))

nums = [2,7,9,3,1]
print(rob(nums))

nums = [2, 1, 1, 2]
print(rob(nums))

"""
h, good question! 👀 That solution almost feels right, but it misses a key part of the problem.

❌ Why this approach doesn’t work:
You're summing alternating houses — all evens vs. all odds — like this:

text
Copy
Edit
even indices: 0, 2, 4, ...
odd indices:  1, 3, 5, ...
Then you're just taking the max of those two totals.

BUT that’s not always optimal!

Sometimes the best choice is to rob:

two non-consecutive houses (not strictly even or odd)

like robbing index 1 and index 4 (odd + even)

The rule is "no two adjacent", not "only odd or even".

🔍 Example where your code fails:
python
Copy
Edit
nums = [2, 1, 1, 2]
Your approach:

Even indices (0, 2): 2 + 1 = 3

Odd indices (1, 3): 1 + 2 = 3

→ Returns 3

But the correct answer is:

Rob index 0 and 3 → 2 + 2 = 4

So the correct output is 4, not 3.

The Right Approach: Dynamic Programming
Instead of summing by index parity, we track:

The best total if we rob this house (num + dp[i-2])

The best total if we skip this house (dp[i-1])

We make the optimal choice at every house.
"""
"""
SLIDING WINDOW. THIS IS RIGHT SOLUTION
"""


def rob_sliding_window(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    prev_house_loot_one = 0 # Max loot up to house i-1
    prev_house_loot_two = 0 # Max loot up to house i-1

    # Sliding Window: prev_house_loot_two -> prev_house_loot_one -> current house

    for num in nums:
        take_house = num + prev_house_loot_two # alteranate house loot only
        skip_house = prev_house_loot_one
        temp_max = max(take_house, skip_house) # max money one can rob

        prev_house_loot_two = prev_house_loot_one
        prev_house_loot_one = temp_max # max money one can rob

    return prev_house_loot_one # max money one can rob


nums = [1,2,3,1]
print(rob_sliding_window(nums))

nums = [2,7,9,3,1]
print(rob_sliding_window(nums))

nums = [2, 1, 1, 2]
print(rob_sliding_window(nums))

nums = [2, 1, 1, 2]
assert rob_sliding_window(nums) != rob(nums), "Both functions are different yielding in diff max money"

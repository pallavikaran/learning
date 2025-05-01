"""
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""
"""
This is a Fibonacci sequence problem using Recursion with memoization
8 =  0, 1, 1, 2, 3, 5, 8, 13, 21
For any step n, the number of ways to reach it is the sum of ways to reach (n-1) and (n-2). 
This is because we can reach step n by either taking one step from (n-1) or (n-2).
Note that the case where we take 2 steps from (n-2) to (n) is also included in this because we will have to take one step from (n-1) in this case.
The time complexity of this solution is O(n), where n is the number of steps.
"""


def climb_stairs(n):
    """
    :type n: int
    :rtype: int
    """
    # Steps 1, 2
    if n <= 2:
        return n

    # Create a variable to track of all the steps
    # n + 1 so that index 0 is included, 3 = [0,0,0,0]
    ways = [0] * (n+1) # ways[0] = 0

    # Populate the variable with steps until 2
    ways[1] = 1
    ways[2] = 2

    for i in range(3, n+1): # to go to the end of the list while iterating i.e. n
        # Populates ways for each step till n calculating all the previous steps with 1 steps and 2 steps using Fibonacci sequence
        ways[i] = climb_stairs(n-1) + climb_stairs(n-2)
        print(ways)

    return ways[n] # n + 1 was added so we can return n which is the last position


n = 2
print(climb_stairs(n))

n = 3
print(climb_stairs(n))

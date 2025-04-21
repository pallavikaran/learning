"""
Fibonacci sequence is sum of last two numbers
This is a Fibonacci sequence problem using Recursion with memoization
8 =  0, 1, 1, 2, 3, 5, 8, 13, 21
5 = 0, 1, 1, 2, 3, 5
Video - https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/
Fn = Fn-1 + Fn-2
"""

def get_fibonacci_sequence(n):
    if n <= 1:
        return n

    # Recursive case: sum of the two preceding Fibonacci numbers
    return get_fibonacci_sequence(n-1) + get_fibonacci_sequence(n-2)

print(get_fibonacci_sequence(5))
print(get_fibonacci_sequence(8))
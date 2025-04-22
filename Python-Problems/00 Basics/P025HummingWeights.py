"""
Number of 1 Bits
Given a positive integer n, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight).


Example 1:
Input: n = 11
Output: 3
Explanation:
The input binary string 1011 has a total of three set bits.

Example 2:
Input: n = 128
Output: 1
Explanation:
The input binary string 10000000 has a total of one set bit.

Example 3:
Input: n = 2147483645
Output: 30
Explanation:
The input binary string 1111111111111111111111111111101 has a total of thirty set bits.

Constraints:
1 <= n <= 231 - 1
Follow up: If this function is called many times, how would you optimize it?
"""
"""
A bit is a single binary digit — either 0 or 1.
1 representing 2 from right and goes left 2 to thw power n
Number	  Binary	.bit_length()
1	           1	    1
2	          10	    2
5	         101	    3
13	        1101	    4
255	    11111111	    8
256	    100000000	    9

A set bit is 1. So we need to count total 1s in the bit form of the number

&= is a bitwise operator meaning AND 
1 AND 0 = 0, 0 AND 1 = 0
1 AND 1 = 1
0 AND 0 = 1
n = 12    

   n      = 1100  (12)
   n - 1  = 1011  (11)
---------------------
   n & n-1 = 1000  (8)
   
Initial n: 1101  (13)
Step 1:
n = 1101
n - 1 = 1100
n & (n - 1) = 1100  → removes the rightmost 1
count = 1

Step 2:
n = 1100
n - 1 = 1011
n & (n - 1) = 1000
count = 2

Step 3:
n = 1000
n - 1 = 0111
n & (n - 1) = 0000
count = 3

Loop ends. Final count = 3 ✅
"""


def hamming_weight(n):
    """
    :type n: int
    :rtype: int
    """
    set_bit_count = 0
    while n != 0:
        n &= (n - 1)  # converts to bitwise and performs AND
        set_bit_count += 1
    return set_bit_count


n = 11
print(hamming_weight(n))


n = 128
print(hamming_weight(n))


n = 2147483645
print(hamming_weight(n))

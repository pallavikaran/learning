"""
Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

Constraints:
1 <= s.length <= 105
s[i] is a printable ascii character.
"""


def reverse_string(s):
    """
    :type s: List[str]
    :rtype: None Do not return anything, modify s in-place instead.
    """
    left_indx = 0
    right_indx = len(s) - 1

    while left_indx < right_indx:
        s[left_indx], s[right_indx] = s[right_indx], s[left_indx]
        left_indx += 1
        right_indx -= 1

    return s


s = ["h","e","l","l","o"]
print(reverse_string(s))

s = ["H","a","n","n","a","h"]
print(reverse_string(s))
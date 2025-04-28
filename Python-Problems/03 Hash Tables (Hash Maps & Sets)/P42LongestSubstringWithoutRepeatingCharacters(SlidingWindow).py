"""
Given a string s, find the length of the longest substring without duplicate characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""
"""
Use two pointers: left and right to represent the current window of non-repeating characters.
Use a set (or a map) to track characters in the current window.
Expand the window by moving right; if a duplicate is found, shrink it from the left until there are no duplicates.
"""


def length_of_longest_substring(s):
    """
    :type s: str
    :rtype: int
    """

    char_set = set()
    left_ptr = 0
    max_length = 0

    for right_ptr in range(0, len(s)):
        while s[right_ptr] in char_set:
            char_set.remove(s[left_ptr])
            left_ptr += 1
        char_set.add(s[right_ptr])
        max_length = max(max_length, right_ptr - left_ptr + 1)

    return max_length


s = "abcabcbb"
print(length_of_longest_substring(s))

s = "bbbbb"
print(length_of_longest_substring(s))

s = "pwwkew"
print(length_of_longest_substring(s))

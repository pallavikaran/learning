"""
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"


Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters.
"""


def expand_from_center(s, left, right):
    # start - center - end
    # From the center checking values on both the sides if it is matching
    while left >= 0 and right < len(s) and (s[left] == s[right]):
        left -= 1
        right += 1
    # The last step made left too small or right too big, or the characters at left and right didn't match.
    return right - left - 1  # Resetting - Eliminating last iteration since while loop criteria is mot mey


def longest_palindrome(s):
    """
    :type s: str
    :rtype: str
    """
    if len(s) < 1:
        return s

    start = 0
    end = 0

    for i in range(0, len(s)):
        # i is the position for the center char
        length_1 = expand_from_center(s, i, i)  # Odd-length palindrome (bab)
        length_2 = expand_from_center(s, i, i+1)  # Even-length palindrome (bb)
        max_length = max(length_1, length_2)

        if max_length > (end - start):
            # updates the start and end indices of the longest palindrome found so far
            start = i - ((max_length - 1) // 2)  # Half the length to the left of the center
            end = i + (max_length // 2)  # Half the length to the right of the center

    return s[start:end+1]  # inclusive of the start index and exclusive of the end index


s = "babad"
print(longest_palindrome(s))

s = "cbbd"
print(longest_palindrome(s))

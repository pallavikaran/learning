"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

Constraints:
1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""


def is_palindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    cleansed_s = ''.join(char for char in s if char.isalpha())
    length_of_cleansed_s = len(cleansed_s)

    if cleansed_s%2 == 0:
        left_cleansed_s = cleansed_s[:cleansed_s/2 - 1]
        right_cleansed_s = cleansed_s[cleansed_s/2:]
    else:
        left_cleansed_s = cleansed_s[:cleansed_s/2 - 1]
        right_cleansed_s = cleansed_s[cleansed_s/2:]

    if left_cleansed_s == right_cleansed_s:
        return True
    else: return False
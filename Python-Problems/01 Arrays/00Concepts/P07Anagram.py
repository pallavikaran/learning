"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
"""

def char_count( word):
    char_cnt_map = {}

    for chars in word:
        if chars not in char_cnt_map.keys():
            char_cnt_map[chars] = 1
        else:
            char_cnt_map[chars] = char_cnt_map.get(chars) + 1

    return char_cnt_map


def is_anagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if char_count(s) == char_count(t):
        return True
    else:
        return False

s = "anagram"
t = "nagaram"
print(is_anagram(s, t))

s = "rat"
t = "car"
print(is_anagram(s, t))

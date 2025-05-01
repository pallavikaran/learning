"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Explanation:
There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:
1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""


def group_anagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    anagaram_groups = {} # key is sorted word and value is matching words in strs

    for word in strs:
        sorted_word = ''.join(sorted(word))
        if sorted_word not in anagaram_groups:
            anagaram_groups[sorted_word] = [word] # add the word to a new list
        else:
            anagaram_groups[sorted_word].append(word)

    return anagaram_groups.values()


strs = ["eat","tea","tan","ate","nat","bat"]
print(group_anagrams(strs))


strs = [""]
print(group_anagrams(strs))


strs = ["a"]
print(group_anagrams(strs))
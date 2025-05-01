"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true

Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""


def is_valid(s: str) -> bool:
    valid_parentheses_map = {'(': ')', '[': ']', '{': '}'}
    temp_lst = []
    for char in s:
        if char in valid_parentheses_map.keys():
            temp_lst.append(char)  # Push
        elif char in valid_parentheses_map.values():
            if len(temp_lst) > 0 and char == valid_parentheses_map.get(temp_lst.pop()):
                continue
            else:
                return False
        else:
            return False
    return True


print("()")
print(is_valid("()"))

print("()[]{}")
print(is_valid("()[]{}"))

print("([])")
print(is_valid("([])"))

print("(])")
print(is_valid("(])"))

print("(*)")
print(is_valid("(*)"))











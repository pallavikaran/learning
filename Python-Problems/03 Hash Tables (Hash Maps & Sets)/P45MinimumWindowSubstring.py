"""
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
The testcases will be generated such that the answer is unique.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 
Constraints:
m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
"""

"""
We use a sliding window with two pointers and a hash map to keep track of character frequencies.
Count the frequency of characters in t.
Start expanding the right pointer to find a valid window.
Once a valid window is found (i.e., it contains all characters from t), start shrinking from the left to minimize the window.
Keep track of the smallest window found.
"""

"""
s = "ADOBECODEBANC"
t = "ABC"
We need the smallest substring in s that contains all the characters of t: A, B, and C.

🔍 Step-by-Step Walkthrough
We'll use the code logic from before, step by step.

Initialization:
t_count = {'A':1, 'B':1, 'C':1}

window = {}

have = 0, need = 3 (since there are 3 unique characters in t)

res = [-1, -1], res_len = ∞

l = 0

Sliding Window Iteration
We move the right pointer r across s and adjust the left pointer l as needed.

1️⃣ r = 0 → s[0] = 'A'
window = {'A': 1}

'A' is in t_count and count matches → have = 1

Not valid yet (have=1, need=3).

2️⃣ r = 1 → s[1] = 'D'
window = {'A': 1, 'D': 1}

'D' not in t → have unchanged

3️⃣ r = 2 → s[2] = 'O'
window = {'A': 1, 'D': 1, 'O': 1}

4️⃣ r = 3 → s[3] = 'B'
window = {'A': 1, 'D': 1, 'O': 1, 'B': 1}

'B' matches → have = 2

5️⃣ r = 4 → s[4] = 'E'
Still not valid

6️⃣ r = 5 → s[5] = 'C'
window = {'A': 1, 'D': 1, 'O': 1, 'B': 1, 'E': 1, 'C': 1}

'C' matches → have = 3 ✅

✅ Valid window: s[0:5] = "ADOBEC"

Update result:

res = [0, 5], res_len = 6

Shrinking from left (l = 0):
Remove 'A': count goes to 0 → have = 2

Move l = 1

Continue expanding:
r = 6 → 'O'
r = 7 → 'D'
r = 8 → 'E'
r = 9 → 'B'
'B' count stays valid → have = 2

r = 10 → 'A'
'A' is back → count matches → have = 3 ✅

✅ Valid window again: s[6:10] = "ODEBA"
But length = 5, not better than previous (6)

Shrink from l again:

Keep moving left until invalid

Eventually:
When r = 12 → s[12] = 'C'

Window = "BANC"

All counts match → valid

✅ New best window = "BANC" (length 4)
Update: res = [9, 12], res_len = 4

🟢 Final Result:
python
Copy
Edit
return s[9:13] = "BANC"
✅ Summary:
Input:

python
Copy
Edit
s = "ADOBECODEBANC"
t = "ABC"
Output:

python
Copy
Edit
"BANC"
"""

from collections import Counter


def min_window(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    if s is None or t is None:
        return ""

    char_freq_in_t = Counter(t)  # Counter to count the characters in string t
    curr_window = {}  # This dictionary keeps the frequency of characters in the current window of s

    have_chars = 0  # counts how many of those required characters are matched in the current window (with the correct frequency).
    need_chars = len(char_freq_in_t)  # how many unique characters from t we need to match.

    result_substring_indexes = [-1, -1]  # s[ current start index, current end index] keeps track of the start and end of the smallest valid window found so far.
    result_min_length = float('inf')  # used to compare lengths and store the minimum

    left_ptr = 0  # Left pointer for the sliding window

    for right_ptr in range(0, len(s)):
        char = s[right_ptr]
        curr_window[char] = curr_window.get(char, 0) + 1  # add each character c to our window dictionary

        if char in char_freq_in_t and curr_window[char] == char_freq_in_t[char]:
            have_chars += 1  # If the character is in char_freq_in_t and we’ve met the exact required frequency, we increment have_chars

        while have_chars == need_chars: # Criteria is met, all chars in current window match all chars and freqs in char_freq_in_t, but the window could be larger or smaller
            # try to shrink the window from the left to find the smallest possible
            if (right_ptr - left_ptr - 1) < result_min_length: # -1 since the index starts from 0 and we are comparing lengths
                # update results to reflect current best matched substring
                result_substring_indexes = [left_ptr, right_ptr]
                result_min_length = right_ptr - left_ptr - 1

            # Pop from the left of the curr window
            curr_window[s[left_ptr]] -= 1

            # if removing a character breaks the requirement, reduce have
            if s[left_ptr] in char_freq_in_t and curr_window[s[left_ptr]] < char_freq_in_t[s[left_ptr]]:
                have_chars -= 1

            # increment left pointer post result and have adjustments
            left_ptr += 1

    if result_min_length != float('inf'):
        # shortest/minimal window substring
        substring_left_index, substring_right_index = result_substring_indexes
        return s[substring_left_index: substring_right_index + 1]
    else:
        return ""


s = "ADOBECODEBANC"
t = "ABC"
print(min_window(s, t))

s = "a"
t = "a"
print(min_window(s, t))

s = "a"
t = "aa"
print(min_window(s, t))

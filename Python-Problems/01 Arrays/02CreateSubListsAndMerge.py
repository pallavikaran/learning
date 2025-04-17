"""
Explanation - Video at bottom = https://www.geeksforgeeks.org/merge-sort/?ref=header_outind
Given an array with low, mid and high indexes(low/high/mid can be anywhere in between the list)
such that low <= mid < high and subarrays are sorted within itself
Subarray 1 = [low, mid]
Subarray 2 = [mid + 1, high]
"""

"""
Time Complexity = θ (m + n) where m = length(left_arr) and n = length(right_arr) We need to iterate through both m & n
Auxiliary Space: O(m + n), Additional space is required for the temporary array (result) used during merging
"""

def createSubListsAndMerge(arr, low, mid, high):

    left_arr = arr[low: mid+1] # subbing the array, left to : is included and right is not included len = 4 (0, 1, 2, 3)
    right_arr = arr[mid + 1 :high + 1] # len = 3 (4, 5, 6)

    # Merge two sorted arrays 01MergeTwoSortedArrays.py
    left_idx = 0
    right_idx = 0
    result = []

    while left_idx < len(left_arr) and right_idx < len(right_arr):
        if left_arr[left_idx] < right_arr[right_idx]:
            result.append(left_arr[left_idx])
            left_idx += 1
        else:
            result.append(right_arr[right_idx])
            right_idx += 1

    while left_idx < len(left_arr):
        result.append(left_arr[left_idx])
        left_idx += 1

    while right_idx < len(right_arr):
        result.append(right_arr[right_idx])
        right_idx += 1

    return result

# Sort all [10, 15, 20, 40, 8, 11, 55]
arr = [10, 15, 20, 40, 8, 11, 55]
low = 0
mid = 3
high = 6
print(createSubListsAndMerge (arr, low, mid, high))

# Sort between [15, 20, 40, 8, 11]
arr = [10, 15, 20, 40, 8, 11, 55]
low = 1
mid = 3
high = 5
print(createSubListsAndMerge (arr, low, mid, high))
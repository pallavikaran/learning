"""
Explanation - Video at bottom = https://www.geeksforgeeks.org/merge-sort/?ref=header_outind
Time Complexity:
     Best Case: O(n log n), When the array is already sorted or nearly sorted.
    Average Case: O(n log n), When the array is randomly ordered.
    Worst Case: O(n log n), When the array is sorted in reverse order.
Auxiliary Space: O(n), Additional space is required for the temporary array (result) used during merging
"""
# Using original list to modify than having extra result list
def merge_two_sorted_lists(original_arr, prev_idx_merged_subarr, left_arr, right_arr):
    # 01MergeTwoSortedLists.py
    left_arr_idx = 0
    right_arr_idx = 0

    while left_arr_idx < len(left_arr) and right_arr_idx < len(right_arr):
        if left_arr[left_arr_idx] < right_arr[right_arr_idx]:
            original_arr[prev_idx_merged_subarr] = left_arr[left_arr_idx]
            left_arr_idx += 1
        else:
            original_arr[prev_idx_merged_subarr] = right_arr[right_arr_idx]
            right_arr_idx += 1
        prev_idx_merged_subarr += 1

    while left_arr_idx < len(left_arr):
        original_arr[prev_idx_merged_subarr] = left_arr[left_arr_idx]
        left_arr_idx += 1
        prev_idx_merged_subarr += 1

    while right_arr_idx < len(right_arr):
        original_arr[prev_idx_merged_subarr] = right_arr[right_arr_idx]
        right_arr_idx += 1
        prev_idx_merged_subarr += 1


def createSubListsAndMerge(arr, left, mid, right):
    # 02CreateSubListsAndMerge.py
    left_sub_arr = arr[left: mid + 1]
    right_sub_arr = arr[mid + 1: right + 1]
    # With left & right sorted arrays, merge both in resulting sorted array
    merge_two_sorted_lists(arr, left, left_sub_arr, right_sub_arr)


def merge_sort(arr, left, right):
    if left < right:
        # find the middle
        mid = (left + right) // 2

        # Sorts elements. Keep dividing left side until left = mid
        merge_sort(arr, left, mid)
        # Sorts elements. After left meets base case, Keep dividing right side until mid + 1 = right
        merge_sort(arr, mid + 1, right)
        # Create sub arrays from orginal array using data from above sorted arrays
        createSubListsAndMerge(arr, left, mid, right)


arr = [10, 15, 20, 40, 8, 11, 55]
merge_sort(arr, 0, len(arr) - 1)
print(arr)
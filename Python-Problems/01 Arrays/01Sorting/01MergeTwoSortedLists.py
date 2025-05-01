"""
Explanation - Video at bottom = https://www.geeksforgeeks.org/merge-sort/?ref=header_outind
Time Complexity: O(len(arr1), len(arr2))
"""
def merge_two_sorted_lists(arr1, arr2):
    arr1_indx = 0
    arr2_indx = 0
    result = []

    while arr1_indx < len(arr1) and  arr2_indx < len(arr2):
        if arr1[arr1_indx] < arr2[arr2_indx]:
            result.append(arr1[arr1_indx])
            arr1_indx += 1
        else:
            result.append(arr2[arr2_indx])
            arr2_indx += 1

    while arr1_indx < len(arr1):
        result.append(arr1[arr1_indx])
        arr1_indx += 1

    while arr2_indx < len(arr2):
        result.append(arr2[arr2_indx])
        arr2_indx += 1

    return result


arr1 = [1, 2, 7, 10]
arr2 = [4,7,9]
print(merge_two_sorted_lists(arr1, arr2))

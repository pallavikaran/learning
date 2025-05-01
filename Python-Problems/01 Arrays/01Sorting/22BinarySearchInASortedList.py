"""
Binary search only works correctly on a sorted list or array
Return index of the element to be searched in a SORTED array
Time Complexity: O(log N)
Auxiliary Space: O(1)
"""
def binary_search_in_sorted_list(arr, search_element, low, high):
    if high >= low:
        mid = low + (high - low) // 2
        if search_element == arr[mid]:
            return mid
        elif search_element > arr[mid]:
            return binary_search_in_sorted_list(arr, search_element, mid + 1, high)
        else: # search_element < arr[mid]:
            return binary_search_in_sorted_list(arr, search_element, low, mid - 1)
    return -1


arr = [2, 3, 4, 10, 40]
search_element = 7
print(f"Searched element  {search_element} found at {binary_search_in_sorted_list(arr, search_element, 0, len(arr))} index")

arr = [2, 3, 4, 10, 40]
search_element = 10
print(f"Searched element  {search_element} found at {binary_search_in_sorted_list(arr, search_element, 0, len(arr))} index")

arr = [2, 3, 4, 10, 40]
search_element = 4
print(f"Searched element  {search_element} found at {binary_search_in_sorted_list(arr, search_element, 0, len(arr))} index")
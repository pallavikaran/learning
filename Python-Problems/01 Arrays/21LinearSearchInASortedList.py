"""
Return index of the element to be searched in a SORTED array
Time Complexity: θ (n), n = len(arr)
"""

def linear_search_in_sorted_list(arr, search_element):
    if len(arr) > 1:
        for i in range(0, len(arr)):
            if arr[i] == search_element:
                return i
        return -1
    else:
        return 0


arr = [10, 15, 20, 40, 8, 11, 55]
search_element = 7
print(f"Searched element  {search_element} found at {linear_search_in_sorted_list(arr, search_element)} index")

arr = [10, 15, 20, 40, 8, 11, 55]
search_element = 55
print(f"Searched element  {search_element} found at {linear_search_in_sorted_list(arr, search_element)} index")

arr = [10, 15, 20, 40, 8, 11, 55]
search_element = 10
print(f"Searched element  {search_element} found at {linear_search_in_sorted_list(arr, search_element)} index")
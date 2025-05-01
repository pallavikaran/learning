"""
QuickSort using Lomuto Partition
Two pointer problem
Video - https://www.geeksforgeeks.org/quick-sort-algorithm/
Time Complexity:
Best Case: (Ω(n log n)), Occurs when the pivot element divides the array into two equal halves.
Average Case (θ(n log n)), On average, the pivot divides the array into two parts, but not necessarily equal.
Worst Case: (O(n²)), Occurs when the smallest or largest element is always chosen as the pivot (e.g., sorted arrays).

Auxiliary Space: O(n), due to recursive call stack
"""


def get_lomuto_partition(arr, low, high):
    pivot = arr[high] # taking last element as pivot element
    i = low - 1 # pointer one

    for j in range(low, high):
        if arr[j] < pivot:
           i += 1
           swap(arr, j, i)

    swap(arr, i + 1, high) # swap pivot to right place

    return i+ 1 # return correct pivot position


def swap(arr, j, i):
    arr[i], arr[j] = arr[j], arr[i]


def quick_sort(arr, low, high):
    if low < high: # list is larger than 1 element hence there is point in sorting

        # get Lomuto Partition. This will have the piviot element in right place
        # elements less than pivot element < pivot element > elements more than pivot element
        pivot_index = get_lomuto_partition(arr, low, high) # Put pivot element in right place
        quick_sort(arr, low, pivot_index - 1) # elements less than pivot element
        quick_sort(arr, pivot_index + 1, high) # elements more than pivot element


arr = [10, 7, 3, 9, 1, 5]
n = len(arr)
quick_sort(arr, 0 , n-1)
print(arr)
"""
Two pointer problem
https://www.youtube.com/watch?v=Vtckgz38QHsQuick Sort Idea
https://www.geeksforgeeks.org/quick-sort-algorithm/
Time Complexity:
Best Case: (Ω(n log n)), Occurs when the pivot element divides the array into two equal halves.
Average Case (θ(n log n)), On average, the pivot divides the array into two parts, but not necessarily equal.
Worst Case: (O(n²)), Occurs when the smallest or largest element is always chosen as the pivot (e.g., sorted arrays).

Auxiliary Space:
O(n), due to recursive call stack
"""

def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] < pivot: # compare each index asc with pivot value
            i += 1
            swap(arr, i, j)

    # adjust pivot to right position
    swap(arr, i + 1, high)
    return i + 1


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def quick_sort(arr, low, high):
    if low < high:
        part = partition(arr, low, high) # divide array in half based on right most element used as pivot

        quick_sort(arr, low, part - 1)
        quick_sort(arr, part + 1, high)


arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quick_sort(arr, 0 , n-1)
for val in arr:
    print(val, end=" ")
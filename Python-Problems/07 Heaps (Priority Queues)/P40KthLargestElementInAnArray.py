"""
This is Min-Heap (Priority Queue) problem
"""

"""
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Can you solve it without sorting?

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4


Constraints:
1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104
"""
"""
Use a min heap to keep track of the top k largest elements.
As you iterate:
    Add elements to the heap.
    If heap size > k, remove the smallest.
    After traversing all elements, the root of the heap is the kth largest.
"""
import heapq


def find_Kth_largest(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """

    # Use a min heap of size k
    min_heap = []

    for num in nums:
        heapq.heappush(min_heap, num)  # Add element
        if len(min_heap) > k:
            heapq.heappop(min_heap)  # Remove smallest if size exceeds k

    return min_heap[0]  # Root is the kth largest


nums = [3,2,1,5,6,4]
k = 2
print(find_Kth_largest(nums, k))

nums = [3,2,3,1,2,4,5,5,6]
k = 4
print(find_Kth_largest(nums, k))

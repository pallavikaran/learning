"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Constraints:
1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
"""


def merge(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: List[List[int]]
    """

    # sort all intervals
    intervals.sort(key=lambda x: x[0])  # Sort by first element in each row
    merged = []

    for interval in intervals:
        # check if incoming interval's left val is more than merged's right value
        if not merged or interval[0] > merged[-1][1]:  # right interval in intervals column = 1
            merged.append(interval)
        else:
            # interval[1] -> right value of interval
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge(intervals))

intervals = [[1, 4], [4, 5]]
print(merge(intervals))

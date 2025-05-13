"""
This is Floyd's Cycle Detection Algorithm (a.k.a. Tortoise and Hare)

Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.
Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
3 -> 2 -> 0 -> -4
     ↑<---------↓

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
1 -> 2
↑<---↓

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
1

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

Constraints:
The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.
"""

"""
Cycle Detection:
A cycle exists in a linked list if a node's next pointer points back to a previously visited node in the list.
If a node points to a node that was visited earlier, then that means the list loops, creating a cycle.
The pos:
    pos is an index that tells you which node the tail's next pointer connects to (forming a cycle).
    If pos is -1, then there is no cycle.
    If pos >= 0, then the last node's next pointer points to the node at that index, forming a cycle
"""

"""
In a cycle, the fast pointer moves faster, so if there's a loop, it must "lap" the slow pointer. Think of two runners on a circular track:
The fast runner takes 2 steps per second.
The slow runner takes 1 step per second.
Eventually, fast catches up, even if they started apart.
This is why they always meet inside the loop.

Example:
1 -> 2 -> 3 -> 4 -> 5
↑<------------------↓
head = [1, 2, 3, 4, 5]
pos = 0

Steps:

Initial:
slow = head → value = 1
fast = head → value = 1

🔁 Iteration 1:
slow = slow.next → value = 2
fast = fast.next.next → value = 3

🔁 Iteration 2:
slow = 3
fast = 5

🔁 Iteration 3:
slow = 4
fast = 2 (remember: 5 → 1 → 2)

🔁 Iteration 4:
slow = 5
fast = 4

🔁 Iteration 5:
slow = 1
fast = 1

✅ At this point: slow == fast, and the cycle is detected.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        else:
            slow_ptr = head  # moves by incrementing by 1 i.e. head.next
            fast_ptr = head  # moves by incrementing by 2 i.e. head.next.next
            while fast_ptr is not None and fast_ptr.next is not None: # Checking that fast_ptr has nodes to increment/check
                slow_ptr = slow_ptr.next
                fast_ptr = fast_ptr.next.next

                if slow_ptr == fast_ptr: # if the nodes of the linked list match that means cycle is detected
                    return True
        return False

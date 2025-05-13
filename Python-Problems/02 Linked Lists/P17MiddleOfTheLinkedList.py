"""
Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.

Example 1:
1 -> 2 -> 3 -> 4 -> 5
          =
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.


Example 2:
1-> 2 -> 3 -> 4 -> 5 -> 6
              =
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

Constraints:
The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100
"""

"""
Two Pointer Approach (Tortoise and Hare)
Use two pointers:
slow moves 1 step at a time.
fast moves 2 steps at a time.
When fast reaches the end, slow will be at the middle.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middle_noode(head):
    """
    :type head: Optional[ListNode]
    :rtype: Optional[ListNode]
    """

    if head is None:
        return
    else:
        slow_ptr = head
        fast_ptr = head

        while fast_ptr is not None and fast_ptr.next is not None:
            slow_ptr = slow_ptr.next  # moves by incrementing by 1 i.e. head.next
            fast_ptr = fast_ptr.next.next  # moves by incrementing by 2 i.e. head.next.next

        return slow_ptr


# Build: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
middle = middle_noode(head)
print(middle.val)

# Build: 1 -> 2 -> 3 -> 4 -> 5 -> 6
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)
head1.next.next.next.next = ListNode(5)
head1.next.next.next.next.next = ListNode(6)
middle1 = middle_noode(head1)
print(middle1.val)


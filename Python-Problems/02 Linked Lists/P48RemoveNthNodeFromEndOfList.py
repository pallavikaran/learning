"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

1 -> 2 -> 3 -> 4 -> 5
               *
1 -> 2 -> 3 ------> 5

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]

Constraints:
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
"""

"""
Two-Pointer (Optimal) Approach for "Nth from End"
Use a fast and slow pointer:
    Move fast pointer n steps ahead.
    Move both fast and slow one step at a time until fast.next is None.
    Now slow is at the node before the one to delete.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Print the updated list
def print_list(node):
    while node:
        print(node.val, end=" → ")
        node = node.next
    print("None")


def remove_Nth_from_end(head, n):
    """
    :type head: Optional[ListNode]
    :type n: int
    :rtype: Optional[ListNode]
    """
    dummy_node_obj = ListNode(0)  # Dummy node to start the list
    dummy_node_obj.next = head  # It is dangerous to assign dummy_node_obj to head coz we can delete head based on n value so the linked list will be messed up
    slow_ptr = fast_ptr = dummy_node_obj

    # Move fast pointer n+1 steps ahead
    for _ in range(0, n+1):
        fast_ptr = fast_ptr.next  # now fast_ptr is the node after the one we need to delete
        # This operation is for traversing the list.

    # Move both pointers until fast reaches the end
    while fast_ptr is not None:  # When fast_ptr reaches end (fast_ptr -> None) then slow_ptr will be at slow will be right before the node to delete
        fast_ptr = fast_ptr.next  # This operation is for traversing the list.
        slow_ptr = slow_ptr.next  # This operation is for traversing the list.

    # Remove the target node This operation is for modifying the list
    slow_ptr.next = slow_ptr.next.next  # slow_ptr is before to be deleted node, hence chasnging to the node next to the to be deleted node

    return dummy_node_obj.next


# Create list: 1 → 2 → 3 → 4 → 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
print_list(head)
# Call the function
new_head = remove_Nth_from_end(head, 2)
print_list(new_head)

# Create list: 1 → 2 → 3 → 4 → 5
head1 = ListNode(1)
# Call the function
print_list(head1)
new_head1 = remove_Nth_from_end(head1, 1)
print_list(new_head1)

# Create list: 1 → 2 → 3 → 4 → 5
head2 = ListNode(1)
head2.next = ListNode(2)
print_list(head2)
# Call the function
new_head2 = remove_Nth_from_end(head2, 1)
print_list(new_head2)

"""
Given the head of a singly linked list, reverse the list, and return the reversed list

Example 1:
1 -> 2-> 3 -> 4 -> 5
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
1 <- 2 <- 3 <- 4 <- 5

Example 2:
1 -> 2
Input: head = [1,2]
Output: [2,1]
2 -> 1

Example 3:
Input: head = []
Output: []

Constraints:
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")


def reverse_list(head):
    """
    :type head: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    if head is None:
        return head
    else:
        previous_node = None  # New head, start with None
        current_node = head

        while current_node is not None:
            next_node = current_node.next  # Store next - temp node holding current row's pointer
            current_node.next = previous_node  # Reverse pointer - Current needs to now point to previous
            previous_node = current_node  # Move prev forward - Now previous has become current
            current_node = next_node  #  Move curr forward - Now current node needs to be updated to next node

    return previous_node  # New head of the reversed list


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
print_list(head)
reversed_head = reverse_list(head)
print_list(reversed_head)

head1 = ListNode(1)
head1.next = ListNode(2)
print_list(head1)
reversed_head1 = reverse_list(head1)
print_list(reversed_head1)

head2 = ListNode()
print_list(head2)
reversed_head2 = reverse_list(head2)
print_list(reversed_head2)

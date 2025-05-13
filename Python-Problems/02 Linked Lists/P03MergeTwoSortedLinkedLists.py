"""
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:
1 -> 2 -> 4
1 -> 3 -> 4
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
1 -> 1 -> 2 -> 3 -> 4 -> 4

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""

"""
key -> list is sorted
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        # In a singly linked list, we need a way to access the starting point of the list — the first node. We assign in later in future methods
        self.head = None

    def insert_at_end(self, data):
        new_node = ListNode(val=data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head  # assign to the first element in linked list
            while current_node.next is not None:
                current_node = current_node.next  # incrementing pointer to assign to next node
            current_node.next = new_node  # Assign last element to the new node


def merge_two_lists(list1, list2):
    """
    :type list1: Optional[ListNode] That means it's expecting the head node of a linked list, not the LinkedList object itself
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    dummy_node_obj = ListNode(0)  # Dummy node to start the list
    current_node = dummy_node_obj

    while list1 and list2:
        if list1.val <= list2.val:
            current_node.next = list1
            list1 = list1.next
        else:
            current_node.next = list2
            list2 = list2.next
        current_node = current_node.next  # Move current forward (When building or traversing a list, you move a pointer (like current) to the next node to avoid updating the same node)

    if list1 is not None:
        current_node.next = list1
    if list2 is not None:
        current_node.next = list2

    # Return the merged list, skipping the dummy node
    return dummy_node_obj.next


def print_linked_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")


list1 = LinkedList()
list1.insert_at_end(1)
list1.insert_at_end(2)
list1.insert_at_end(4)
list2 = LinkedList()
list2.insert_at_end(1)
list2.insert_at_end(3)
list2.insert_at_end(4)
result12 = merge_two_lists(list1.head, list2.head)  # That means it's expecting the head node of a linked list, not the LinkedList object itself
print_linked_list(result12)

list3 = LinkedList()
list4 = LinkedList()
print_linked_list(merge_two_lists(list3.head, list4.head))

list5 = LinkedList()
list6 = LinkedList()
list6.insert_at_end(0)
print_linked_list(merge_two_lists(list5.head, list6.head))

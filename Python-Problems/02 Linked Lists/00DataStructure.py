"""
A node is a basic unit of a linked list. Each node typically contains:
Some data
A reference (or pointer) to the next node in the list

Data
This is the value or information that the node stores. For example, it could be a number, string, or even an object.

node.next
This refers to the link to the next node in the list. It's how nodes are connected in a sequence. If a node is the last one in the list, node.next is usually null or None (depending on the programming language), meaning there is no next node.

Analogy: Think of it like train cars
Each train car is a Node.
Each coupler connecting to the next car is the .next pointer.
When you say node, you're talking about the whole car.
When you say node.next, you're talking about the connection to the next car.
"""

"""
__init__: Initializes the linked list with an empty head.
insertAtBegin(): Inserts a node at the beginning of the linked list.
insertAtIndex(): Inserts a node at the given index of the linked list.
insertAtEnd(): Inserts a node at the end of the linked list.
remove_node(): Deletes a node by taking data as an argument. It traverses the linked list and deletes the node if a match is found.
sizeOfLL(): Returns the current size of the linked list.
printLL(): Traverses the linked list and prints the data of each node. printLL() method ensures the last node is printed by adding a print(current_node.data) after the loop ends. This handles the edge case of printing the last node.
"""


# Create a Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


node = Node(10)
print(node)
print(node.data)
print(node.next)


class LinkedList:
    def __init__(self):
        # In a singly linked list, we need a way to access the starting point of the list — the first node. We assign in later in future methods
        self.head = None

    # Print the linked list
    def print_linked_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def get_size_of_linked_list(self):
        size = 0
        current_node = self.head
        while current_node is not None:
            size += 1
            current_node = current_node.next
        return size

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head  # assign to the first element in linked list
            while current_node.next is not None:
                current_node = current_node.next  # incrementing pointer to assign to next node
            current_node.next = new_node  # Assign last element to the new node

    def insert_at_start(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head  # Point new node to head node
            self.head = new_node  # Head Node becomes new node

    def insert_at_index(self, data, index):
        new_node = Node(data)
        if index == 0:
            self.insert_at_start(data)
        else:
            current_node = self.head
            position = 0  # starting index
            while (current_node is not None and position + 1 != index):   # Need tp iterate to the node before the actual index so can use .next pointer to point to new node
                position += 1  # incrementing position index
                current_node = current_node.next  # incrementing the node

            if current_node is not None:  # checking if current data node is present and that the linked list has not ended
                # the node before the index node needs to be pointed to current node
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                print(f"index {index} not found")

    def update_node(self, val, index):
        if index == 0:
            self.head.data = val
        else:
            current_node = self.head
            position = 0
            while current_node is not None and position != index:
                position += 1
                current_node = current_node.next

            if current_node is not None:
                current_node.data = val
            else:
                print(f"index {index} not found")

    def remove_first_node(self):
        if self.head is not None:
            self.head = self.head.next
        else:
            print(f"Linked List is empty")

    def remove_last_node(self):
        if self.head is None:
            return
        elif self.head.next is None:
            self.head = None
        else:
            current_node = self.head
            while current_node.next is not None and current_node.next.next is not None: # Traverse to second last node
                current_node = current_node.next

            current_node.next = None

    def remove_at_index(self, index):
        if self.head is None:
            return
        elif index == 0:
            self.remove_first_node()
        else:
            current_node = self.head
            position = 0
            # current node exists, a node after current node exists so that post deletion the prev node will point to the deleted node's next
            while current_node is not None and current_node.next is not None and position + 1 != index: # Traverse just before reaching the index to delete the index
                position += 1
                current_node = current_node.next

            if current_node is not None and current_node.next is not None: # Check if valid node and the next node exists to point after deletion
                current_node.next = current_node.next.next
            else:
                print(f"index {index} not found")

    def remove_node_based_on_data(self, data):
        current_node = self.head
        if current_node is not None and current_node.data == data:
            self.remove_first_node()
        else:
            while current_node is not None and current_node.next is not None: # need to reach an index before node that matches with data
                if current_node.next.data == data:
                    current_node.next = current_node.next.next  # Node before matching node points to the next(data match) node's pointer
                    return
                current_node = current_node.next

            print("Node with the given data not found")


#  create a new linked list. One object is created in this named llist and all the operations are performed in this object
llist = LinkedList()
llist.print_linked_list()

# add nodes to the linked list
llist.insert_at_end('a')
llist.insert_at_end('b')
print("Node Data insert_at_end:")
llist.print_linked_list()

llist.insert_at_start('c')
print("Node Data insert_at_start:")
llist.print_linked_list()

llist.insert_at_end('d')

llist.insert_at_index('g', 2)
llist.insert_at_index('t', 9)
print("Node Data insert_at_index:")
llist.print_linked_list()

print("\nGet size of Linked List")
print(llist.get_size_of_linked_list())

print("\nUpdate node Value at Index : 1")
llist.update_node('ff', 2)
llist.print_linked_list()

print("\nRemove First Node:")
llist.remove_first_node()
llist.print_linked_list()

print("\nRemove Last Node:")
llist.remove_last_node()
llist.print_linked_list()

print("\nRemove Node at Index : 1")
llist.remove_at_index(1)
llist.print_linked_list()

print("\nRemove Node with data: b")
llist.remove_node_based_on_data('b')
llist.print_linked_list()


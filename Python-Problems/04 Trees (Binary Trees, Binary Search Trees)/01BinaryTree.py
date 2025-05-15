"""
Binary Tree is a non-linear and hierarchical data structure where each node has at most two children referred to as the left child and the right child.
The topmost node in a binary tree is called the root, and the bottom-most nodes are called leaves.

IT ALWAYS HAS TWO CHILDREN.

Representation of Binary Tree
Each node in a Binary Tree has three parts:
    Data
    Pointer to the left child
    Pointer to the right child

                ROOT NODE
             _______________
            |      DATA     |
            |---------------|
            | LEFT  | RIGHT |
            |_______|_______|
                /       \
               /         \
 _____________/_       ___\___________
|      DATA     |     |     DATA      |
|---------------|     |---------------|
| LEFT  | RIGHT |     | LEFT  | RIGHT |
|_______|_______|     |_______|_______|
    LEFT CHILD          RIGHT CHILD
     /   \                  /  \
    /     \                /    \
  Null    Null           Null   Null

Terminologies in Binary Tree
    Nodes: The fundamental part of a binary tree, where each node contains data and link to two child nodes.
    Root: The topmost node in a tree is known as the root node. It has no parent and serves as the starting point for all nodes in the tree.
    Parent Node: A node that has one or more child nodes. In a binary tree, each node can have at most two children.
    Child Node: A node that is a descendant of another node (its parent).
    Leaf Node: A node that does not have any children or both children are null.
    Internal Node: A node that has at least one child. This includes all nodes except the leaf nodes.
    Depth of a Node: The number of edges from a specific node to the root node. The depth of the root node is zero.
    Height of a Binary Tree: The number of nodes from the deepest leaf node to the root node.
"""

"""
            2 <- Root
          /    \
         /      \
        3        4
      /   \     /  \
     5  Null   Null Null
    / \ 
  Null Null 
"""


class Node:
    def __init__(self, data, left=None, right=None):
        self. left = left
        self.right = right
        self.val = data


def print_tree(node, prefix="", is_left=True):
    if node.right:
        print_tree(node.right, prefix + ("│   " if is_left else "    "), False)
    print(prefix + ("└── " if is_left else "┌── ") + str(node.val))
    if node.left:
        print_tree(node.left, prefix + ("    " if is_left else "│   "), True)


print("********************* create and print binary search tree  *********************")
# Initialize and allocate memory for tree nodes
first_node_obj = Node(2)  # Root
second_node_obj = Node(3)
third_node_obj = Node(5)
fourth_node_obj = Node(4)

# Connect binary tree nodes
first_node_obj.left = second_node_obj
first_node_obj.right = fourth_node_obj
second_node_obj.left = third_node_obj

print_tree(first_node_obj)

"""
A binary tree traversal means visiting each node in the tree in a particular order.
Depth-First Search (DFS) algorithms: DFS explores as far down a branch as possible before backtracking. 
It is implemented using recursion. The main traversal methods in DFS for binary trees are:
There are 3 main depth-first traversals:
    |--------------------------------|
    |Traversal	|    Visit Order     |
    |--------------------------------|
    |In-order	|Left → Root → Right | 
    |Pre-order	|Root → Left → Right |
    |Post-order	|Left → Right → Root |
    |--------------------------------|
    
Breadth-First Search (BFS) algorithms: BFS explores all nodes at the present depth before moving on to nodes at the next depth level. 
It is typically implemented using a queue. BFS in a binary tree is commonly referred to as Level Order Traversal


Example:
        1
       / \
      2   3
     / \
    4   5   
Where-ever the root/center needs to come in the order just print(root.val, end=' ')
"""

"""
In-order Traversal (Left → Root → Right)
    Visit left subtree
    Visit the current node
    Visit right subtree
In a binary search tree (BST), in-order gives nodes in SORTED ORDER.
"""


def in_order_traversal_dfs(root):
    if root is not None:
        in_order_traversal_dfs(root.left)
        print(root.val, end=' ')
        in_order_traversal_dfs(root.right)


print("********************* in_order_traversal_dfs *********************")
root = Node(1,
        Node(2, Node(4),Node(5)),
        Node(3))
print_tree(root)
in_order_traversal_dfs(root)

"""
Pre-order Traversal (Root → Left → Right)
    Visit the current node
    Visit left subtree
    Visit right subtree
Used to copy a tree. Helpful in prefix expression notation (like in compilers)
"""


def pre_order_traversal_dfs(root):
    if root is not None:
        print(root.val, end=' ')
        pre_order_traversal_dfs(root.left)
        pre_order_traversal_dfs(root.right)


print("********************* pre_order_traversal_dfs *********************")
print_tree(root)
pre_order_traversal_dfs(root)


"""
Post-order Traversal (Left → Right → Root)
    Visit left subtree
    Visit right subtree
    Visit the current node
Used to delete or free memory in trees. Useful for expression tree evaluation (e.g., calculators)
"""


def post_order_traversal_dfs(root):
    if root is not None:
        post_order_traversal_dfs(root.left)
        post_order_traversal_dfs(root.right)
        print(root.val, end=' ')


print("********************* post_order_traversal_dfs *********************")
print_tree(root)
post_order_traversal_dfs(root)

"""
Level Order Traversal
1. Start by putting the root node in the queue.
2. While the queue is not empty:
    a. Remove the front node.
    b. Process it (e.g., print it).
    c. Add its left and right children to the queue (if they exist).
"""

from collections import deque


def level_order_bfs(root):
    if root is not None:
        queue = deque([root])  # start with the root node in the queue. The queue helps to track which node to visit next
        while queue:
            curr_node = queue.popleft()  # Remove and get the leftmost node in the queue (FIFO order)
            print(curr_node.val, end=' ')
            if curr_node.left:
                queue.append(curr_node.left)  # If there's a left child, add it to the queue to visit later.

            if curr_node.right:
                queue.append(curr_node.right)  # If there's a right child, add it to the queue to visit later.


print("********************* level_order_bfs *********************")
print_tree(root)
level_order_bfs(root)

"""
Insertion in Binary Tree
"""


def insert_in_binary_tree(root, data):
    new_node = Node(data)

    if root is None:
        return new_node

    queue = deque([root])  # This creates a python dqueue and initially puts the root node of the binary tree inside the queue

    while queue:
        curr_node = queue.popleft()  #  It removes and returns the first (leftmost) element from the queue

        if curr_node.left is None:
            curr_node.left = new_node
            return root
        else:
            queue.append(curr_node.left)  # If there's a left child, add it to the queue to visit later.

        if curr_node.right is None:
            curr_node.right = new_node
            return root
        else:
            queue.append(curr_node.right)  # If there's a right child, add it to the queue to visit later.

    return root


print("********************* insert_in_binary_tree *********************")
print_tree(root)
insert_in_binary_tree(root, 6)
insert_in_binary_tree(root, 7)
insert_in_binary_tree(root, 8)
print_tree(root)

"""
Searching in Binary Tree
"""


def search_in_binary_tree(root, target):
    if root is not None:
        queue = deque([root])  # This creates a python dqueue and initially puts the root node of the binary tree inside the queue

        while queue:
            curr_node = queue.popleft()  #  It removes and returns the first (leftmost) element from the queue

            if curr_node.val == target:
                return True

            if curr_node.left is not None:
                queue.append(curr_node.left)  # If there's a left child, add it to the queue to visit later.

            if curr_node.right is not None:
                queue.append(curr_node.right)  # If there's a right child, add it to the queue to visit later.

        return False   # After entire tree is searched and not found
    else:
        return False   # In case root is None


print("********************* search_in_binary_tree *********************")
print_tree(root)
print(search_in_binary_tree(root,1))
print(search_in_binary_tree(root, 4))
print(search_in_binary_tree(root, 9))

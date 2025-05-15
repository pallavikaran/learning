"""
Binary Tree is a non-linear and hierarchical data structure where each node has at most two children referred to as the left child and the right child.
The topmost node in a binary tree is called the root, and the bottom-most nodes are called leaves.

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
There are 3 main depth-first traversals:
    |--------------------------------|
    |Traversal	|    Visit Order     |
    |--------------------------------|
    |In-order	|Left → Root → Right | 
    |Pre-order	|Root → Left → Right |
    |Post-order	|Left → Right → Root |
    |--------------------------------|
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


def in_order_traversal(root):
    if root is not None:
        in_order_traversal(root.left)
        print(root.val, end=' ')
        in_order_traversal(root.right)


root = Node(1,
        Node(2, Node(4),Node(5)),
        Node(3))
print(print_tree(root))
print(in_order_traversal(root))

"""
Pre-order Traversal (Root → Left → Right)
    Visit the current node
    Visit left subtree
    Visit right subtree
Used to copy a tree. Helpful in prefix expression notation (like in compilers)
"""


def pre_order_traversal(root):
    if root is not None:
        print(root.val, end=' ')
        pre_order_traversal(root.left)
        pre_order_traversal(root.right)


print(print_tree(root))
print(pre_order_traversal(root))

"""
Post-order Traversal (Left → Right → Root)
    Visit left subtree
    Visit right subtree
    Visit the current node
Used to delete or free memory in trees. Useful for expression tree evaluation (e.g., calculators)
"""


def post_order_traversal(root):
    if root is not None:
        post_order_traversal(root.left)
        post_order_traversal(root.right)
        print(root.val, end=' ')


print(print_tree(root))
print(post_order_traversal(root))



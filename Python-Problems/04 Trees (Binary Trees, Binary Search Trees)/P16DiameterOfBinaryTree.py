"""
Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.

Example 1:
          1
         / \
        2   3
      /  \
     4   5
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:
Input: root = [1,2]
Output: 1

Constraints:
The number of nodes in the tree is in the range [1, 104].
-100 <= Node.val <= 100
"""

"""
For each node: The longest path that passes through it is: left_depth + right_depth
The maximum of all such paths in the tree is the diameter.
We do a post-order DFS: Left → Right → Root 
At each node, calculate:
    Depth of left subtree
    Depth of right subtree
    Update the global diameter with left + right if it's larger
"""

"""
Python doesn't let you assign to a variable from an outer scope unless it's declared nonlocal (for inner functions) or global.
❌ This won’t work:
diameter = 0
def dfs(node):
    diameter = max(diameter, left + right)  # WRONG — rebinds a new local `diameter`
    
✅ This works:
diameter = [0]
def dfs(node):
    diameter[0] = max(diameter[0], left + right)  # Modifies the shared list
"""
from collections import deque


# Definition for a binary tree node.
class Node(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values):  # This builds a tree having all children both in left & right
    if not values:
        return None
    root = Node(values[0])  # root node
    queue = deque([root])   # initialize queue with root node
    index = 1  # since root is already at index 0
    while queue and index < len(values):
        node = queue.popleft()  # prev value will act as parent to populate left and right children
        if index < len(values) and values[index] is not None:  # populate left child
            node.left = Node(values[index])
            queue.append(node.left)
        index += 1
        if index < len(values) and values[index] is not None:  # populate right child
            node.right = Node(values[index])
            queue.append(node.right)
        index += 1
    return root


def diameter_of_binary_tree(root):
    """
    :type root: Optional[TreeNode]
    :rtype: int
    """
    diameter = [0]  # Use list to store diameter so it can be updated inside nested function

    def post_order_traversal_dfs(node):
        if not node:
            return 0

        left_length = post_order_traversal_dfs(node.left)
        right_length = post_order_traversal_dfs(node.right)
        diameter[0] = max(diameter[0], left_length + right_length)  # Update max diameter seen so far
        return 1 + max(left_length, right_length)  # Return height of this subtree to its parent

    post_order_traversal_dfs(root)
    return diameter[0]


tree = build_tree([1, 2, 3, 4, 5])
print(diameter_of_binary_tree(tree))

tree = build_tree([1,2])
print(diameter_of_binary_tree(tree))

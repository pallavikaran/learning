"""
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
Example 1:
        3
       / \
      9  20
        /  \
       15  7

Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2

Constraints:
The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
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


def max_depth(root):
    """
    :type root: Optional[TreeNode]
    :rtype: int
    """
    if not root:
        return 0
    else:
        # Recursively find the depth of the left & right subtree & get the max
        return 1 + max(max_depth(root.left), max_depth(root.right))  # Add 1 to account for the current root node itself


tree = build_tree([3,9,20,None,None,15,7])
print(max_depth(tree))

tree = build_tree([1,None,2])
print(max_depth(tree))

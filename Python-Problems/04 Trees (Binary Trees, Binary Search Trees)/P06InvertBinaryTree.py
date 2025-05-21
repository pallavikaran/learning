"""
Given the root of a binary tree, invert the tree, and return its root.
Example 1:
            4                   4
          /  \                 /  \
        2     7    =>         7    2
      / \    / \            / \   / \
     1  3   6  9           9  6  3   1

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:
Input: root = [2,1,3]
Output: [2,3,1]

Example 3:
Input: root = []
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 100].
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


def pre_order_traversal_dfs(root):
    if root is not None:
        print(root.val, end=' ')
        pre_order_traversal_dfs(root.left)
        pre_order_traversal_dfs(root.right)


def invert_binary_tree(root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    if root is None:
        return
    else:
        # invert left right
        temp = root.left
        root.left = root.right
        root.right = temp
        # recursive invert left & right
        invert_binary_tree(root.left)
        invert_binary_tree(root.right)

    return root


tree = build_tree([4,2,7,1,3,6,9])
inverted = invert_binary_tree(tree)
print(pre_order_traversal_dfs(inverted))

tree = build_tree([2,1,3])
inverted = invert_binary_tree(tree)
print(pre_order_traversal_dfs(inverted))

tree = build_tree([])
inverted = invert_binary_tree(tree)
print(pre_order_traversal_dfs(inverted))

"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:
Input: root = [2,1,3]
Output: true
       2
      / \
     1  3


Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
       5
      / \
     1  4
       / \
      3   6


Constraints:
The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_valid_BST(root):
    """
    :type root: Optional[TreeNode]
    :rtype: bool
    """

    def compare(node, min_value, max_value):
        if not node:
            return True

        if not (min_value < node.val < max_value):
            return False

        # At this node, compare left child's value and right child's value of the node
        return (compare(node.left, min_value, node.val)  # for a valid tree, left child value < node.value
                and compare(node.right, node.val, max_value))  # for a valid tree, right child value > node.value

    return compare(root, float('-inf'), float('inf'))  # Start with the whole range of possible values (-inf to +inf).


root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
print(is_valid_BST(root))

root1 = TreeNode(5)
root1.left = TreeNode(1)
root1.right = TreeNode(4)
root1.right.left = TreeNode(3)
root1.right.right = TreeNode(6)
print(is_valid_BST(root1))

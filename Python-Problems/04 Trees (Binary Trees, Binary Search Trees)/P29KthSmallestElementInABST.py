"""
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Example 1:
Input: root = [3,1,4,null,2], k = 1
Output: 1
    3
   / \
  1  4
   \
    2

Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
          5
         / \
        3  6
       / \
      2  4
     /
    1

Constraints:
The number of nodes in the tree is n.
1 <= k <= n <= 104
0 <= Node.val <= 104
"""
"""
Inorder Traversal (Left → Node → Right)
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kth_smallest(root, k):
    """
    :type root: Optional[TreeNode]
    :type k: int
    :rtype: int
    """
    if not root:
        return None

    current = root
    elements_stack = []

    # Inorder Traversal (Left → Node → Right)
    while True:
        # Go to the leftmost node
        while current:  # Since it is BST, the left most elements will be the smallest so build a stack to add those values
            elements_stack.append(current)
            current = current.left
        current = elements_stack.pop()  # Running latest smallest value
        k -= 1. # decrement k so you get to k=0
        # If k is 0, we've found the kth smallest
        if k == 0:
            return current.val

        # Go to the right subtree and add subsequent children's left most values to elements_stack above
        current = current.right


k = 1
root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.right = TreeNode(2)
print(kth_smallest(root, k))

k = 3
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.left.left = TreeNode(1)
print(kth_smallest(root, k))

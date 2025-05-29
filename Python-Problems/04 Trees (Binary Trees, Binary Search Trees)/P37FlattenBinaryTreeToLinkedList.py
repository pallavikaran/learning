"""
Given the root of a binary tree, flatten the tree into a "linked list":
The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.

Example 1:
Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
                    1
        1            \
       / \            2
      2   5     =>    \
     /\    \          3
    3  4   6           \
                       4
                        \
                        5
                         \
                          6
Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [0]
Output: [0]

Constraints:
The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
Follow up: Can you flatten the tree in-place (with O(1) extra space)?
"""
"""
Approach: Reverse Postorder (Right → Left → Root)
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def print_linked_list(current):
    while current:
        print(current.val, end=" -> ")
        current = current.right
    print(" ")


def flatten(root):
    """
    :type root: Optional[TreeNode]
    :rtype: None Do not return anything, modify root in-place instead.
    """

    prev = [None]  # keeps track of the previous node visited during recursion

    def dfs(node):
        if not node:
            return

        # This is the reverse of preorder traversal (root → left → right) → now doing right → left → root
        dfs(node.right)  # Visit the right subtree first.
        dfs(node.left)  # Visit the left subtree first.

        # Flatten logic
        node.right = prev[0]  # The current node's right pointer is set to the previous node we visited (self.prev), so we chain it into a right-skewed list.
        node.left = None  # We remove the left child, since the final structure must only use .right like a linked list.
        prev[0] = node  # update the previous node

    dfs(root)
    # Do not return anything, modify root in-place instead.


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.right = TreeNode(6)
flatten(root)
print_linked_list(root)


root1 = None
flatten(root1)
print_linked_list(root1)


root2 = TreeNode(0)
flatten(root2)
print_linked_list(root2)


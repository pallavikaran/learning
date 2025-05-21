"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
Example 1:  |
            1
          / |  \
        2   |   2
      /  \  | /  \
    3    4  | 4   3
Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:
        1
       / \
      2  2
      \   \
      3   3

Input: root = [1,2,2,null,3,null,3]
Output: false

Constraints:
The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100
"""


class Node:
    def __init__(self, data, left=None, right=None):
        self. left = left
        self.right = right
        self.val = data


def is_symmetric(root):
    """
    :type root: Optional[TreeNode]
    :rtype: bool
    """
    if not root:
        return True  # no tree so True

    def is_mirror(t1, t2):
        if not t1 and not t2:
            return True  # both left and right are None or null hence mirror/same

        if not t1 or not t2:  # either t1 or t2 is null hence unbalanced, both is already checked above so either is unbalanced
            return False

        return (
                t1.val == t2.val  # Current node values must match
                and is_mirror(t1.left, t2.right)  # Left subtree of t1 vs right subtree of t2
                and is_mirror(t1.right, t2.left)  # Right subtree of t1 vs left subtree of t2
        )

    return is_mirror(root.left, root.right)


# root = [1,2,2,3,4,4,3]
tree = Node(1)
tree.left = Node(2, Node(3), Node(4))
tree.right = Node(2, Node(4), Node(3))
print(is_symmetric(tree))

# root = [1,2,2,null,3,null,3]
tree1 = Node(1)
tree1.left = Node(2, None, Node(4))
tree1.right = Node(2, None, Node(3))
print(is_symmetric(tree1))

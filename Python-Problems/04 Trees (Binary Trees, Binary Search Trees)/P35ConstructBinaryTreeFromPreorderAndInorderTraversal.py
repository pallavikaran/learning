"""
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

Example 1:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: preorder = [-1], inorder = [-1]
Output: [-1]

Constraints:
1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.
"""
"""
Preorder traversal visits nodes in the order:
Root → Left → Right

Inorder traversal visits nodes in the order:
Left → Root → Right

So, in preorder: The first value is always the root of the (sub)tree.

Using that root: Find its index in the inorder list. All elements to the left of that index are in the left subtree, and to the right are in the right subtree.
"""
from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Convert tree to list (level order)
def tree_to_list(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Remove trailing Nones
    while result and result[-1] is None:
        result.pop()
    return result


def build_tree(preorder, inorder):
    """
    :type preorder: List[int]
    :type inorder: List[int]
    :rtype: Optional[TreeNode]
    """
    if not preorder or not inorder:
        return []

    # Create a value-to-index map for inorder traversal
    inorder_index_map = {}
    for i, val in enumerate(inorder):
        inorder_index_map[val] = i

    # Pointer to keep track of root index in preorder
    pre_order_index = [0]

    def build(left, right):
        if left > right:
            return None

        # Get the current root value and increment preorder index
        root_val = preorder[pre_order_index[0]]
        pre_order_index[0] += 1

        # Create tree with the root node
        root = TreeNode(root_val)

        # Build left and right subtrees using inorder boundaries
        root.left = build(left, inorder_index_map[root_val] - 1)
        root.right = build(inorder_index_map[root_val] + 1, right)

        return root

    return build(0, len(inorder) - 1)


preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
root = build_tree(preorder, inorder)
print(tree_to_list(root))

preorder = [-1]
inorder = [-1]
root = build_tree(preorder, inorder)
print(tree_to_list(root))

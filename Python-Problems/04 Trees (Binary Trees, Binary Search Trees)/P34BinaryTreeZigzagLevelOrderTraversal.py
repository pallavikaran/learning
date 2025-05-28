"""
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

    3
   / \
  9  20
    / \
   15 7

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
"""

"""
Breadth-First Search (BFS) - Level order Traversal
"""
from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def zigzag_level_order(root):
    """
    :type root: Optional[TreeNode]
    :rtype: List[List[int]]
    """
    if not root:
        return []

    result = []   # This will hold the final zigzag level order traversal
    queue = deque([root])  # Initialize queue with the root node
    left_to_right = True  # Flag to control zigzag direction

    while queue:
        level_size = len(queue) # Number of nodes at the current level
        level_nodes = deque()  # Temporary deque to store values at this level

        for _ in range(0, level_size):  # Loop over all nodes at this level
            node = queue.popleft()  # FIFO Removal, Remove node from the front of the queue

            # Append node value in appropriate direction
            if left_to_right:
                level_nodes.append(node.val)  # Left to right, add value to the right
            else:
                level_nodes.appendleft(node.val)  # Right to left for zig zag pattern, add value to the left

            # Add children to the queue for next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # After all children are processed add to result
        result.append(list(level_nodes))  # Add current level's values to result
        left_to_right = not left_to_right  # Toggle direction for next level

    return result  # Return the final zigzag level order list


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(7)
root.right.right = TreeNode(15)
print(zigzag_level_order(root))

root = TreeNode(1)
print(zigzag_level_order(root))

root = None
print(zigzag_level_order(root))

"""
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.
Example 1:
                    0
                   / \
                -3    9
                /    /
              -10   5


                 0
                / \
             -10   5
              \    \
              -3   9

Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:
Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.

Constraints:
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in a strictly increasing order.
"""
"""
ASCENDING ORDER OF ARRAY
NEED TO CREATE HEIGHT BALANCED TREE hence easy to get mid value via len(nums) // 2
"""


# Definition for a binary tree node.
class Node(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def in_order_traversal_dfs(root):  # Left → Node → Right
    if root is not None:
        in_order_traversal_dfs(root.left)
        print(root.val, end=' ')
        in_order_traversal_dfs(root.right)


def sorted_array_to_BST(nums):
    """
    :type nums: List[int]
    :rtype: Optional[TreeNode]
    """
    if not nums:
        return None
    else:
        middle_element = len(nums) // 2
        root = Node(nums[middle_element])

        # attach children to the root node
        root.left = sorted_array_to_BST(nums[:middle_element])  # Create the current root node using left half
        root.right = sorted_array_to_BST(nums[middle_element + 1:])  # Create the current root node using right half

    return root


nums = [-10, -3, 0, 5, 9]
tree = sorted_array_to_BST(nums)
print(in_order_traversal_dfs(tree))

nums = [1,3]
tree = sorted_array_to_BST(nums)
print(in_order_traversal_dfs(tree))

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def isBalwithHeight(root):
            if not root:
                return [0,True]
            left = isBalwithHeight(root.left)
            right = isBalwithHeight(root.right)
            return [max(left[0], right[0]) + 1, left[1] and right[1] and abs(left[0]-right[0]) <= 1]
        return isBalwithHeight(root)[1]
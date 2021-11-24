# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        gap=float('inf')
        closest=float('inf')
        while root:
            if abs(root.val - target) < gap:
                gap=abs(root.val - target)
                closest=root.val
            if target == root.val:
                break
            elif target < root.val:
                root=root.left
            else:
                root=root.right
        return closest
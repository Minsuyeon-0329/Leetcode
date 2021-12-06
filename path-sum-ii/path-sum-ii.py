# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        path=[]
        def findpath(root,targetSum,curr):
            if not root:
                return 
            curr.append(root.val)
            if root.val == targetSum and root.left == None and root.right==None:
                path.append(curr)
                return
            findpath(root.left,targetSum-root.val,curr[:])
            findpath(root.right,targetSum-root.val,curr[:])
        findpath(root,targetSum,[])
        return path
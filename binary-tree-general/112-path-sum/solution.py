# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.hasPathSumHelper(root, targetSum, 0)
    

    def hasPathSumHelper(self, root, targetSum, accum):
        if root is None:
            return False
        
        accum+=root.val

        if root.left is None and root.right is None:
            return targetSum == accum
        else:
            return self.hasPathSumHelper(root.left,targetSum, accum) or self.hasPathSumHelper(root.right, targetSum, accum)

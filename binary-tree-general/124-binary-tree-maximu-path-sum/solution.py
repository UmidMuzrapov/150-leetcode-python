# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    currentMax = -10**5

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxHelper(root)
        return self.currentMax
        

    def maxHelper(self, root):
        if root is None:
            return 0

        lmax = self.maxHelper(root.left)
        rmax = self.maxHelper(root.right)

        singlemax = max(max(lmax, rmax) + root.val, root.val)
        topmax = max(singlemax, lmax+rmax+root.val)
        self.currentMax = max(self.currentMax, topmax)

        return singlemax


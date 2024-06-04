# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.sumNumberHelper(root, '')

    def sumNumberHelper(self, root, s):
        if root is None:
            return 0
        
        s = s + str(root.val)
        if root.left is None and root.right is None:
            return int(s)

        left = self.sumNumberHelper(root.left, s)
        right = self.sumNumberHelper(root.right, s)

        return left + right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None

        head = None
        cur = None

        for p in self.preorder(root):
            if head is None:
                head = TreeNode(p.val)
                cur = head
            else:
                cur.right = TreeNode(p.val)
                cur.left = None
                cur = cur.right
        
        root.left = None
        root.val = head.val
        root.right = head.right


    def preorder(self, root):
        if root is not None:
            yield root

            yield from self.preorder(root.left)
            yield from self.preorder(root.right)
        

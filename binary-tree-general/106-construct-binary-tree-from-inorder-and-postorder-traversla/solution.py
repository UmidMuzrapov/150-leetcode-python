# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    post_i=0
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        my_dict = {num:i for i, num in enumerate(inorder)}
        self.post_i = len(postorder) - 1
        return self.buildTreeHelper(inorder, postorder, my_dict, 0, len(inorder) -1 )
        
    def buildTreeHelper(self, inorder, postorder, my_dict, instart, inend):
        if instart > inend:
            return None
        
        node = TreeNode(postorder[self.post_i])
        self.post_i -= 1

        if instart == inend:
            return node

        in_i = my_dict[node.val]
        node.right = self.buildTreeHelper(inorder, postorder, my_dict, in_i + 1, inend)
        node.left = self.buildTreeHelper(inorder, postorder, my_dict, instart, in_i-1)

        return node
        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    preindex = 0

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        my_dict = {num:i for i, num in enumerate(inorder)}
        return self.buildTreeHelper(preorder, inorder, my_dict, 0, len(inorder) - 1)
    
    def buildTreeHelper(self, preorder, inorder, my_dict, instart, inend):
        if instart > inend:
            return None
        
        node = TreeNode(preorder[self.preindex])
        self.preindex+=1

        if instart == inend:
            return node

        in_index = my_dict[node.val]
        node.left = self.buildTreeHelper(preorder, inorder, my_dict, instart, in_index-1)
        node.right =  self.buildTreeHelper(preorder, inorder, my_dict, in_index + 1, inend)
        return node



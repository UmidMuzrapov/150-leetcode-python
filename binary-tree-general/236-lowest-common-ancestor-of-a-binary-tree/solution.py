# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_path = []
        q_path = []
        self.helper(root, p, p_path)
        self.helper(root, q, q_path)
        min_len = min(len(p_path), len(q_path))

        for i in range(min_len):
            if p_path[i] != q_path[i]:
                return p_path[i-1]
        
        return p_path[min_len-1]

    def helper(self, root, p, path):
        if root is None:
            return 
        
        path.append(root)
        if root.val == p.val:
            return 
        
        self.helper(root.left, p, path)
        if path[-1].val == p.val:
            return 

        self.helper(root.right, p, path)
        if path[-1].val == p.val:
            return 
            
        path.pop()
    


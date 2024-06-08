# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = [root]
        left = True
        
        while queue:
            size = len(queue)
            temp = []
            level = []

            for i in range(size):
                if left:
                    level.append(queue[i].val)
                else:
                    level.append(queue[size-1-i].val)
                
                elem = queue[i]
                if elem.left:
                    temp.append(elem.left)
                if elem.right:
                    temp.append(elem.right)
                
            queue = temp
            left = not left
            result.append(level)

        return result
                    
                    



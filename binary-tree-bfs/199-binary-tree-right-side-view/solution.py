# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = []
        queue.append(root)
        result = []

        while queue:
            size = len(queue)
            result.append(queue[-1].val)
            temp = []

            for i in range(size):
                elem = queue[i]
                if elem.left:
                    temp.append(elem.left)
                if elem.right:
                    temp.append(elem.right)
            
            queue = temp
        
        return result

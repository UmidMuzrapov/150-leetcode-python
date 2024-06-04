# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    queue = []

    def __init__(self, root: Optional[TreeNode]):
        self.iterable = self.iter(root)

    def next(self) -> int:
        if len(self.queue) > 0:
            return self.queue.pop(0)

        return next(self.iterable, None)

    def hasNext(self) -> bool:
        val = self.next()
        if val is None:
            return len(self.queue) > 0
        else:
            self.queue.append(val)
            return True
        
    def iter(self, root):
        if root is not None:
            yield from self.iter(root.left)
            yield root.val 
            yield from self.iter(root.right)

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

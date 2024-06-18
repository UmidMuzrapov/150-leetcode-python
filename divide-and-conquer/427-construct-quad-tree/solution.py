
class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        return self.helper(0, 0, n, n, grid)

    def helper(self, rs, cs, re, ce, grid):
        all_same, val = self.is_all_same(rs, cs, re, ce, grid)
    
        if all_same:
            return Node(val, True)
        
        root = Node(val, False)
        step = (re-rs)//2
        directions = []

        for i in range(rs, re, step):
            for k in range(cs, ce, step):
                directions.append((i, k, i+step, k+step))

        root.topLeft = self.helper(*directions[0], grid)
        root.topRight = self.helper(*directions[1], grid)
        root.bottomLeft = self.helper(*directions[2], grid)
        root.bottomRight = self.helper(*directions[3], grid)

        return root
    
    def is_all_same(self, rs, cs, re, ce, grid):
        prev = grid[rs][cs]
        for r in range(rs, re):
            for c in range(cs, ce):
                if grid[r][c]!=prev:
                    return False, True
        
        return True, True if prev == 1 else False

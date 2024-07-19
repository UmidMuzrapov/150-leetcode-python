class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        return self.isInterleaveRecursive(s1, s2, s3, 0, 0, 0, {}, -1, 0, 0)
    
    def isInterleaveRecursive(self, s1, s2, s3, start1, start2, start3, memo, prev, n, m):
        if start3 >= len(s3):
            return abs(n - m) <= 1
        
        target = s3[start3]
        for i, s in enumerate([s1, s2]):
            if (start1, start2, start3) in memo:
                return memo[(start1, start2, start3)]
            
            start = start1 if i == 0 else start2
            if start < len(s) and target in s[start:]:
                loc = s[start:].find(target) + 1 + start
                n_new, m_new = self.getChunks(i + 1, prev, n, m)
                if self.isInterleaveRecursive(s1, s2, s3, 
                                              loc if i == 0 else start1, 
                                              loc if i == 1 else start2, 
                                              start3 + 1, memo, i + 1, n_new, m_new):
                    memo[(start1, start2, start3)] = True
                    return True
        
        memo[(start1, start2, start3)] = False
        return False
    
    def getChunks(self, cur, prev, n, m):
        if prev == -1 or cur == prev:
            return n, m
        return (n + 1, m) if cur == 1 else (n, m + 1)

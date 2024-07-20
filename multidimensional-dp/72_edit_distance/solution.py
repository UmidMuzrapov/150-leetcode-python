class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        return self.dfs(word1, word2, 0, 0, {})

    def dfs(self, word1, word2, s1, s2, memo):
        if s1 == len(word1):
            return len(word2) - s2
        if s2 == len(word2):
            return len(word1) - s1

        if (s1, s2) in memo:
            return memo[(s1, s2)]
        
        result = 0
        if word1[s1] == word2[s2]:
            result = self.dfs(word1, word2, s1 + 1, s2 + 1, memo)
        else:
            insert = self.dfs(word1, word2, s1, s2 + 1, memo) + 1
            delete = self.dfs(word1, word2, s1 + 1, s2, memo) + 1
            replace = self.dfs(word1, word2, s1 + 1, s2 + 1, memo) + 1
            result = min(insert, delete, replace)

        memo[(s1, s2)] = result
        return result


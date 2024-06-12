class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        queue = deque([(startGene, 0)])
        mutations = {'A':'CGT', 'C':'AGT', 'G':'ACT', 'T':'ACG'}
        s = {word for word in bank}
        word = ''

        while queue:
            cur, step = queue.popleft()
            if cur == endGene:
                return step

            for i, char in enumerate(cur):
                for m in mutations[char]:
                    word = cur[:i]+m+cur[i+1:]
                    if word in s:
                        queue.append((word, step+1))
                        s.remove(word)
        
        return -1
            


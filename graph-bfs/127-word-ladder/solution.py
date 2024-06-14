class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = deque([(beginWord, 1)])
        s = {word for word in wordList}
        alphabet = 'qwertyuiopasdfghjklzxcvbnm'
        word = ''

        while queue:
            cur, step = queue.popleft()
            if cur == endWord:
                return step
            for i, char in enumerate(cur):
                for l in alphabet:
                    word = cur[:i]+l+cur[i+1:]
                    if word in s:
                        queue.append((word, step+1))
                        s.remove(word)
        
        return 0

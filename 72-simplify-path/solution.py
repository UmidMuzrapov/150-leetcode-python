class Solution:
    '''
    Transform an absolute path to a simplified canonical path
    . current directory
    .. up one directory
    // interpret as a single slash
    '''
    def simplifyPath(self, path: str) -> str:
        words = []
        stack = deque()
        
        for char in path:
            if char == '/':
                self.tackleChunk(words, stack)
            else:
                stack.append(char)
        
        self.tackleChunk(words, stack)

        return "/"+"/".join(words)
    
    def tackleChunk(self, words, stack):
        word = "".join(stack)

        if not word or word==".":
            pass
        elif word == "..":
            if words: words.pop()
        else:
            words.append(word)

        stack.clear()

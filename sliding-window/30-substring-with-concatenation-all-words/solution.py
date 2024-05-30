class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        s_len = len(s)
        word_len = len( words[0])
        words_len = word_len*len(words)
        start = 0
        end = words_len
        substrin = ''
        result = []

        if s_len < words_len:
            return result

        while end <= s_len:
            substring = s[start:end]
            if self.isPermutation(substring, words, word_len):
                result.append(start)
            end+=1
            start+=1
        
        return result
    
    def isPermutation(self, substring, words, word_len):
        my_dict = {}
        for word in words:
            if word in my_dict:
                my_dict[word] += 1
            else:
                my_dict[word] = 1

        word = ''

        for i in range(0, len(substring), word_len):
            word = substring[i:i+word_len]
            if word in my_dict:
                my_dict[word]-=1
            else:
                return False

        for val in my_dict.values():
            if val != 0:
                return False

        return True

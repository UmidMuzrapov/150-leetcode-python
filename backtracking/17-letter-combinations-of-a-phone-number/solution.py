class Solution:
    my_dict =  {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        result = []
        self.helper(0,len(digits), digits, '', result)
        
        return result

    def helper(self, start, end, digits, word, result):
        if start == end:
            result.append(word)
            return

        for char in self.my_dict[digits[start]]:
            self.helper(start+1, end, digits, word + char, result)

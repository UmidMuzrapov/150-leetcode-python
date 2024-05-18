class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = self.skip_to_alnum(s, 0, True)
        right = self.skip_to_alnum(s, len(s) - 1, False)

        while left < right:
            if s[left].lower() != s[right].lower():
                return False
            left = self.skip_to_alnum(s, left + 1, True)
            right = self.skip_to_alnum(s, right - 1, False)
        
        return True
            
    
    def skip_to_alnum(self, s, index, left):
        n = len(s)

        while index < n and index >= 0 and not s[index].isalnum():
            index = index + 1 if left else index - 1

        return index

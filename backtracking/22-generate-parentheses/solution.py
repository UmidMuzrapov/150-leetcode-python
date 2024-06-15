class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def helper(opening, closing, accum):
            if opening == n and closing == n:
                result.append(accum)
            
            if opening < n:
                helper(opening + 1, closing, accum+'(')
            if opening > closing:
                helper(opening, closing+1, accum+')')

        result = []
        helper(0, 0, '')
        return result

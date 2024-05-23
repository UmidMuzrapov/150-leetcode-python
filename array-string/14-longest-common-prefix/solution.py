class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        go_on = True
        result = ""
        i = 0

        while go_on:
            char = ''
            if i < len(strs[0]):
                char = strs[0][i] 
            else:
                return result

            for s in strs:
                if len(s) > i and s[i] == char:
                    pass
                else:
                    return result
            
            result=result + char
            i+=1
        

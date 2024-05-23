class Solution:
    def convert(self, s: str, numRows: int) -> str:
        result = [[] for _ in range(numRows)]
        n = len(s)
        step = max(numRows, numRows + (numRows - 2))

        for i in range(0, n, step):
            for k in range (0, min(step, n - i)):
                if k < numRows:
                    result[k].append(s[i+k])
                else:
                    adjusted_i = (numRows - 2) - k%numRows
                    result[adjusted_i].append(s[i+k])
        
        s_result = ''
        for row in result:
            s_result+=''.join(row)

        return s_result

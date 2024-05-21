class Solution:
    def romanToInt(self, s: str) -> int:
        my_dict = {'I': 1, 'V': 5, 'X': 10, 'L':50, 'C':100, 'D': 500, 'M':1000}
        i = 0
        n = len(s)
        result = 0

        while i < n - 1:
            current = s[i]
            next_val = s[i+1]

            if my_dict[current] >= my_dict[next_val]:
                result +=my_dict[current]
                i+=1
            else:
                result +=(my_dict[next_val] - my_dict[current])
                i+=2
        
        if i == n - 1:
            result+=my_dict[s[i]]

        return result 

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        q = deque()
        a, b = self.equalLength(a, b)

        for i in range(len(a)-1, -1, -1):
            val, carry =self.addDigits(int(a[i]), int(b[i]), carry)
            q.appendleft(str(val))
    
        if carry:
            q.appendleft(str(carry))
        
        return ''.join(q)
            
        
    def addDigits(self, digit1, digit2, carry):
        my_sum = digit1 + digit2 + carry
        
        # return val, carry on
        if my_sum == 0:
            return 0, 0
        elif my_sum == 1:
            return 1, 0
        elif my_sum == 2:
            return 0, 1
        elif my_sum == 3:
            return 1, 1
    
    
    def equalLength(self, a, b):
        min_length = min(len(a), len(b))
        max_length = max(len(a), len(b))
        difference = max_length - min_length

        if max_length > len(a):
            a = "0"*difference + a
        
        if max_length > len(b):
            b = "0"*difference + b
        
        return a, b


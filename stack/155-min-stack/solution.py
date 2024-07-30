class MinStack:

    def __init__(self):
        self._min_value = 10**32
        self._stack = deque()
        

    def push(self, val: int) -> None:
        if self._min_value > val:
            self._min_value = val

        self._stack.append(val)

    def pop(self) -> None:
        val = self._stack.pop()
        if val == self._min_value:
            self._min_value = min(self._stack) if self._stack else 10**32
        
    def top(self) -> int:
        return self._stack[-1]
        

    def getMin(self) -> int:
        return self._min_value
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

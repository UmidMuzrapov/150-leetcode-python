class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = set(['+',"-","/", "*"])
        for token in tokens:
            if token in operations:
                rightOperator = stack.pop()
                leftOperator = stack.pop()
                eval = self.evaluate(leftOperator, rightOperator, token)
                stack.append(eval)
            else:
                stack.append(int(token))
        
        return stack.pop()
        
    def evaluate(self, leftOperator, rightOperator, operation):
        #print(f'left {leftOperator} right {rightOperator} operation {operation}')
        if operation == '-':
            return leftOperator - rightOperator
        elif operation == '+':
            return leftOperator + rightOperator
        elif operation == '*':
            return leftOperator * rightOperator
        else:
            floorVal = floor(leftOperator/rightOperator)
            ceilVal = ceil(leftOperator/rightOperator)
            return floorVal if abs(floorVal) < abs(ceilVal) else ceilVal


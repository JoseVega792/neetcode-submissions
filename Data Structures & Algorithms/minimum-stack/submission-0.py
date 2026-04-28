class MinStack:

    def __init__(self):
        self.minVal = {}
        self.stack = []

    def push(self, val: int) -> None:
        self.minVal[len(self.stack)] = val if not self.minVal else min(val, self.minVal[len(self.stack) - 1])
        self.stack.append(val)

    def pop(self) -> None:
        del self.minVal[len(self.stack)-1]
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minVal[len(self.stack)- 1] 
        

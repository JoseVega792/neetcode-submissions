class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == '+':
                first, second = stack.pop(), stack.pop()
                curr = first + second
                stack.append(curr)
            elif t == '*':
                first, second = stack.pop(), stack.pop()
                curr = first * second
                stack.append(curr)
            elif t == '/':
                first, second = stack.pop(), stack.pop()
                curr = int(second / first)
                stack.append(curr)
            elif t == '-':
                first, second = stack.pop(), stack.pop()
                curr = second - first
                stack.append(curr)
            else:
                stack.append(int(t))
        return stack[-1]
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for t in tokens:
            if t in ('+', '-', '*', '/'):
                sec = int(nums.pop())
                first = int(nums.pop())
                if t == '+':
                    nums.append(first + sec)
                elif t == '-':
                    nums.append(first - sec)
                elif t == '*':
                    nums.append(first * sec)
                elif t == '/':
                    nums.append(int(first / sec))
            else:
                nums.append(t)
        return int(nums[-1])
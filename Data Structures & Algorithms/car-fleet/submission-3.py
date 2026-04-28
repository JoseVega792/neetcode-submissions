class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = sorted([(p,s) for p,s in zip(position, speed)])
        stack = []
        for p,s in fleets[::-1]:
            trajectory = (target - p) / s
            stack.append(trajectory)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
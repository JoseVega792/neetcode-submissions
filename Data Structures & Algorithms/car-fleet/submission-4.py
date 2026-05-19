class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = sorted([(position[i], speed[i]) for i in range(len(position))])
        stack = []
        for p,s in fleets[::-1]:
            traj = (target - p) / s
            stack.append(traj)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

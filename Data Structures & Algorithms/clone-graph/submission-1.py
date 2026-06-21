"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        adj = {}
        firstVal = node.val
        queue = deque([node])
        while queue:
            currNode = queue.popleft()
            if currNode.val not in adj:
                adj[currNode.val] = Node(currNode.val)
            for nei in currNode.neighbors:
                if nei.val not in adj:
                    adj[nei.val] = Node(nei.val)
                    queue.append(nei)
                adj[currNode.val].neighbors.append(adj[nei.val])
        return adj[firstVal]
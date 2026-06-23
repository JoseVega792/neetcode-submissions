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
        
        nodes = {}
        nodes[node.val] = Node(node.val)
        queue = deque([node])
        while queue:
            currNode = queue.popleft()
            for nei in currNode.neighbors:
                if nei.val not in nodes:
                    nodes[nei.val] = Node(nei.val)
                    queue.append(nei)
                nodes[currNode.val].neighbors.append(nodes[nei.val])
        return nodes[node.val]
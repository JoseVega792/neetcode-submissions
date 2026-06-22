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
        firstVal = node.val
        queue = deque([node])
        while queue:
            currNode = queue.popleft()
            if currNode.val not in nodes:
                nodes[currNode.val] = Node(currNode.val)
            for n in currNode.neighbors:
                if n.val not in nodes:
                    nodes[n.val] = Node(n.val)
                    queue.append(n)
                nodes[currNode.val].neighbors.append(nodes[n.val])
        return nodes[firstVal]
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        nodeMap = {}
        newHead = Node(head.val)
        nodeMap[head] = newHead

        #Setup Nodes
        temp = head.next
        prev = newHead
        while temp:
            curr = Node(temp.val)
            prev.next = curr
            nodeMap[temp] = curr
            prev = prev.next
            temp = temp.next

        #Setup Random
        runner = newHead
        temp = head
        while temp:
            runner.random = nodeMap[temp.random] if temp.random else None
            runner = runner.next
            temp = temp.next
        
        return newHead
        
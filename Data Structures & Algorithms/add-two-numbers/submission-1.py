# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        start = ListNode()
        intial = start
        remainder = 0
        while l1 or l2 or remainder:
            currVal = remainder
            if l1:
                currVal += l1.val 
            if l2:
                currVal += l2.val
            remainder = currVal // 10
            nodeVal = currVal % 10
            newNode = ListNode(nodeVal)
            intial.next = newNode
            intial = intial.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return start.next
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
            currVal += l1.val if l1 else 0
            currVal += l2.val if l2 else 0

            #Obtain sum and remainder
            remainder = currVal // 10
            nodeVal = currVal % 10

            #Construct new node and add to new list
            intial.next = ListNode(nodeVal)

            #Continue to next node
            intial = intial.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return start.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        newList = ListNode(0,head)
        node = head
        while n:
            node = node.next
            n -= 1
        
        newList = ListNode(0,head)
        curr = newList
        while node:
            curr = curr.next
            node = node.next
        
        curr.next = curr.next.next
        return newList.next
        

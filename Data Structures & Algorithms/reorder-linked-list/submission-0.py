# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        # find midpoint
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # reverse 
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        # set
        start = head
        count = 1
        while start:
            count += 1
            if count % 2 == 0:
                prevNext = prev.next
                temp = start.next
                start.next = prev
                prev.next = temp
                prev = prevNext
            start = start.next

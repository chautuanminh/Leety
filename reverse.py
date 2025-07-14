# Definition for singly-linked list.
class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # c, pre, tem 
        # prev --> none how does this work?
        # c = head & prev = none
        # t = c
        # c.next = prev
        # prev = c
        # c = t.next
        cur = head
        prev = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev
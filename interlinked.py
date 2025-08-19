# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        
        p1, p2 = headA, headB
        
        while p1 != p2:
            # when one pointer reaches end, redirect it to the other list's head
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA
        
        return p1
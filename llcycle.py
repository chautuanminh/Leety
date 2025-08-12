# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur = head
        seen = set()
        if cur is None: 
            return False
        while cur not in seen:
            if cur.next is None: 
                return False
            seen.add(cur)
            cur = cur.next
        return cur in seen
        
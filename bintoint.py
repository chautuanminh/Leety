# Definition for singly-linked list.
from collections import *
from typing import *
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
def list_to_linked_list(values):
    dummy = ListNode()
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        count = 0
        current = head
        while current:
            count = (count * 2) + current.val
            current = current.next
        return count 

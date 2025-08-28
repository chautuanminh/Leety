# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()   # create a dummy node
        current = dummy       # pointer to build the list\
        carry = 0
        while l1 or l2 or carry:
            temp1 = l1.val if l1 else 0
            temp2 = l2.val if l2 else 0
            sum_val = (temp1 + temp2 + carry) 
            carry = sum_val // 10
            sum_val = sum_val % 10
            current.next = ListNode(sum_val)
            current = current.next
            if l1:
                l1 = l1.next 
            else: l1 = None
            if l2: 
                l2 = l2.next
            else: l2 = None 
        return dummy.next
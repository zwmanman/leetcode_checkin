# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return head
        
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        
        while head:
            if head.val == val:
                prev.next = head.next
            else:
                prev = prev.next
            head = head.next
            
        return dummy.next
            
            
            
            
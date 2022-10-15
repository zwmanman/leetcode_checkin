# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode()
        prev = dummy
        
        if not head or not head.next:
            return head
        
        while head and head.next:
            nextNode = head.next
            prev.next = nextNode
            n_node = nextNode.next
            
            nextNode.next = head
            head.next = n_node
            
            prev = head
            head = n_node
            
        return dummy.next
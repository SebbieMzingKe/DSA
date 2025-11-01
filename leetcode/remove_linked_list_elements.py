# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """

        if not head:
            return None

        # returns a minimum number of runtime
        # head.next = self.removeElements(head.next, val)
        # return head.next if head.val == val else head

        dummy = ListNode(0, head)
        prev = dummy
        
        while prev.next:
            if prev.next.val == val:
                prev.next = prev.next.next
            else:
                prev = prev.next
        
        return dummy.next
    
        # dummy = ListNode(next = head)
        # prev, current = dummy, head

        # while current:
        #     nxt = current.next
        #     if current.val == val:
        #         prev.next = nxt
        #     else:
        #         prev = current
        #     current = nxt
        # return dummy.next
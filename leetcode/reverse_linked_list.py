class Solution(object):
    def reversList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev, current = None, head

        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        return prev
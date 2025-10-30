# Definition for singly-linked list.
from turtle import right


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """

        temp = ListNode(0, head)
        left_ptr = temp
        right_ptr = head

        for _ in range(n):
            right_ptr = right_ptr.next

        while right_ptr:
            left_ptr = left_ptr.next
            right_ptr = right_ptr.next
        left_ptr.next = left_ptr.next.next

        return temp.next
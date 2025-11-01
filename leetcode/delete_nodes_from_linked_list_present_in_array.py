class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        nums_set = set(nums)
        dummy = ListNode(0, head)
        prev = dummy

        while prev.next:
            if prev.next.val in nums_set:
                prev.next = prev.next.next
            else:
                prev = prev.next
        return dummy.next
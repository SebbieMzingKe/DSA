class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        prev_index = -float('inf') #last position of 1

        for i, num in enumerate(nums):
            if num == 1:
                if i - prev_index - 1 < k:
                    return False
        return True
        

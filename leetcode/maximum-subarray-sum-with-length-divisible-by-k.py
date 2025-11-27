class Solution(object):
    def maxSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        min_prefix = [float("inf")] * k      
        min_prefix[0] = 0

        max_sum = float("-inf")
        current_sum = 0

        for i, num in enumerate(nums):
            current_sum += num
            remainder = (i + 1) % k

            max_sum = max(max_sum, current_sum - min_prefix[remainder])
            min_prefix[remainder] = min(min_prefix[remainder], current_sum)

        return max_sum
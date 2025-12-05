class Solution(object):
    def countPartitions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        result = 0

        left = 0
        right = sum(nums)

        for i in range(n - 1):
            left += nums[i]
            right -= nums[i]

            if (left - right) % 2 == 0:
                result += 1
        return result
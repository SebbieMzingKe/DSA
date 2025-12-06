from collections import deque


class Solution(object):
    def countPartitions(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        MOD = 10 ** 9 + 7
        n = len(nums)

        dp = [0] * (n + 1)
        dp[0] = 1

        max_dq = deque()
        min_dq = deque()

        left = 0
        accumulated = 1

        for r in range(n):
            while max_dq and max_dq[-1] < nums[r]:
                max_dq.pop()
            
            max_dq.append(nums[r])
            
            while min_dq and min_dq[-1] > nums[r]:
                min_dq.pop()
            
            min_dq.append(nums[r])

            while max_dq[0] - min_dq[-1] > k:

                if max_dq[0] == nums[left]:
                    max_dq.popleft()

                if min_dq[0] == nums[left]:
                    min_dq.popleft()

                accumulated = (accumulated - dp[left]) % MOD
                left += 1

            dp[r + 1] = accumulated
            accumulated = (accumulated + dp[r + 1]) % MOD

        return dp[n]


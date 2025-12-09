from collections import defaultdict


class Solution(object):
    def specialTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        MOD = 10 ** 9 + 7

        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        left_count = defaultdict(int)
        answer = 0

        for j_val in nums:
            target = 2 * j_val

            total = count[target]
            left = left_count[target]

            right = total -left

            if j_val == target:
                right -= 1

            answer = (answer + left * right) % MOD

            left_count[j_val] += 1
        
        return answer
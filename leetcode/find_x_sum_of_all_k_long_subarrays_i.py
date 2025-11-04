from collections import Counter


class Solution(object):
    def findXSum(self, nums, k, x):
        """
        :type nums: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """

        answer = []

        for i in range(len(nums) - k + 1):
            window = nums[i:i + k]
            frequency = Counter(window)

            if len(frequency) <= x:
                answer.append(frequency)
            
            else:
                pairs = sorted(frequency.items(), key = lambda p: ([p[1], p[0]]), reverse=True)

                x_sum = sum(num * count for num, count in pairs[:x])
                answer.append(x_sum)
        return answer
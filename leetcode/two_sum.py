class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i, j in enumerate(nums):
            diff = target - j
            if diff in hashmap:
                return [i, hashmap[diff]]
            hashmap[j] = i
        return []
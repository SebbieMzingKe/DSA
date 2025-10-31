class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        seen = set()
        result = []

        for n in nums:
            if n in seen:
                result.append(n)
            else:
                seen.add(n)
        return result
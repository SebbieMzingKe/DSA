class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """

        count = (high - low) // 2
        if low % 2 == 1 or high % 2 == 1:
            count += 1
        return count
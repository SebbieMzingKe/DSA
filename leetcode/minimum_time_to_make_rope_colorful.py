class Solution(object):
    def minCost(self, colors, neededTime):
        """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
        """

        result = 0
        for i in range(1, len(colors)):
            if colors[i] == colors[i - 1]:

                # remove balloon with smaller time
                result += min(neededTime[i], neededTime[i - 1])

                # keep max index for next comparison
                neededTime[i] = max(neededTime[i], neededTime[i - 1])

        return result
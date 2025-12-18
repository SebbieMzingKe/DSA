class Solution(object):
    def maximumProfit(self, prices, k):
        """
        :type prices: List[int]
        :type k: int
        :rtype: int
        """

        dp = [[float('-inf')] * 3 for _ in range(k + 1)]

        dp[0][0] = 0

        for p in prices:

            new_dp = [row[:] for row in dp]

            for j in range(k + 1):
                
                if dp[j][1] != float('-inf'):
                    new_dp[j][0] = max(new_dp[j][0], dp[j][1] + p)

                if dp[j][2] != float('-inf'):
                    new_dp[j][0] = max(new_dp[j][0], dp[j][2] - p)

                if j < k:

                    if dp[j][0] != float('-inf'):
                        new_dp[j + 1][1] = max(new_dp[j + 1][1], dp[j][0] - p)

                    if dp[j][0] != float('-inf'):
                        new_dp[j + 1][2] = max(new_dp[j + 1][2], dp[j][0] + p)
            dp = new_dp

        return max(dp[j][0] for j in range(k + 1))


if __name__ == "__main__":
    solver = Solution()
    
    # Test Case 1
    prices1 = [1, 7, 9, 8, 2]
    k1 = 2
    result1 = solver.maximumProfit(prices1, k1)
    print(f"Test Case 1: {result1} (Expected: 14)")

    # Test Case 2
    prices2 = [12, 16, 19, 19, 8, 1, 19, 13, 9]
    k2 = 3
    result2 = solver.maximumProfit(prices2, k2)
    print(f"Test Case 2: {result2} (Expected: 36)")
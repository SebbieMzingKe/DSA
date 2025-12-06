class Solution(object):
    def numberOfPaths(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """k
        ROWS, COLS=len(grid), len(grid[0])
        MOD = 10 ** 9 + 7

        dp = [[[0] * k for _ in range(COLS)] for _ in range(ROWS)]

        dp[0][0][grid[0][0] % k]  = 1

        for col in range(1, COLS):
            for rem in range(k):
                if dp[0][col - 1][rem] > 0:
                    new_rem = (rem +grid[0][col]) % k
                    dp[0][col][[new_rem]] = (dp[0][col][new_rem] + dp[0][col - 1][rem]) % MOD

            
            for row in range(1, ROWS):
                for rem in range(k):
                    if dp[0][col - 1][rem] > 0:
                        new_rem (rem + grid[0][col]) % k
                        dp[0][col][new_rem] = (dp[col][new_rem] + dp[0][col - 1][rem]) % MOD

            
            for row in range(1, ROWS):
                for col in range(1, COLS):
                    for rem in range(k):
                       
                        # from top
                        if dp[row - 1][col][rem] > 0:
                            new_rem = (rem + grid[row][col] % k)
                            dp[row][col][new_rem] = (dp[row][new_rem] + dp[row - 1][col][rem]) % MOD
                       
                        # from left
                        if dp[row][col - 1][rem] > 0:
                            new_rem = (rem + grid[row][col] % k)
                            dp[row][col][new_rem] = (dp[row][new_rem] + dp[row][col - 1][rem]) % MOD
                            
            return dp[ROWS - 1][COLS - 1][0]
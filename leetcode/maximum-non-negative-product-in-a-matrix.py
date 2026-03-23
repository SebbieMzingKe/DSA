class Solution(object):
    def maxProductPath(self, grid):

        m, n = len(grid), len(grid[0])
        
        MOD = 10**9 + 7

        max_dp = [[0] * n for _ in range(m)]
        min_dp = [[0] * n for _ in range(m)]
        
        max_dp[0][0] = min_dp[0][0] = grid[0][0]
        
        for i in range(1, m):
            max_dp[i][0] = min_dp[i][0] = max_dp[i-1][0] * grid[i][0]
            
        for j in range(1, n):
            max_dp[0][j] = min_dp[0][j] = max_dp[0][j-1] * grid[0][j]
            
        for i in range(1, m):
            for j in range(1, n):
                val = grid[i][j]
                p1 = max_dp[i-1][j] * val
                p2 = min_dp[i-1][j] * val
                p3 = max_dp[i][j-1] * val
                p4 = min_dp[i][j-1] * val
                
                max_dp[i][j] = max(p1, p2, p3, p4)
                min_dp[i][j] = min(p1, p2, p3, p4)
                
        ans = max_dp[m-1][n-1]
        return -1 if ans < 0 else ans % MOD


if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, grid, expected):
        result = solver.maxProductPath(grid)
        status = "PASS" if result == expected else "FAIL"

        print(f"Test Case {case_num}:")
        for row in grid:
            print(f"  {row}")
        print(f"Output:   {result}")
        print(f"Expected: {expected}")
        print(f"Status:   {status}\n")

    # Example 1
    run_test(1, [[-1, -2, -3], [-2, -3, -3], [-3, -3, -2]], -1)

    # Example 2
    run_test(2, [[1, -2, 1], [1, -2, 1], [3, -4, 1]], 8)

    # Example 3
    run_test(3, [[1, 3], [0, -4]], 0)

    # Custom Case: Single cell
    run_test(4, [[-3]], -1)

    # Custom Case: Single cell positive
    run_test(5, [[3]], 3)

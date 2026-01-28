class Solution(object):
    def minCost(self, grid, k):
        m, n = len(grid), len(grid[0])
        dp = [[float("inf")] * n for _ in range(m)]
        dp[0][0] = 0
        MAX_VAL = 10002

        for turn in range(k + 1):
            # normal moves
            for i in range(m):
                for j in range(n):
                    if i > 0:
                        cost = dp[i - 1][j] + grid[i][j]
                        if cost < dp[i][j]:
                            dp[i][j] = cost
                    if j > 0:
                        cost = dp[i][j - 1] + grid[i][j]
                        if cost < dp[i][j]:
                            dp[i][j] = cost

            # teleportation
            if turn < k:
                min_cost_by_val = [float("inf")] * MAX_VAL
                for i in range(m):
                    for j in range(n):
                        val = grid[i][j]
                        if dp[i][j] < min_cost_by_val[val]:
                            min_cost_by_val[val] = dp[i][j]

                current_min = float("inf")
                for v in range(MAX_VAL - 1, -1, -1):
                    if min_cost_by_val[v] < current_min:
                        current_min = min_cost_by_val[v]
                    min_cost_by_val[v] = current_min

                for i in range(m):
                    for j in range(n):
                        val = grid[i][j]
                        if min_cost_by_val[val] < dp[i][j]:
                            dp[i][j] = min_cost_by_val[val]

        return dp[m - 1][n - 1]


if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, grid, k, expected):
        result = solver.minCost(grid, k)
        status = "PASS" if result == expected else "FAIL"
        print(
            f"Test Case {case_num}: Result {result} (Expected: {expected}) -> {status}"
        )

    # Example 1
    # Path: (0,0)->(1,0)->(1,1)->Teleport(2,2)
    # Costs: 0 -> 2 -> 7 -> 7
    grid1 = [[1, 3, 3], [2, 5, 4], [4, 3, 5]]
    run_test(1, grid1, 2, 7)

    # Example 2
    # No useful teleport (sources are smaller than required destinations)
    # Path: (0,0)->(1,0)->(1,1)->(2,1)
    # Costs: 0 -> 2 -> 5 -> 9
    grid2 = [[1, 2], [2, 3], [3, 4]]
    run_test(2, grid2, 1, 9)

    # Custom Case: Large jump
    # (0,0)=10, (0,1)=100, (1,0)=100, (1,1)=5
    # Move normal would be huge. Teleport (0,0) -> (1,1) possible since 10 >= 5.
    # Cost: 0 -> 0 (at 1,1). But wait, we must reach m-1, n-1.
    # Cost at (0,0) is 0. Teleport to (1,1) cost 0. Done.
    grid3 = [[10, 100], [100, 5]]
    run_test(3, grid3, 1, 0)

class Solution(object):
    def maximumAmount(self, coins):
        m, n = len(coins), len(coins[0])
        dp = [[-float("inf")] * 3 for _ in range(n)]

        v0 = coins[0][0]
        dp[0][0] = v0
        dp[0][1] = 0 if v0 < 0 else v0
        dp[0][2] = 0 if v0 < 0 else v0

        for j in range(1, n):
            v = coins[0][j]
            for k in range(3):
                if dp[j - 1][k] != -float("inf"):
                    dp[j][k] = dp[j - 1][k] + v
                if v < 0 and k > 0 and dp[j - 1][k - 1] != -float("inf"):
                    dp[j][k] = max(dp[j][k], dp[j - 1][k - 1])

        for i in range(1, m):
            v = coins[i][0]
            new_dp0 = [-float("inf")] * 3
            for k in range(3):
                if dp[0][k] != -float("inf"):
                    new_dp0[k] = dp[0][k] + v
                if v < 0 and k > 0 and dp[0][k - 1] != -float("inf"):
                    new_dp0[k] = max(new_dp0[k], dp[0][k - 1])
            dp[0] = new_dp0

            for j in range(1, n):
                v = coins[i][j]
                new_dpj = [-float("inf")] * 3
                for k in range(3):
                    best_prev = max(dp[j][k], dp[j - 1][k])
                    if best_prev != -float("inf"):
                        new_dpj[k] = best_prev + v
                    if v < 0 and k > 0:
                        best_prev_k1 = max(dp[j][k - 1], dp[j - 1][k - 1])
                        if best_prev_k1 != -float("inf"):
                            new_dpj[k] = max(new_dpj[k], best_prev_k1)
                dp[j] = new_dpj

        return dp[n - 1][2]


if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, coins, expected):
        result = solver.maximumAmount(coins)
        status = "PASS" if result == expected else "FAIL"

        print(f"Test Case {case_num}:")
        print(f"  Grid:")
        for row in coins:
            print(f"    {row}")
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}")
        print(f"  Status:   {status}\n")

    # Example 1
    run_test(1, [[0, 1, -1], [1, -2, 3], [2, -3, 4]], 8)

    # Example 2
    run_test(2, [[10, 10, 10], [10, 10, 10]], 40)

    # Custom Case: All heavily negative, only 2 neutralizations
    run_test(3, [[-10, -10], [-10, -10]], -10)

    # Custom Case: 1D path
    run_test(4, [[-5, -5, -5, -5]], -10)

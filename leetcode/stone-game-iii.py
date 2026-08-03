class Solution(object):
    def stoneGameIII(self, stoneValue):
        n = len(stoneValue)
        dp = [-float("inf")] * (n + 1)
        dp[n] = 0

        for i in range(n - 1, -1, -1):
            take_sum = 0
            for k in range(1, 4):
                if i + k <= n:
                    take_sum += stoneValue[i + k - 1]
                    dp[i] = max(dp[i], take_sum - dp[i + k])

        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"


if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, stoneValue, expected):
        result = solver.stoneGameIII(stoneValue)
        status = "PASS" if result == expected else "FAIL"

        print(f"Test Case {case_num}:")
        print(f"  Input:    {stoneValue}")
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}")
        print(f"  Status:   {status}\n")

    # Example 1
    run_test(1, [1, 2, 3, 7], "Bob")

    # Example 2
    run_test(2, [1, 2, 3, -9], "Alice")

    # Example 3
    run_test(3, [1, 2, 3, 6], "Tie")

    # Custom Case 4: All negative stones
    run_test(4, [-1, -2, -3], "Tie")

class Solution(object):
    def numberOfStableArrays(self, zero, one, limit):
        MOD = 10**9 + 7

        dp0 = [[0] * (one + 1) for _ in range(zero + 1)]
        dp1 = [[0] * (one + 1) for _ in range(zero + 1)]

        for i in range(1, min(zero, limit) + 1):
            dp0[i][0] = 1
        for j in range(1, min(one, limit) + 1):
            dp1[0][j] = 1

        for i in range(1, zero + 1):
            for j in range(1, one + 1):
                dp0[i][j] = (dp0[i - 1][j] + dp1[i - 1][j]) % MOD
                if i > limit:
                    dp0[i][j] = (dp0[i][j] - dp1[i - limit - 1][j]) % MOD

                dp1[i][j] = (dp0[i][j - 1] + dp1[i][j - 1]) % MOD
                if j > limit:
                    dp1[i][j] = (dp1[i][j] - dp0[i][j - limit - 1]) % MOD

        return (dp0[zero][one] + dp1[zero][one]) % MOD


if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, zero, one, limit, expected):
        import time

        start_time = time.time()

        result = solver.numberOfStableArrays(zero, one, limit)

        end_time = time.time()
        status = "PASS" if result == expected else "FAIL"

        print(f"Test Case {case_num}: zero={zero}, one={one}, limit={limit}")
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}")
        print(f"  Status:   {status}")
        print(f"  Time:     {end_time - start_time:.4f} seconds\n")

    # Example 1
    run_test(1, 1, 1, 2, 2)

    # Example 2
    run_test(2, 1, 2, 1, 1)

    # Example 3
    run_test(3, 3, 3, 2, 14)

    run_test(4, 500, 500, 10, 89454152)

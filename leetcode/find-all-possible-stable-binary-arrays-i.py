from ast import mod


class Solution(object):
    def numberOfStableArrays(self, zero, one, limit):
        MOD = 10 ** 9 + 7

        dp = [[[0, 0] for _ in range(one + 1)] for _ in range(zero + 1)]
        
        for i in range(1, min(zero, limit) + 1):
            dp[i][0][0] = 1
        for j in range(1, min(one, limit) + 1):
            dp[0][j][1] = 1
            
        for i in range(1, zero + 1):
            for j in range(1, one + 1):
                dp[i][j][0] = (dp[i - 1][j][0] + dp[i - 1][j][1]) % MOD
                if i > limit:
                    dp[i][j][0] = (dp[i][j][0] - dp[i - limit - 1][j][1]) % MOD
                    
                dp[i][j][1] = (dp[i][j - 1][0] + dp[i][j - 1][1]) % MOD
                if j > limit:
                    dp[i][j][1] = (dp[i][j][1] - dp[i][j - limit - 1][0]) % MOD
                    
        return (dp[zero][one][0] + dp[zero][one][1]) % MOD


if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, zero, one, limit, expected):
        result = solver.numberOfStableArrays(zero, one, limit)
        status = "PASS" if result == expected else "FAIL"

        print(f"Test Case {case_num}: zero={zero}, one={one}, limit={limit}")
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}")
        print(f"  Status:   {status}\n")

    # Example 1
    run_test(1, 1, 1, 2, 2)

    # Example 2
    run_test(2, 1, 2, 1, 1)

    # Example 3
    run_test(3, 3, 3, 2, 14)

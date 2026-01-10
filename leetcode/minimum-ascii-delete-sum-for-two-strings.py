class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """

        m, n = len(s1), len(s2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])

        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] + ord(s2[j - 1])

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]

                else:
                    cost_delete_s1 = dp[i - 1][j] + ord(s1[i - 1])
                    cost_delete_s2 = dp[i][j - 1] + ord(s2[j - 1])
                    dp[i][j] = min(cost_delete_s1, cost_delete_s2)

        return dp[m][n]


if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, s1, s2, expected):
        result = solver.minimumDeleteSum(s1, s2)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test Case {case_num}: '{s1}', '{s2}' -> {result} (Expected: {expected}) -> {status}")

    # Example 1
    # Deleting 's' from "sea" (115) and 't' from "eat" (116) = 231
    run_test(1, "sea", "eat", 231)

    # Example 2
    # "delete" -> "let" (delete d, e, e)
    # "leet" -> "let" (delete e)
    # Sum: 100 + 101 + 101 + 101 = 403
    run_test(2, "delete", "leet", 403)
    
    # Edge Case: Identical strings (Cost 0)
    run_test(3, "hello", "hello", 0)
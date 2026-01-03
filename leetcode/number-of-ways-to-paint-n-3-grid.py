class Solution(object):
    def numOfWays(self, n):
        """
        :type n: int
        :rtype: int
        """

        MOD = 10 ** 9 + 7

        aba = 6
        abc = 6

        for _ in range(n - 1):
            new_aba = (3 * aba + 2 * abc) % MOD
            new_abc = (2 * aba + 2 * abc) % MOD

            aba, abc = new_aba, new_abc

        return (aba + abc) % MOD


if __name__ == "__main__":
    solver = Solution()
    
    # Helper to print pass/fail
    def run_test(case_num, n, expected):
        result = solver.numOfWays(n)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test Case {case_num}: n={n} -> Result: {result} (Expected: {expected}) -> {status}")

    # Example 1
    # n = 1
    # Expected: 12 (6 ABA + 6 ABC)
    run_test(1, 1, 12)
    
    # Example 2
    # n = 2
    # Calculation:
    # A2 = 3*6 + 2*6 = 18 + 12 = 30
    # B2 = 2*6 + 2*6 = 12 + 12 = 24
    # Total = 54
    run_test(2, 2, 54)
    
    # Example 3
    # n = 5000
    run_test(3, 5000, 30228214)
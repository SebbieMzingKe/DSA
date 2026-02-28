class Solution(object):
    def concatenatedBinary(self, n):
        MOD = 10**9 + 7
        ans = 0
        bit_length = 0

        for i in range(1, n + 1):
            if i & (i - 1) == 0:
                bit_length += 1


            ans = ((ans << bit_length) | i) % MOD

        return ans

if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, n, expected):
        result = solver.concatenatedBinary(n)
        status = "PASS" if result == expected else "FAIL"
        print(
            f"Test Case {case_num}: n={n} -> {result} (Expected: {expected}) -> {status}"
        )

    # Example 1
    # 1 -> "1" -> 1
    run_test(1, 1, 1)

    # Example 2
    # 1, 2, 3 -> "1" + "10" + "11" -> "11011" -> 27
    run_test(2, 3, 27)

    # Example 3
    run_test(3, 12, 505379714)

    # Custom Case: n=4
    # 1, 2, 3, 4 -> "1" + "10" + "11" + "100" -> "11011100" -> 220
    run_test(4, 4, 220)

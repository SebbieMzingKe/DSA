class Solution(object):
    def winnerSquareGame(self, n):
        dp = [False] * (n + 1)

        squares = []
        k = 1
        while k * k <= n:
            squares.append(k * k)
            k += 1

        for i in range(1, n + 1):
            for sq in squares:
                if sq > i:
                    break
                if not dp[i - sq]:
                    dp[i] = True
                    break

        return dp[n]


if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, n, expected):
        result = solver.winnerSquareGame(n)
        status = "PASS" if result == expected else "FAIL"

        print(f"Test Case {case_num}:")
        print(f"  Input:    n = {n}")
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}")
        print(f"  Status:   {status}\n")

    # Example 1
    run_test(1, 1, True)

    # Example 2
    run_test(2, 2, False)

    # Example 3
    run_test(3, 4, True)

    # Custom Case 4: Larger number
    run_test(4, 7, False)

    # Custom Case 5: 17 stones (17 -> 16 -> 1) Alice wins
    run_test(5, 17, True)

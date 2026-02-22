class Solution(object):
    def binaryGap(self, n):
        max_gap = 0
        last_pos = -1
        pos = 0

        while n > 0:
            if n & 1 == 1:
                if last_pos != -1:
                    max_gap = max(max_gap, pos - last_pos)
                last_pos = pos
            n >>= 1
            pos += 1

        return max_gap


if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, n, expected):
        result = solver.binaryGap(n)
        status = "PASS" if result == expected else "FAIL"

        binary_rep = bin(n)[2:]
        print(
            f"Test Case {case_num}: n={n} ({binary_rep}) -> Gap: {result} (Expected: {expected}) -> {status}"
        )

    # Example 1
    # 22 is "10110". Gaps are 2 (between pos 1 and 3) and 1 (between 3 and 4). Max is 2.
    run_test(1, 22, 2)

    # Example 2
    # 8 is "1000". Only one '1', so no adjacent pairs. Gap is 0.
    run_test(2, 8, 0)

    # Example 3
    # 5 is "101". Distance between the two '1's is 2.
    run_test(3, 5, 2)

    # Custom Case: All 1s
    # 15 is "1111". Max distance between any adjacent pair is 1.
    run_test(4, 15, 1)

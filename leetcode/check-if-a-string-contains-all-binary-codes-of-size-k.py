class Solution(object):
    def hasAllCodes(self, s, k):
        target_count = 1 << k

        if len(s) < target_count + k - 1:
            return False

        seen = set()

        for i in range(len(s) - k + 1):
            seen.add(s[i : i + k])

            if len(seen) == target_count:
                return True
        return len(seen) == target_count


if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, s, k, expected):
        result = solver.hasAllCodes(s, k)
        status = "PASS" if result == expected else "FAIL"
        print(
            f"Test Case {case_num}: s='{s}', k={k} -> {result} (Expected: {expected}) -> {status}"
        )

    # Example 1
    # k=2 -> needs "00", "01", "10", "11"
    run_test(1, "00110110", 2, True)

    # Example 2
    # k=1 -> needs "0", "1"
    run_test(2, "0110", 1, True)

    # Example 3
    # k=2 -> missing "00"
    run_test(3, "0110", 2, False)

    # Custom Case: String too short
    # k=3 needs at least length 2^3 + 3 - 1 = 10
    run_test(4, "010101", 3, False)

    # Custom Case: Exact minimum length sequence (De Bruijn sequence)
    # k=2 -> length 2^2 + 2 - 1 = 5. "00110" contains 00, 01, 11, 10
    run_test(5, "00110", 2, True)

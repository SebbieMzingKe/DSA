class Solution(object):
    def checkOnesSegment(self, s):
        return "01" not in s


if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, s, expected):
        result = solver.checkOnesSegment(s)
        status = "PASS" if result == expected else "FAIL"
        print(
            f"Test Case {case_num}: '{s}' -> {result} (Expected: {expected}) -> {status}"
        )

    # Example 1
    # "1001" contains "01" in the middle. Second segment of 1s exists.
    run_test(1, "1001", False)

    # Example 2
    # "110" does not contain "01". Only one segment.
    run_test(2, "110", True)

    # Custom Case: Single character
    run_test(3, "1", True)

    # Custom Case: All ones
    run_test(4, "1111", True)

    # Custom Case: Trailing ones after many zeros
    run_test(5, "100000001000", False)

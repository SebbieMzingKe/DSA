class Solution(object):
    def maxSumTrionic(self, nums):

        n = len(nums)
        inc1 = float("-inf")
        dec = float("-inf")
        inc2 = float("-inf")
        max_sum = float("-inf")

        for i in range(1, n):
            curr = nums[i]
            prev = nums[i - 1]

            next_inc1 = float("-inf")
            next_dec = float("-inf")
            next_inc2 = float("-inf")

            if curr > prev:
                next_inc1 = max(prev, inc1) + curr
                next_inc2 = max(inc2, dec) + curr

            elif curr < prev:
                next_dec = max(dec, inc1) + curr

            inc1, dec, inc2 = next_inc1, next_dec, next_inc2

            if inc2 > max_sum:
                max_sum = inc2

        return int(max_sum)


if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, nums, expected):
        result = solver.maxSumTrionic(nums)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test Case {case_num}: {result} (Expected: {expected}) -> {status}")

    # Example 1
    # Path: -2 -> -1 (inc) -> -3 (dec) -> 0 -> 2 (inc)
    # Sum: -4
    run_test(1, [0, -2, -1, -3, 0, 2, -1], -4)

    # Example 2
    # Path: 1 -> 4 (inc) -> 2 (dec) -> 7 (inc)
    # Sum: 14
    run_test(2, [1, 4, 2, 7], 14)

    # Custom Case: Negative numbers domination
    # [-5, -1, -5, -1] -> -1 > -5 (inc), -5 < -1 (dec), -1 > -5 (inc)
    # Sum: -5 + -1 + -5 + -1 = -12
    run_test(3, [-5, -1, -5, -1], -12)

    # Custom Case: Broken chain
    # [1, 2, 3, 3, 2, 1, 5] -> Equal 3 breaks the chain.
    # But later 3, 2, 1, 5 is dec->inc? No, need inc->dec->inc.
    # This specific input might not have a solution if constraints allowed empty,
    # but problem guarantees at least one exists.
    # Let's try [1, 5, 2, 6] (Simple valid) -> 14
    run_test(4, [1, 5, 2, 6], 14)

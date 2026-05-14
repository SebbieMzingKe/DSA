class Solution(object):
    def isGood(self, nums):
        n = max(nums)

        if len(nums) != n + 1:
            return False

        expected = list(range(1, n)) + [n, n]

        return sorted(nums) == expected


if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, nums, expected_bool):
        result = solver.isGood(nums)
        status = "PASS" if result == expected_bool else "FAIL"

        print(f"Test Case {case_num}:")
        print(f"  Input:    {nums}")
        print(f"  Output:   {result}")
        print(f"  Expected: {expected_bool}")
        print(f"  Status:   {status}\n")

    # Example 1
    run_test(1, [2, 1, 3], False)

    # Example 2
    run_test(2, [1, 3, 3, 2], True)

    # Example 3
    run_test(3, [1, 1], True)

    # Example 4
    run_test(4, [3, 4, 4, 1, 2, 1], False)

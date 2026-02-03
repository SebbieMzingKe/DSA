class Solution(object):
    def isTrionic(self, nums):
        n = len(nums)
        if n < 4:
            return False

        # Valid ranges: 0 < p < q < n-1
        for p in range(1, n - 2):
            for q in range(p + 1, n - 1):

                # Verify segment 1 (Increasing)
                if any(nums[i] >= nums[i + 1] for i in range(p)):
                    continue

                # Verify segment 2 (Decreasing)
                if any(nums[i] <= nums[i + 1] for i in range(p, q)):
                    continue

                # Verify segment 3 (Increasing)
                if any(nums[i] >= nums[i + 1] for i in range(q, n - 1)):
                    continue

                return True
        return False


if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, nums, expected):
        result = solver.isTrionic(nums)
        status = "PASS" if result == expected else "FAIL"
        print(
            f"Test Case {case_num}: {nums} -> {result} (Expected: {expected}) -> {status}"
        )

    # Example 1
    # p=2 (val 5), q=4 (val 2)
    # [1,3,5] inc, [5,4,2] dec, [2,6] inc -> True
    run_test(1, [1, 3, 5, 4, 2, 6], True)

    # Example 2
    # Too short / no valid pattern
    run_test(2, [2, 1, 3], False)

    # Custom Case: Minimum valid length (4)
    # [1, 5, 2, 6] -> p=1, q=2
    # 0..1 [1,5] inc? Yes.
    # 1..2 [5,2] dec? Yes.
    # 2..3 [2,6] inc? Yes.
    run_test(3, [1, 5, 2, 6], True)

    # Custom Case: Flat spots (should fail strictly increasing/decreasing)
    # [1, 2, 2, 1, 2] -> p=2? [1,2,2] not strictly inc.
    run_test(4, [1, 2, 2, 1, 2], False)

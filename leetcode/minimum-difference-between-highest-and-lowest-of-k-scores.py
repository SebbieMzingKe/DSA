class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k == 1:
            return 0

        nums.sort()

        min_diff = float("inf")

        for i in range(len(nums) - k + 1):
            current_diff = nums[i + k - 1] - nums[i]

            min_diff = min(min_diff, current_diff)

        return min_diff


if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, nums, k, expected):
        result = solver.minimumDifference(list(nums), k)
        status = "PASS" if result == expected else "FAIL"
        print(
            f"Test Case {case_num}: nums={nums}, k={k} -> {result} (Expected: {expected}) -> {status}"
        )

    # Example 1
    # [90], k=1 -> Diff 0
    run_test(1, [90], 1, 0)

    # Example 2
    # [9,4,1,7] -> Sort -> [1,4,7,9]
    # Windows of size 2:
    # [1,4] diff 3
    # [4,7] diff 3
    # [7,9] diff 2 (Min)
    run_test(2, [9, 4, 1, 7], 2, 2)

    # Custom Case: k equals length
    # [1, 5, 10] k=3 -> Sort [1,5,10] -> 10-1 = 9
    run_test(3, [1, 5, 10], 3, 9)

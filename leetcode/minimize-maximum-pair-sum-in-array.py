class Solution(object):
    def minPairSum(self, nums):
        nums.sort()
        max_pair_sum = 0
        n = len(nums)
        for i in range(n // 2):
            current_sum = nums[i] + nums[n - 1 - i]
            max_pair_sum = max(max_pair_sum, current_sum)
        return max_pair_sum


if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, nums, expected):

        result = solver.minPairSum(list(nums))
        status = "PASS" if result == expected else "FAIL"
        print(
            f"Test Case {case_num}: {nums} -> {result} (Expected: {expected}) -> {status}"
        )

    # Example 1
    # Sorted: [2, 3, 3, 5]
    # Pairs: (2+5)=7, (3+3)=6. Max = 7.
    run_test(1, [3, 5, 2, 3], 7)

    # Example 2
    # Sorted: [2, 3, 4, 4, 5, 6]
    # Pairs: (2+6)=8, (3+5)=8, (4+4)=8. Max = 8.
    run_test(2, [3, 5, 4, 2, 4, 6], 8)

    # Custom Case: Large range
    # Sorted: [1, 2, 9, 10]
    # Pairs: (1+10)=11, (2+9)=11. Max = 11.
    run_test(3, [1, 10, 2, 9], 11)

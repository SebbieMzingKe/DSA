class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        min_val = min(nums)
        max_val = max(nums)
        num_set = set(nums)

        missing = []

        for i in range(min_val + 1, max_val):
            if i not in num_set:
                missing.append(i)

        return missing


if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, nums, expected):
        result = solver.findMissingElements(nums)
        status = "PASS" if result == expected else "FAIL"

        print(f"Test Case {case_num}:")
        print(f"  Input:    {nums}")
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}")
        print(f"  Status:   {status}\n")

    # Example 1
    run_test(1, [1, 4, 2, 5], [3])

    # Example 2
    run_test(2, [7, 8, 6, 9], [])

    # Example 3
    run_test(3, [5, 1], [2, 3, 4])

    # Custom Case 4: Long gap
    run_test(4, [10, 20], [11, 12, 13, 14, 15, 16, 17, 18, 19])

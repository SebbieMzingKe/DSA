class Solution(object):
    def separateDigits(self, nums):
        ans = []
        for i in nums:
           for j in str(i):
              ans.append(int(j))

        return ans


if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, nums, expected):
        result = solver.separateDigits(nums)
        status = "PASS" if result == expected else "FAIL"

        print(f"Test Case {case_num}:")
        print(f"  Input:    {nums}")
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}")
        print(f"  Status:   {status}\n")

    # Example 1
    run_test(1, [13, 25, 83, 77], [1, 3, 2, 5, 8, 3, 7, 7])

    # Example 2
    run_test(2, [7, 1, 3, 9], [7, 1, 3, 9])

    # Custom Case 3: A single large number with a zero
    run_test(3, [10921], [1, 0, 9, 2, 1])

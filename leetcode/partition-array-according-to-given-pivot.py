class Solution(object):
    def pivotArray(self, nums, pivot):
        less = []
        equal = []
        greater = []

        for num in nums:
            if num < pivot:
                less.append(num)

            elif num == pivot:
                equal.append(num)

            else:
                greater.append(num)

        return less + equal + greater


if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, nums, pivot, expected):
        # We pass a copy of nums (nums[:]) so printing later isn't affected if mutated
        result = solver.pivotArray(nums[:], pivot)
        status = "PASS" if result == expected else "FAIL"

        print(f"Test Case {case_num}:")
        print(f"  Input:    nums = {nums}, pivot = {pivot}")
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}")
        print(f"  Status:   {status}\n")

    # Example 1
    run_test(1, [9, 12, 5, 10, 14, 3, 10], 10, [9, 5, 3, 10, 10, 12, 14])

    # Example 2
    run_test(2, [-3, 4, 3, 2], 2, [-3, 2, 4, 3])

    # Custom Case 3: All elements are the same
    run_test(3, [7, 7, 7, 7], 7, [7, 7, 7, 7])

    # Custom Case 4: Pivot is larger than all elements
    run_test(4, [1, 2, 3], 5, [1, 2, 3])

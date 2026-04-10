class Solution(object):
    def minimumDistance(self, nums):
        n = len(nums)
        min_dist = float("inf")

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if nums[i] == nums[j] == nums[k]:
                        dist = 2 * (k - i)
                        if dist < min_dist:
                            min_dist = dist

        return -1 if min_dist == float("inf") else min_dist


if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, nums, expected):
        result = solver.minimumDistance(nums)
        status = "PASS" if result == expected else "FAIL"

        print(f"Test Case {case_num}:")
        print(f"  Input:    {nums}")
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}")
        print(f"  Status:   {status}\n")

    # Example 1
    run_test(1, [1, 2, 1, 1, 3], 6)

    # Example 2
    run_test(2, [1, 1, 2, 3, 2, 1, 2], 8)

    # Example 3
    run_test(3, [1], -1)

    # Custom Case 4: Adjacent triplet
    run_test(4, [5, 5, 5], 4)

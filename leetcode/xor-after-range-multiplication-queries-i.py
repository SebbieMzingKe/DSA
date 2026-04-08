class Solution(object):
    def xorAfterQueries(self, nums, queries):
        MOD = 10**9 + 7

        for l, r, k, v in queries:
            idx = l
            while idx <= r:
                nums[idx] = (nums[idx] * v) % MOD
                idx += k

        final_xor = 0
        for num in nums:
            final_xor ^= num

        return final_xor


if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, nums, queries, expected):
        # We pass a copy of nums (nums[:]) so the original list isn't mutated during printing
        result = solver.xorAfterQueries(nums[:], queries)
        status = "PASS" if result == expected else "FAIL"

        print(f"Test Case {case_num}:")
        print(f"  Input nums: {nums}")
        print(f"  Queries:    {queries}")
        print(f"  Output:     {result}")
        print(f"  Expected:   {expected}")
        print(f"  Status:     {status}\n")

    # Example 1
    run_test(1, [1, 1, 1], [[0, 2, 1, 4]], 4)

    # Example 2
    run_test(2, [2, 3, 1, 5, 4], [[1, 4, 2, 3], [0, 2, 1, 2]], 31)

    # Custom Case: Single element
    run_test(3, [5], [[0, 0, 1, 2]], 10)

    # Custom Case: Large step (k > length of range)
    run_test(4, [1, 2, 3, 4], [[0, 3, 10, 5]], 4)  # Only index 0 gets multiplied by 5

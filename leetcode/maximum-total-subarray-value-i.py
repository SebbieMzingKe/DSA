class Solution(object):
    def maxTotalValue(self, nums, k):
        return (max(nums) - min(nums)) * k


if __name__ == "__main__":
    solver = Solution()
    
    def run_test(case_num, nums, k, expected):
        result = solver.maxTotalValue(nums, k)
        status = "PASS" if result == expected else "FAIL"
        
        print(f"Test Case {case_num}:")
        print(f"  Nums:     {nums}")
        print(f"  k:        {k}")
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}")
        print(f"  Status:   {status}\n")

    # Example 1
    run_test(1, [1, 3, 2], 2, 4)

    # Example 2
    run_test(2, [4, 2, 5, 1], 3, 12)

    # Custom Case 3: All elements the same (difference should be 0)
    run_test(3, [7, 7, 7, 7], 10, 0)
    
    # Custom Case 4: Large k
    run_test(4, [100, 1], 1000, 99000)
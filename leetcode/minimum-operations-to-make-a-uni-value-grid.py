class Solution(object):
    def minOperations(self, grid, x):
        nums = []
        
        for row in grid:
            nums.extend(row)

        target_mod = nums[0] % x

        for num in nums:
            if num % x != target_mod:
                return -1
        
        nums.sort()
        median = nums[len(nums) // 2]

        operations = 0
        for num in nums:
            operations += abs(num - median) // x
        
        return operations

if __name__ == "__main__":
    solver = Solution()
    
    def run_test(case_num, grid, x, expected):
        result = solver.minOperations(grid, x)
        status = "PASS" if result == expected else "FAIL"
        
        print(f"Test Case {case_num}:")
        print(f"  Grid:     {grid}")
        print(f"  x:        {x}")
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}")
        print(f"  Status:   {status}\n")

    # Example 1
    run_test(1, [[2, 4], [6, 8]], 2, 4)

    # Example 2
    run_test(2, [[1, 5], [2, 3]], 1, 5)

    # Example 3
    run_test(3, [[1, 2], [3, 4]], 2, -1)
    
    # Custom Case: Single element grid
    run_test(4, [[146]], 86, 0)
    
    # Custom Case: All elements already equal
    run_test(5, [[5, 5], [5, 5]], 3, 0)


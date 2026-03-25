class Solution(object):
    def canPartitionGrid(self, grid):
        m, n = len(grid), len(grid[0])
        
        row_sums = [sum(row) for row in grid]
        total_sum = sum(row_sums)
        
        if total_sum % 2 != 0:
            return False
            
        target = total_sum // 2
        
        current_sum = 0
        for i in range(m - 1):
            current_sum += row_sums[i]
            if current_sum == target:
                return True
                
        col_sums = [0] * n
        for i in range(m):
            for j in range(n):
                col_sums[j] += grid[i][j]
                
        current_sum = 0
        for j in range(n - 1):
            current_sum += col_sums[j]
            if current_sum == target:
                return True
                
        return False

if __name__ == "__main__":
    solver = Solution()
    
    def run_test(case_num, grid, expected):
        result = solver.canPartitionGrid(grid)
        status = "PASS" if result == expected else "FAIL"
        
        print(f"Test Case {case_num}:")
        print("  Grid:")
        for row in grid:
            print(f"    {row}")
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}")
        print(f"  Status:   {status}\n")

    # Example 1
    # Horizontal cut between row 0 and 1: [1,4] (sum 5) and [2,3] (sum 5)
    run_test(1, [[1,4],[2,3]], True)

    # Example 2
    # Total sum is 10. Rows: 4, 6. Cols: 3, 7. Neither equals 5.
    run_test(2, [[1,3],[2,4]], False)

    # Custom Case 3: Vertical cut works
    # Col 0: 3, Col 1: 3, Col 2: 6. Split after col 1: (3+3) = 6. 
    run_test(3, [[1,1,2],[2,2,4]], True)
    
    # Custom Case 4: Total sum is odd (Quick exit)
    run_test(4, [[1,1],[1,2]], False)
    
    # Custom Case 5: 1D grid row
    # Total sum 6. Split after index 1 -> 1+2 = 3.
    run_test(5, [[1, 2, 3]], True)